# -*- coding: utf-8 -*-
# pylint: disable=attribute-defined-outside-init

"""pdok-reverse-geocoder.py: QGIS Processing tool for reverse geocoding with the PDOK \
   Locatieserver. Tested with QGIS version 3.16, but will probably work with any \
   3.X version.
"""
import traceback
import os.path
import textwrap

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, QVariant

from qgis.core import (
    QgsProject,
    QgsProcessing,
    QgsField,
    QgsGeometry,
    QgsPointXY,
    QgsWkbTypes,
    QgsFeature,
    QgsUnitTypes,
    QgsFeatureSink,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterDistance,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterEnum,
    QgsProcessingParameterString,
    QgsProcessingParameterFeatureSink,
)

from pdokservicesplugin.lib.util import (
    get_processing_error_message,
)

from pdokservicesplugin.lib.http_client import PdokServicesNetworkException

from ..lib.locatieserver import (
    LsType,
    reverse_lookup,
    TypeFilter,
)


class PDOKReverseGeocoder(QgsProcessingAlgorithm):
    """
    This processing tool queries the PDOK Locatieserver reverse geocoder service for each point in the input
    layer and adds the first result to the target attribute.
    """

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate("Processing", string)

    def createInstance(self):
        # Must return a new copy of your tool.
        return PDOKReverseGeocoder()

    def name(self):
        """
        Returns the unique tool name.
        """
        return "pdok-reverse-geocoder"

    def displayName(self):
        """
        Returns the translated tool name.
        """
        return self.tr("PDOK Reverse Geocoder")

    def group(self):
        """
        Returns the name of the group this tool belongs to.
        """
        return self.tr("Locatie Server")

    def icon(self):
        provider_path = os.path.dirname(__file__)
        plugin_path = os.path.dirname(provider_path)
        img_path = os.path.join(plugin_path, "resources", "icon_pdok.svg")

        icon = QtGui.QIcon(img_path)
        return icon

    def groupId(self):
        """
        Returns the unique ID of the group this tool belongs
        to.
        """
        return "pdok-locatie-server"

    def shortHelpString(self):
        """
        Returns a localised short help string for the tool.
        """
        return self.tr(
            textwrap.dedent(
                """
                Deze processing tool bevraagt de PDOK-Locatieserver reverse-geocoder-service voor elk punt in de input-laag and voegt het geselecteerde veld uit het resultaat van de reverse-geocoder-service toe aan dit punt. 
                
                Zie ook de PDOK Locatieserver reverse geocoding API <a href="https://github.com/PDOK/locatieserver/wiki/API-Reverse-Geocoder">documentatie</a>
                
                <h3>Parameters</h3>
                <dl>
                    <dt><b>Input point layer</b></dt>
                    <dd>voor elke feature in de input-laag wordt de reverse-geocoder-service bevraagd</dd>
                    <dt><b>Fields</b> - <em>default value: <tt>weergavenaam</tt></em></dt>
                    <dd>velden (kommagescheiden lijst) uit het reverse-geocoder-resultaat om toe te voegen aan de inputlaag, default is <tt>weergavenaam</tt> (N.B. in de output-laag wordt het veld <tt>weergavenaam</tt> hernoemd naar <tt>weergavenaam_{result_type}</tt>)</dd>
                    <dt><b>Result type</b> - <em>default value: <tt>adres</tt></em></dt>
                    <dd>Op te bevragen Locatieserver result-type (adres, buurt etc) </dd>
                    <dt><b>Score threshold [optional]</b></dt>
                    <dd>resultaten van de geocoder bevatten een score die een indicatie geven van hoe goed het resultaat matcht met de query, resultaten met een score lager dan de score threshold worden achterwege gelaten</dd>
                    <dt><b>Output point layer</b></dt>
                    <dd>outputlaag met het resultaat van de geocoder met de toegevoegde attributen van het reverse geocoder resultaat, projectie hetzelfde als de inputlaag</dd>
                </dl>
                """
            )
        )

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and outputs of the tool.
        """

        self.predicates = [
            (ls_type.value, self.tr(ls_type.value)) for ls_type in LsType
        ]
        self.INPUT = "INPUT"  # recommended name for the main input parameter
        self.FIELDS = "FIELDS"
        self.RESULT_TYPE = "RESULT_TYPE"
        self.DISTANCE_THRESHOLD = "DISTANCE_THRESHOLD"
        self.OUTPUT = "OUTPUT"  # recommended name for the main output parameter

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr("Input point layer"),
                types=[QgsProcessing.TypeVectorPoint],
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT, self.tr("Output point layer")
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.FIELDS,
                self.tr("Fields (comma seperated list)"),
                defaultValue="weergavenaam",
                optional=False,
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.RESULT_TYPE,
                self.tr("Result type to query"),
                options=[p[1] for p in self.predicates],
                defaultValue=0,
                optional=False,
            )
        )
        dist_param = QgsProcessingParameterDistance(
            self.DISTANCE_THRESHOLD,
            self.tr("Score threshold"),
            defaultValue=None,
            optional=True,
            minValue=0,
        )
        dist_param.setDefaultUnit(QgsUnitTypes.DistanceMeters)
        self.addParameter(dist_param)

    def processAlgorithm(self, parameters, context, feedback):
        try:
            # read out algorithm parameters
            input_points = self.parameterAsVectorLayer(parameters, self.INPUT, context)
            distance_threshold = parameters[self.DISTANCE_THRESHOLD]
            result_type_str = [
                self.predicates[i][0]
                for i in self.parameterAsEnums(parameters, self.RESULT_TYPE, context)
            ][0]
            result_type = LsType[result_type_str]
            input_fields = [x.strip() for x in parameters[self.FIELDS].split(",")]
            input_layer_fields = input_points.fields()
            input_layer_fields_names = [field.name() for field in input_layer_fields]
            field_mapping = {}

            for input_field in input_fields:
                mapped_field_name = input_field
                if input_field == "weergavenaam":
                    mapped_field_name = f"weergavenaam_{result_type.value}"
                # TODO: improve field mapping, since no check if ls_{input_field} exists
                # in input_layer_fields_names
                if mapped_field_name in input_layer_fields_names:
                    mapped_field_name = f"ls_{input_field}"
                field_mapping[input_field] = mapped_field_name

            for input_field in input_fields:
                input_layer_fields.append(
                    QgsField(field_mapping[input_field], QVariant.String)
                )

            (sink, dest_id) = self.parameterAsSink(
                parameters,
                self.OUTPUT,
                context,
                input_layer_fields,
                QgsWkbTypes.Point,
                input_points.sourceCrs(),
            )

            # Setup transformation if required
            in_crs = input_points.crs()
            out_crs = QgsCoordinateReferenceSystem.fromEpsgId(28992)
            transform = None
            if in_crs.authid() != "EPSG:28992":
                transform = QgsCoordinateTransform(
                    in_crs, out_crs, QgsProject.instance()
                )

            if feedback.isCanceled():
                return {}

            # start processing features
            for point in input_points.getFeatures():
                geom = point.geometry()
                fid = point.id()
                if transform:
                    geom.transform(transform)

                point_geom = QgsGeometry.asPoint(geom)
                pxy = QgsPointXY(point_geom)
                x_coord = pxy.x()
                y_coord = pxy.y()

                # afstand field required, add if not requested by user
                if "afstand" not in input_fields:
                    input_fields.append("afstand")
                data = reverse_lookup(
                    x_coord, y_coord, input_fields, TypeFilter([result_type])
                )
                # TODO: add exception handling reverse_lookup

                result = None
                if len(data) > 0:
                    if (
                        distance_threshold is not None
                        and data[0]["afstand"] > distance_threshold
                    ):
                        distance = data[0]["afstand"]
                        feedback.pushInfo(
                            f"feature id: {fid} - distance threshold ({distance_threshold}) exceeded: {distance}"
                        )
                        continue  # we will NOT add this feature to the output! Go to next feature...
                    else:
                        result = {}
                        for key in field_mapping:
                            if key in data[0]:
                                result[key] = data[0][key]
                            else:
                                feedback.pushInfo(
                                    f'feature id: {fid} - field "{key}" not in response'
                                )
                else:
                    feedback.pushInfo(
                        f"feature id: {fid} - no objects found for x,y ({x_coord},{y_coord}) with result_type: {result_type.value}"
                    )

                attrs = point.attributes()
                new_ft = QgsFeature(input_layer_fields)

                for i in range(len(attrs)):
                    attr = attrs[i]
                    field_name = input_layer_fields_names[i]
                    new_ft.setAttribute(field_name, attr)

                for key in result:
                    new_ft.setAttribute(field_mapping[key], result[key])

                new_ft.setGeometry(point.geometry())
                sink.addFeature(new_ft, QgsFeatureSink.FastInsert)

                if feedback.isCanceled():
                    return {}

            results = {}
            results[self.OUTPUT] = dest_id
            return results
        except PdokServicesNetworkException as pdok_ex:
            message = get_processing_error_message(
                "an error",
                self.displayName(),
                pdok_ex,
                traceback.format_exc(),
                "while executing HTTP request",
            )
            raise QgsProcessingException(message)
        except Exception as ex:
            message = get_processing_error_message(
                "an unexpected error",
                self.displayName(),
                ex,
                traceback.format_exc(),
            )
            raise QgsProcessingException(message)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pdokservicesplugindialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PdokServicesPlugin(object):
    def setupUi(self, PdokServicesPlugin):
        PdokServicesPlugin.setObjectName("PdokServicesPlugin")
        PdokServicesPlugin.resize(838, 944)
        self.verticalLayout = QtWidgets.QVBoxLayout(PdokServicesPlugin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(PdokServicesPlugin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.layers_tab = QtWidgets.QWidget()
        self.layers_tab.setObjectName("layers_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layers_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.servicesView = QtWidgets.QTableView(self.layers_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.servicesView.sizePolicy().hasHeightForWidth())
        self.servicesView.setSizePolicy(sizePolicy)
        self.servicesView.setMinimumSize(QtCore.QSize(0, 0))
        self.servicesView.setObjectName("servicesView")
        self.gridLayout_2.addWidget(self.servicesView, 1, 0, 1, 4)
        self.layerInfo = QtWidgets.QTextBrowser(self.layers_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerInfo.sizePolicy().hasHeightForWidth())
        self.layerInfo.setSizePolicy(sizePolicy)
        self.layerInfo.setMaximumSize(QtCore.QSize(16777215, 300))
        self.layerInfo.setOpenExternalLinks(True)
        self.layerInfo.setObjectName("layerInfo")
        self.gridLayout_2.addWidget(self.layerInfo, 2, 0, 1, 4)
        self.layerSearch = QtWidgets.QLineEdit(self.layers_tab)
        self.layerSearch.setClearButtonEnabled(True)
        self.layerSearch.setObjectName("layerSearch")
        self.gridLayout_2.addWidget(self.layerSearch, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layers_tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.layerOptionsGroupbox = QtWidgets.QGroupBox(self.layers_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.layerOptionsGroupbox.sizePolicy().hasHeightForWidth()
        )
        self.layerOptionsGroupbox.setSizePolicy(sizePolicy)
        self.layerOptionsGroupbox.setTitle("")
        self.layerOptionsGroupbox.setObjectName("layerOptionsGroupbox")
        self.formLayout = QtWidgets.QFormLayout(self.layerOptionsGroupbox)
        self.formLayout.setObjectName("formLayout")
        self.wmsStyleLabel = QtWidgets.QLabel(self.layerOptionsGroupbox)
        self.wmsStyleLabel.setObjectName("wmsStyleLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.wmsStyleLabel
        )
        self.wmsStyleComboBox = QtWidgets.QComboBox(self.layerOptionsGroupbox)
        self.wmsStyleComboBox.setEditable(True)
        self.wmsStyleComboBox.setObjectName("wmsStyleComboBox")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.wmsStyleComboBox
        )
        self.labelCrs = QtWidgets.QLabel(self.layerOptionsGroupbox)
        self.labelCrs.setObjectName("labelCrs")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCrs)
        self.comboSelectProj = QtWidgets.QComboBox(self.layerOptionsGroupbox)
        self.comboSelectProj.setObjectName("comboSelectProj")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.comboSelectProj
        )
        self.labelAddLayer = QtWidgets.QLabel(self.layerOptionsGroupbox)
        self.labelAddLayer.setObjectName("labelAddLayer")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.labelAddLayer
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadLayer = QtWidgets.QPushButton(self.layerOptionsGroupbox)
        self.btnLoadLayer.setEnabled(False)
        self.btnLoadLayer.setObjectName("btnLoadLayer")
        self.horizontalLayout.addWidget(self.btnLoadLayer)
        self.btnLoadLayerTop = QtWidgets.QPushButton(self.layerOptionsGroupbox)
        self.btnLoadLayerTop.setEnabled(False)
        self.btnLoadLayerTop.setObjectName("btnLoadLayerTop")
        self.horizontalLayout.addWidget(self.btnLoadLayerTop)
        self.btnLoadLayerBottom = QtWidgets.QPushButton(self.layerOptionsGroupbox)
        self.btnLoadLayerBottom.setEnabled(False)
        self.btnLoadLayerBottom.setObjectName("btnLoadLayerBottom")
        self.horizontalLayout.addWidget(self.btnLoadLayerBottom)
        self.formLayout.setLayout(
            5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout
        )
        self.gridLayout_2.addWidget(self.layerOptionsGroupbox, 3, 0, 1, 4)
        self.tabWidget.addTab(self.layers_tab, "")
        self.ls_tab = QtWidgets.QWidget()
        self.ls_tab.setObjectName("ls_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ls_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.geocoderSearch = QtWidgets.QLineEdit(self.ls_tab)
        self.geocoderSearch.setText("")
        self.geocoderSearch.setObjectName("geocoderSearch")
        self.gridLayout_4.addWidget(self.geocoderSearch, 0, 1, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.ls_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cbx_wpl = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_wpl.setChecked(True)
        self.cbx_wpl.setObjectName("cbx_wpl")
        self.gridLayout_5.addWidget(self.cbx_wpl, 1, 0, 1, 1)
        self.cbx_gem = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_gem.setChecked(True)
        self.cbx_gem.setObjectName("cbx_gem")
        self.gridLayout_5.addWidget(self.cbx_gem, 0, 0, 1, 1)
        self.cbx_pcd = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_pcd.setChecked(True)
        self.cbx_pcd.setObjectName("cbx_pcd")
        self.gridLayout_5.addWidget(self.cbx_pcd, 3, 0, 1, 1)
        self.cbx_weg = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_weg.setChecked(True)
        self.cbx_weg.setObjectName("cbx_weg")
        self.gridLayout_5.addWidget(self.cbx_weg, 2, 0, 1, 1)
        self.cbx_pcl = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_pcl.setChecked(True)
        self.cbx_pcl.setObjectName("cbx_pcl")
        self.gridLayout_5.addWidget(self.cbx_pcl, 1, 1, 1, 1)
        self.cbx_hmp = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_hmp.setChecked(True)
        self.cbx_hmp.setObjectName("cbx_hmp")
        self.gridLayout_5.addWidget(self.cbx_hmp, 2, 1, 1, 1)
        self.cbx_adr = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_adr.setChecked(True)
        self.cbx_adr.setObjectName("cbx_adr")
        self.gridLayout_5.addWidget(self.cbx_adr, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.ls_tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.geocoderResultView = QtWidgets.QTableView(self.ls_tab)
        self.geocoderResultView.setObjectName("geocoderResultView")
        self.gridLayout_4.addWidget(self.geocoderResultView, 3, 0, 1, 3)
        self.lookupinfo = QtWidgets.QTextBrowser(self.ls_tab)
        self.lookupinfo.setOpenExternalLinks(True)
        self.lookupinfo.setObjectName("lookupinfo")
        self.gridLayout_4.addWidget(self.lookupinfo, 4, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.ls_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.geocoderResultSearch = QtWidgets.QLineEdit(self.ls_tab)
        self.geocoderResultSearch.setObjectName("geocoderResultSearch")
        self.gridLayout_4.addWidget(self.geocoderResultSearch, 2, 1, 1, 2)
        self.tabWidget.addTab(self.ls_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.settings_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout1.setContentsMargins(0, 0, 0, 0)
        self.formLayout1.setObjectName("formLayout1")
        self.nr_favs_input = QtWidgets.QSpinBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nr_favs_input.sizePolicy().hasHeightForWidth()
        )
        self.nr_favs_input.setSizePolicy(sizePolicy)
        self.nr_favs_input.setMinimum(1)
        self.nr_favs_input.setMaximum(10)
        self.nr_favs_input.setObjectName("nr_favs_input")
        self.formLayout1.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.nr_favs_input
        )
        self.nr_favs_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.nr_favs_label.setObjectName("nr_favs_label")
        self.formLayout1.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.nr_favs_label
        )
        self.tabWidget.addTab(self.settings_tab, "")
        self.about_tab = QtWidgets.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.about_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.webView = QtWidgets.QTextBrowser(self.about_tab)
        self.webView.setOpenExternalLinks(True)
        self.webView.setObjectName("webView")
        self.gridLayout_3.addWidget(self.webView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.about_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(PdokServicesPlugin)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PdokServicesPlugin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PdokServicesPlugin)

    def retranslateUi(self, PdokServicesPlugin):
        _translate = QtCore.QCoreApplication.translate
        PdokServicesPlugin.setWindowTitle(
            _translate("PdokServicesPlugin", "PDOK Services Plugin")
        )
        self.layerSearch.setPlaceholderText(
            _translate(
                "PdokServicesPlugin",
                'Start met het type service en dan overige termen, bv "wfs cbs provincie"',
            )
        )
        self.label.setText(_translate("PdokServicesPlugin", "Zoeken"))
        self.wmsStyleLabel.setText(_translate("PdokServicesPlugin", "Style"))
        self.labelCrs.setText(_translate("PdokServicesPlugin", "CRS"))
        self.labelAddLayer.setText(_translate("PdokServicesPlugin", "Laag toevoegen"))
        self.btnLoadLayer.setToolTip(
            _translate("PdokServicesPlugin", "Boven actieve kaartlaag toevoegen")
        )
        self.btnLoadLayer.setText(_translate("PdokServicesPlugin", "Standaard"))
        self.btnLoadLayerTop.setToolTip(
            _translate("PdokServicesPlugin", "Als bovenste kaartlaag toevoegen")
        )
        self.btnLoadLayerTop.setText(_translate("PdokServicesPlugin", "Boven"))
        self.btnLoadLayerBottom.setToolTip(
            _translate("PdokServicesPlugin", "Als onderste kaartlaag toevoegen")
        )
        self.btnLoadLayerBottom.setText(_translate("PdokServicesPlugin", "Onder"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.layers_tab),
            _translate("PdokServicesPlugin", "PDOK services"),
        )
        self.groupBox_3.setTitle(
            _translate(
                "PdokServicesPlugin",
                "Zoek alleen type (zie https://github.com/PDOK/locatieserver/wiki/Zoekvoorbeelden-Locatieserver voor defaults)",
            )
        )
        self.cbx_wpl.setText(_translate("PdokServicesPlugin", "Woonplaats"))
        self.cbx_gem.setText(_translate("PdokServicesPlugin", "Gemeente"))
        self.cbx_pcd.setText(_translate("PdokServicesPlugin", "Postcode"))
        self.cbx_weg.setText(
            _translate("PdokServicesPlugin", "Weg (BAG openbare ruimte)")
        )
        self.cbx_pcl.setText(_translate("PdokServicesPlugin", "Perceel"))
        self.cbx_hmp.setText(_translate("PdokServicesPlugin", "Hectometerpaal"))
        self.cbx_adr.setText(_translate("PdokServicesPlugin", "Adres"))
        self.pushButton.setText(_translate("PdokServicesPlugin", "Toggle All/None"))
        self.label_6.setText(
            _translate("PdokServicesPlugin", "Zoek (ook voor snelzoektoolbar)")
        )
        self.label_2.setText(
            _translate("PdokServicesPlugin", "Filter resultaten hieronder op:")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.ls_tab),
            _translate("PdokServicesPlugin", "PDOK Locatieserver"),
        )
        self.nr_favs_label.setText(
            _translate("PdokServicesPlugin", "Aantal favorieten")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.settings_tab),
            _translate("PdokServicesPlugin", "Instellingen"),
        )
        self.webView.setHtml(
            _translate(
                "PdokServicesPlugin",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">QGIS plugin voor PDOK services</span><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> </span></h1>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">Deze plugin wordt gemaakt door Richard Duivenvoorde (</span><a href=\"http://www.zuidt.nl\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">Zuidt</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">). <br /><br />De code van deze plugin is te vinden op </span><a href=\"https://github.com/rduivenvoorde/pdokservicesplugin\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">Github</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">. Bugs kunt u daar melden. </span></p>\n"
                "<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">PDOK</span><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> </span></h2>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><img src=\":/plugins/pdokservicesplugin/resources/pdok.png\" style=\"float: left;\" /><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> </span><a href=\"http://www.pdok.nl\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">PDOK</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> stelt webservices beschikbaar van landsdekkende geo-informatie afkomstig van overheden. Deze data komen rechtstreeks bij de bron vandaan, d.w.z. dat overheidsorganisaties bronhouder van deze data zijn. Daardoor zijn de data actueel en betrouwbaar. Bovendien zijn ze door elke afnemer (overheid, bedrijf, particulier) kosteloos te gebruiken. </span></p>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">De lijst van services en lagen in deze plugin worden met behulp van het </span><span style=\" font-family:'monospace'; font-size:11pt; font-weight:296; color:#444444;\">pdokservicesspider</span><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> script gegeneerd (te vinden op </span><a href=\"https://github.com/rduivenvoorde/pdokservicesplugin\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">Github</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">). Dit script genereert deze lijst op basis van de </span><a href=\"https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?service=CSW&amp;request=GetCapabilities&amp;version=2.0.2\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">CSW service</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> van het </span><a href=\"https://www.nationaalgeoregister.nl/\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">Nationaal Georegister</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">. </span></p>\n"
                "<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">OpenGeoGroep. Anders denken, Anders doen...</span><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> </span></h2>\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:162.5%;\"><img src=\":/plugins/pdokservicesplugin/resources/ogg.gif\" style=\"float: left;\" /><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\">De </span><a href=\"http://www.opengeogroep.nl\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; text-decoration: underline; color:#0000ff;\">OpenGeoGroep</span></a><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif'; font-size:11pt; font-weight:296; color:#444444;\"> is een commerciele ICT-dienstverlener die diensten en oplossingen biedt voor geo-informatie vraagstukken. Al onze diensten zijn leveranciersonafhankelijk. De OpenGeoGroep onderscheidt zich door het aanbieden van diensten en innovatieve oplossingen gebaseerd op professionele Open Source Software en op basis van Open Standaarden.</span><span style=\" font-family:'Ubuntu'; font-size:11pt;\"> </span></p></body></html>",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.about_tab),
            _translate("PdokServicesPlugin", "OpenGeoGroep en PDOK"),
        )

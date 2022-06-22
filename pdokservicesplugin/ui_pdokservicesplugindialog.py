# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pdokservicesplugindialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PdokServicesPlugin(object):
    def setupUi(self, PdokServicesPlugin):
        PdokServicesPlugin.setObjectName("PdokServicesPlugin")
        PdokServicesPlugin.resize(838, 944)
        self.verticalLayout = QtWidgets.QVBoxLayout(PdokServicesPlugin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(PdokServicesPlugin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.servicesView.sizePolicy().hasHeightForWidth())
        self.servicesView.setSizePolicy(sizePolicy)
        self.servicesView.setMinimumSize(QtCore.QSize(0, 0))
        self.servicesView.setObjectName("servicesView")
        self.gridLayout_2.addWidget(self.servicesView, 1, 0, 1, 4)
        self.layer_info = QtWidgets.QTextBrowser(self.layers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_info.sizePolicy().hasHeightForWidth())
        self.layer_info.setSizePolicy(sizePolicy)
        self.layer_info.setMaximumSize(QtCore.QSize(16777215, 300))
        self.layer_info.setOpenExternalLinks(True)
        self.layer_info.setObjectName("layer_info")
        self.gridLayout_2.addWidget(self.layer_info, 2, 0, 1, 4)
        self.layerSearch = QtWidgets.QLineEdit(self.layers_tab)
        self.layerSearch.setClearButtonEnabled(True)
        self.layerSearch.setObjectName("layerSearch")
        self.gridLayout_2.addWidget(self.layerSearch, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layers_tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.layer_options_groupbox = QtWidgets.QGroupBox(self.layers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_options_groupbox.sizePolicy().hasHeightForWidth())
        self.layer_options_groupbox.setSizePolicy(sizePolicy)
        self.layer_options_groupbox.setTitle("")
        self.layer_options_groupbox.setObjectName("layer_options_groupbox")
        self.formLayout = QtWidgets.QFormLayout(self.layer_options_groupbox)
        self.formLayout.setObjectName("formLayout")
        self.wmsStyleLabel = QtWidgets.QLabel(self.layer_options_groupbox)
        self.wmsStyleLabel.setObjectName("wmsStyleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wmsStyleLabel)
        self.wmsStyleComboBox = QtWidgets.QComboBox(self.layer_options_groupbox)
        self.wmsStyleComboBox.setEditable(True)
        self.wmsStyleComboBox.setObjectName("wmsStyleComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wmsStyleComboBox)
        self.labelCrs = QtWidgets.QLabel(self.layer_options_groupbox)
        self.labelCrs.setObjectName("labelCrs")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCrs)
        self.comboSelectProj = QtWidgets.QComboBox(self.layer_options_groupbox)
        self.comboSelectProj.setObjectName("comboSelectProj")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboSelectProj)
        self.labelAddLayer = QtWidgets.QLabel(self.layer_options_groupbox)
        self.labelAddLayer.setObjectName("labelAddLayer")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelAddLayer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadLayer = QtWidgets.QPushButton(self.layer_options_groupbox)
        self.btnLoadLayer.setEnabled(False)
        self.btnLoadLayer.setObjectName("btnLoadLayer")
        self.horizontalLayout.addWidget(self.btnLoadLayer)
        self.btnLoadLayerTop = QtWidgets.QPushButton(self.layer_options_groupbox)
        self.btnLoadLayerTop.setEnabled(False)
        self.btnLoadLayerTop.setObjectName("btnLoadLayerTop")
        self.horizontalLayout.addWidget(self.btnLoadLayerTop)
        self.btnLoadLayerBottom = QtWidgets.QPushButton(self.layer_options_groupbox)
        self.btnLoadLayerBottom.setEnabled(False)
        self.btnLoadLayerBottom.setObjectName("btnLoadLayerBottom")
        self.horizontalLayout.addWidget(self.btnLoadLayerBottom)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout_2.addWidget(self.layer_options_groupbox, 3, 0, 1, 4)
        self.tabWidget.addTab(self.layers_tab, "")
        self.ls_tab = QtWidgets.QWidget()
        self.ls_tab.setObjectName("ls_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ls_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.ls_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.lookupinfo = QtWidgets.QTextBrowser(self.ls_tab)
        self.lookupinfo.setOpenExternalLinks(True)
        self.lookupinfo.setObjectName("lookupinfo")
        self.gridLayout_4.addWidget(self.lookupinfo, 4, 0, 1, 3)
        self.geocoderSearch = QtWidgets.QLineEdit(self.ls_tab)
        self.geocoderSearch.setText("")
        self.geocoderSearch.setObjectName("geocoderSearch")
        self.gridLayout_4.addWidget(self.geocoderSearch, 0, 1, 1, 2)
        self.geocoderResultView = QtWidgets.QTableView(self.ls_tab)
        self.geocoderResultView.setObjectName("geocoderResultView")
        self.gridLayout_4.addWidget(self.geocoderResultView, 3, 0, 1, 3)
        self.geocoderResultSearch = QtWidgets.QLineEdit(self.ls_tab)
        self.geocoderResultSearch.setObjectName("geocoderResultSearch")
        self.gridLayout_4.addWidget(self.geocoderResultSearch, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.ls_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.ls_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cbx_gem = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_gem.setChecked(True)
        self.cbx_gem.setObjectName("cbx_gem")
        self.gridLayout_5.addWidget(self.cbx_gem, 0, 0, 1, 1)
        self.cbx_weg = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_weg.setChecked(True)
        self.cbx_weg.setObjectName("cbx_weg")
        self.gridLayout_5.addWidget(self.cbx_weg, 2, 0, 1, 1)
        self.cbx_wpl = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_wpl.setChecked(True)
        self.cbx_wpl.setObjectName("cbx_wpl")
        self.gridLayout_5.addWidget(self.cbx_wpl, 1, 0, 1, 1)
        self.cbx_adr = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_adr.setChecked(True)
        self.cbx_adr.setObjectName("cbx_adr")
        self.gridLayout_5.addWidget(self.cbx_adr, 0, 1, 1, 1)
        self.cbx_pcl = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_pcl.setChecked(True)
        self.cbx_pcl.setObjectName("cbx_pcl")
        self.gridLayout_5.addWidget(self.cbx_pcl, 1, 1, 1, 1)
        self.cbx_hmp = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_hmp.setChecked(True)
        self.cbx_hmp.setObjectName("cbx_hmp")
        self.gridLayout_5.addWidget(self.cbx_hmp, 2, 1, 1, 1)
        self.cbx_pcd = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbx_pcd.setChecked(True)
        self.cbx_pcd.setObjectName("cbx_pcd")
        self.gridLayout_5.addWidget(self.cbx_pcd, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 3)
        self.tabWidget.addTab(self.ls_tab, "")
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PdokServicesPlugin)

    def retranslateUi(self, PdokServicesPlugin):
        _translate = QtCore.QCoreApplication.translate
        PdokServicesPlugin.setWindowTitle(_translate("PdokServicesPlugin", "PDOK Services Plugin"))
        self.layerSearch.setPlaceholderText(_translate("PdokServicesPlugin", "Start met het type service en dan overige termen, bv \"wfs cbs provincie\""))
        self.label.setText(_translate("PdokServicesPlugin", "Zoeken"))
        self.wmsStyleLabel.setText(_translate("PdokServicesPlugin", "Style"))
        self.labelCrs.setText(_translate("PdokServicesPlugin", "CRS"))
        self.labelAddLayer.setText(_translate("PdokServicesPlugin", "Laag toevoegen"))
        self.btnLoadLayer.setToolTip(_translate("PdokServicesPlugin", "Boven actieve kaartlaag toevoegen"))
        self.btnLoadLayer.setText(_translate("PdokServicesPlugin", "Standaard"))
        self.btnLoadLayerTop.setToolTip(_translate("PdokServicesPlugin", "Als bovenste kaartlaag toevoegen"))
        self.btnLoadLayerTop.setText(_translate("PdokServicesPlugin", "Boven"))
        self.btnLoadLayerBottom.setToolTip(_translate("PdokServicesPlugin", "Als onderste kaartlaag toevoegen"))
        self.btnLoadLayerBottom.setText(_translate("PdokServicesPlugin", "Onder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.layers_tab), _translate("PdokServicesPlugin", "PDOK Services"))
        self.label_2.setText(_translate("PdokServicesPlugin", "Filter Resultaten "))
        self.label_6.setText(_translate("PdokServicesPlugin", "Zoek"))
        self.groupBox_3.setTitle(_translate("PdokServicesPlugin", "Zoek Type"))
        self.cbx_gem.setText(_translate("PdokServicesPlugin", "Gemeente"))
        self.cbx_weg.setText(_translate("PdokServicesPlugin", "Weg (BAG openbare ruimte)"))
        self.cbx_wpl.setText(_translate("PdokServicesPlugin", "Woonplaats"))
        self.cbx_adr.setText(_translate("PdokServicesPlugin", "Adres"))
        self.cbx_pcl.setText(_translate("PdokServicesPlugin", "Perceel"))
        self.cbx_hmp.setText(_translate("PdokServicesPlugin", "Hectometerpaal"))
        self.cbx_pcd.setText(_translate("PdokServicesPlugin", "Postcode"))
        self.pushButton.setText(_translate("PdokServicesPlugin", "Toggle All/None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ls_tab), _translate("PdokServicesPlugin", "PDOK Locatieserver"))
        self.webView.setHtml(_translate("PdokServicesPlugin", "<html>\n"
"\n"
"<head>\n"
"  <style>\n"
"    body {\n"
"      color: #444444;\n"
"      font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"      font-size: 15px;\n"
"      font-size-adjust: none;\n"
"      font-stretch: normal;\n"
"      font-style: normal;\n"
"      font-variant: normal;\n"
"      font-weight: 300;\n"
"      line-height: 1.625;\n"
"    }\n"
"  </style>\n"
"\n"
"</head>\n"
"\n"
"<body>\n"
"  <h1>QGIS plugin voor PDOK services</h1>\n"
"  <p>\n"
"    Deze plugin wordt gemaakt door Richard Duivenvoorde (<a href=\"http://www.zuidt.nl\">Zuidt</a>).\n"
"    <br>\n"
"    De code van deze plugin is te vinden op <a href=\"https://github.com/rduivenvoorde/pdokservicesplugin\">Github</a>.\n"
"    Bugs kunt u daar melden.\n"
"  </p>\n"
"\n"
"  <h2>PDOK</h2>\n"
"  <p>\n"
"    <img style=\"margin-right:10px;\" src=\":/plugins/pdokservicesplugin/resources/pdok.png\" align=\"left\" />\n"
"    <a href=\"http://www.pdok.nl\">PDOK</a> stelt webservices beschikbaar van landsdekkende geo-informatie afkomstig van\n"
"    overheden. Deze data komen rechtstreeks bij de bron vandaan, d.w.z. dat overheidsorganisaties bronhouder van deze\n"
"    data zijn. Daardoor zijn de data actueel en betrouwbaar. Bovendien zijn ze door elke afnemer (overheid, bedrijf,\n"
"    particulier) kosteloos te gebruiken.\n"
"  </p>\n"
"  <p>\n"
"    De lijst van services en lagen in deze plugin worden met behulp van het <tt>pdokservicesspider</tt> script\n"
"    gegeneerd (te vinden op <a href=\"https://github.com/rduivenvoorde/pdokservicesplugin\">Github</a>). Dit script\n"
"    genereert deze lijst op basis van de <a\n"
"      href=\"https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?service=CSW&request=GetCapabilities&version=2.0.2\">CSW\n"
"      service</a> van het <a href=\"https://www.nationaalgeoregister.nl/\">Nationaal Georegister</a>.\n"
"  </p>\n"
"\n"
"  <h2>OpenGeoGroep</h2>\n"
"  <h3>Anders denken, Anders doen..</h3>\n"
"  <p><img src=\":/plugins/pdokservicesplugin/ogg.gif\" align=\"left\" />De <a\n"
"      href=\"http://www.opengeogroep.nl\">OpenGeoGroep</a> is een\n"
"    commerciele ICT-dienstverlener die diensten en oplossingen biedt voor geo-informatie vraagstukken. Al onze diensten\n"
"    zijn leveranciersonafhankelijk. De OpenGeoGroep onderscheidt zich door het aanbieden van diensten en innovatieve\n"
"    oplossingen gebaseerd op professionele Open Source Software en op basis van Open Standaarden.</p>\n"
"</body>\n"
"\n"
"</html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), _translate("PdokServicesPlugin", "OpenGeoGroep en PDOK"))

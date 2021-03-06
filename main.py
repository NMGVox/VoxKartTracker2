# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vox Kart TrackerakVVyP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import requests
import re
import os
import csv
import webbrowser
from bs4 import BeautifulSoup

import VoxKartResources


class MainWindow(QMainWindow):
    results_sn = []  # Hold the names of the  servers for id
    server_info = {}  # Use server names ask key to retrieve info about the server (players, ip, number playing)
    filepath = os.path.expanduser('~\\Documents\\VoxKartTracker')
    pref_servers = []
    time_between_ref = 30000

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # if not MainWindow.objectName():
        #     MainWindow.setObjectName(u"MainWindow")
        #  Create and stylize the main window
        self.resize(479, 688)
        self.setMinimumSize(QSize(479, 688))
        self.setMaximumSize(QSize(479, 688))
        font = QFont()
        font.setFamily(u"Arial")
        self.setFont(font)
        self.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u"../../Pictures/SPBMG1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.actionClose = QAction(self)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        #  Create a button that toggles a user's preferred servers
        self.prefToggle = QCheckBox(self.centralwidget)
        self.prefToggle.setObjectName(u"prefToggle")
        self.prefToggle.setGeometry(QRect(30, 600, 211, 17))
        self.prefToggle.setMinimumSize(QSize(211, 17))
        self.prefToggle.setMaximumSize(QSize(211, 17))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.prefToggle.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.prefToggle.setFont(font1)
        self.prefToggle.setCursor(QCursor(Qt.ArrowCursor))
        self.prefToggle.setCheckable(True)
        self.prefToggle.setChecked(False)
        #  End preference button initialization

        #  Initialize the Server Table (Holds names of servers, and how many are currently playing)
        self.servertable = QTableWidget(self.centralwidget)
        self.servertable.setObjectName(u"servertable")
        self.servertable.setGeometry(QRect(26, 108, 251, 481))
        self.servertable.setMinimumSize(QSize(265, 481))
        self.servertable.setMaximumSize(QSize(265, 481))
        self.servertable.setColumnCount(2)
        self.servertable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.servertable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        #  ServerTable Setting Palette
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        brush2 = QBrush(QColor(27, 27, 27, 150))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        brush3 = QBrush(QColor(94, 94, 94, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
        #endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
        #endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        brush5 = QBrush(QColor(240, 240, 240, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
        #endif
        self.servertable.setPalette(palette1)
        self.servertable.setLayoutDirection(Qt.LeftToRight)
        self.servertable.setAutoFillBackground(False)
        self.servertable.setFrameShape(QFrame.NoFrame)
        self.servertable.setFrameShadow(QFrame.Sunken)
        self.servertable.setLineWidth(1)
        self.servertable.setMidLineWidth(1)
        self.servertable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.servertable.setAlternatingRowColors(True)
        self.servertable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.servertable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.servertable.setSortingEnabled(False)
        self.servertable.setRowCount(0)
        self.servertable.horizontalHeader().setVisible(True)
        self.servertable.setHorizontalHeaderLabels(['Server Name', 'Players'])
        self.servertable.horizontalHeader().setHighlightSections(True)
        self.servertable.horizontalHeader().setProperty("showSortIndicator", False)
        self.servertable.verticalHeader().setVisible(False)
        self.servertable.verticalHeader().setHighlightSections(False)

        #  End initialization of server table

        #Initialize the server info table
        self.player_table = QTableWidget(self.centralwidget)
        if (self.player_table.columnCount() < 1):
            self.player_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.player_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.player_table.setObjectName(u"serverinfotable")
        self.player_table.setGeometry(QRect(306, 158, 151, 381))
        self.player_table.setMinimumSize(QSize(151, 381))
        self.player_table.setMaximumSize(QSize(151, 381))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
        #endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
        #endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
        #endif
        self.player_table.setPalette(palette2)
        self.player_table.setAutoFillBackground(False)
        self.player_table.setFrameShape(QFrame.NoFrame)
        self.player_table.setFrameShadow(QFrame.Plain)
        self.player_table.setLineWidth(1)
        self.player_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.player_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.player_table.setAutoScroll(True)
        self.player_table.setAutoScrollMargin(23)
        self.player_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.player_table.setAlternatingRowColors(True)
        self.player_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.player_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.player_table.setTextElideMode(Qt.ElideRight)
        self.player_table.setShowGrid(True)
        self.player_table.setGridStyle(Qt.NoPen)
        self.player_table.setSortingEnabled(False)
        self.player_table.setWordWrap(True)
        self.player_table.setCornerButtonEnabled(True)
        self.player_table.horizontalHeader().setVisible(True)
        self.player_table.horizontalHeader().setCascadingSectionResizes(True)
        self.player_table.verticalHeader().setVisible(False)
        self.player_table.verticalHeader().setCascadingSectionResizes(False)
        self.player_table.verticalHeader().setHighlightSections(False)
        self.player_table.verticalHeader().setStretchLastSection(False)
        self.player_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.player_table.setHorizontalHeaderLabels(["Player Name"])
        self.player_table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        # End of serverinfotable. Should really rename this "playertable" or something later on.

        self.prefbutton = QPushButton(self.centralwidget)
        self.prefbutton.setObjectName(u"prefbutton")
        self.prefbutton.setEnabled(True)
        self.prefbutton.setGeometry(QRect(306, 108, 151, 41))
        self.prefbutton.setMinimumSize(QSize(151, 41))
        self.prefbutton.setMaximumSize(QSize(151, 41))
        self.prefbutton.setFont(font)
        self.prefbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.prefbutton.setStyleSheet(u"QPushButton {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4, 5, 61, 255), stop:1 rgba(21, 22, 46, 255));\n"
                                      "color: \"Silver\";\n"
                                      "border-radius: 10px;}\n"
                                      "\n"
                                      "QPushButton:disabled {\n"
                                      "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(125, 125, 125, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "color:black;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.prefbutton.setEnabled(False)


        self.connectbutton = QPushButton(self.centralwidget)
        self.connectbutton.setObjectName(u"connectbutton")
        self.connectbutton.setEnabled(True)
        self.connectbutton.setGeometry(QRect(310, 550, 141, 41))
        self.connectbutton.setMinimumSize(QSize(141, 41))
        self.connectbutton.setMaximumSize(QSize(141, 41))
        self.connectbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectbutton.setAutoFillBackground(False)
        self.connectbutton.setStyleSheet(u"QPushButton {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4, 5, 61, 255), stop:1 rgba(21, 22, 46, 255));\n"
                                         "color: \"Silver\";\n"
                                         "border-radius: 10px;}\n"
                                         "\n"
                                         "QPushButton:disabled {\n"
                                         "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(125, 125, 125, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "color:black;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.connectbutton.setFlat(False)
        self.connectbutton.setEnabled(False)

        self.SonicRoboBlast2Logo = QLabel(self.centralwidget)
        self.SonicRoboBlast2Logo.setObjectName(u"SonicRoboBlast2Logo")
        self.SonicRoboBlast2Logo.setGeometry(QRect(70, 10, 171, 51))
        self.SonicRoboBlast2Logo.setMinimumSize(QSize(171, 51))
        self.srb2kartlogo = QLabel(self.centralwidget)
        self.srb2kartlogo.setObjectName(u"srb2kartlogo")
        self.srb2kartlogo.setGeometry(QRect(250, 10, 171, 51))
        self.srb2kartlogo.setMinimumSize(QSize(171, 51))
        self.Background = QLabel(self.centralwidget)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 491, 671))

        self.closeInfoButton = QPushButton(self.centralwidget)
        self.closeInfoButton.setObjectName(u"closeInfoButton")
        self.closeInfoButton.setEnabled(False)
        self.closeInfoButton.setVisible(False)
        self.closeInfoButton.setGeometry(QRect(418, 159, 21, 21))
        self.closeInfoButton.setCursor(QCursor(Qt.PointingHandCursor))

        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.closeInfoButton.setFont(font2)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 630, 41, 22))
        self.comboBox.setMinimumSize(QSize(41, 22))
        self.comboBox.setMaximumSize(QSize(41, 22))
        self.refreshLabel = QLabel(self.centralwidget)
        self.refreshLabel.setObjectName(u"refreshLabel")
        self.refreshLabel.setGeometry(QRect(30, 619, 121, 41))
        self.refreshLabel.setMinimumSize(QSize(121, 41))
        self.refreshLabel.setMaximumSize(QSize(121, 41))
        self.refreshLabel.setStyleSheet(u"color: \"white\";\n"
                                        "font: 75 10pt \"Arial\";\n"
                                        "")
        self.refreshLabel.setFrameShape(QFrame.NoFrame)
        self.refreshLabel.setFrameShadow(QFrame.Raised)
        self.refreshLabel2 = QLabel(self.centralwidget)
        self.refreshLabel2.setObjectName(u"refreshLabel2")
        self.refreshLabel2.setGeometry(QRect(200, 620, 51, 41))
        self.refreshLabel2.setMinimumSize(QSize(51, 41))
        self.refreshLabel2.setMaximumSize(QSize(51, 41))
        self.refreshLabel2.setStyleSheet(u"color: \"white\";\n"
                                         "font: 75 10pt \"Arial\";\n"
                                         "")
        self.refreshLabel2.setFrameShape(QFrame.NoFrame)
        self.refreshLabel2.setFrameShadow(QFrame.Raised)
        self.searchbar = QLineEdit(self.centralwidget)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setGeometry(QRect(190, 80, 201, 20))
        self.searchLabel = QLabel(self.centralwidget)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setGeometry(QRect(90, 80, 91, 21))
        self.searchLabel.setStyleSheet(u"color: \"white\";\n"
                                       "font: 75 10pt \"Arial\";\n"
                                       "")
        self.searchLabel.setFrameShape(QFrame.NoFrame)
        self.searchLabel.setFrameShadow(QFrame.Raised)
        self.setCentralWidget(self.centralwidget)

        #  Create a time that controls the refresh period
        self.timer = QTimer(self)

        #  Scrollbar styling
        self.setStyleSheet("""QScrollBar:vertical {
                                        background-color: #727272;
                              }
                              QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
                                        background-color:#171817;
                              }""")

        self.Background.raise_()
        self.SonicRoboBlast2Logo.raise_()
        self.prefToggle.raise_()
        self.servertable.raise_()
        self.player_table.raise_()
        self.prefbutton.raise_()
        self.srb2kartlogo.raise_()
        self.connectbutton.raise_()
        self.closeInfoButton.raise_()
        self.comboBox.raise_()
        self.refreshLabel.raise_()
        self.refreshLabel2.raise_()
        self.searchbar.raise_()
        self.searchLabel.raise_()
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 479, 210))
        self.menubar.setDefaultUp(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(self)

        self.connectbutton.setDefault(False)

        QMetaObject.connectSlotsByName(self)

        self.interactionHandler()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vox's Kart Tracker", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.prefToggle.setText(QCoreApplication.translate("MainWindow", u"Show Preferred Servers Only", None))
        ___qtablewidgetitem = self.player_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Player Name", None));
        #if QT_CONFIG(tooltip)
        self.player_table.setToolTip("")
        #endif // QT_CONFIG(tooltip)
        self.prefbutton.setText(QCoreApplication.translate("MainWindow", u"Add/Remove From \n"
                                                                         "Preferred Servers", None))
        self.connectbutton.setText(QCoreApplication.translate("MainWindow", u"Connect (Must have\n"
                                                                            "Community build)", None))
        self.SonicRoboBlast2Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/VoxKart/TTKBANNR_1_171x51.png\"/></p></body></html>", None))
        self.srb2kartlogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/VoxKart/TTKART_171x51.png\"/></p></body></html>", None))
        self.Background.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/VoxKart/INTERSCR_479x688.png\"/></p></body></html>", None))
        self.closeInfoButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"120", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"300", None))

        self.refreshLabel.setText(QCoreApplication.translate("MainWindow", u"Refresh Table Every", None))
        self.refreshLabel2.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"Search Servers:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

    #  Self-explanatory: Function handles user input.
    def interactionHandler(self):
        self.makeprefs()
        self.getserverinfo(self.servertable)
        self.servertable.clicked.connect(lambda: self.showserverinfo(self.player_table, self.servertable.selectedItems(), self.prefbutton, self.connectbutton))
        self.prefbutton.clicked.connect(lambda: self.manage_pref(self.servertable.selectedItems(), self.searchbar.text(), self.servertable, self.prefToggle.isChecked()))
        self.searchbar.textChanged.connect(lambda: self.searchHelper(self.searchbar.text(), self.servertable, self.prefToggle.isChecked()))
        self.connectbutton.clicked.connect(self.connectToServer)
        self.prefToggle.stateChanged.connect(lambda: self.showPrefHelper(self.servertable, self.prefToggle.isChecked(), self.searchbar.text()))
        self.closeInfoButton.clicked.connect(self.closePlayerInfoTab)
        self.comboBox.currentIndexChanged.connect(self.changeTime)
        self.actionClose.triggered.connect(self.closeApp)

        self.timer.timeout.connect(lambda: self.getserverinfo(self.servertable))
        self.timer.start(self.time_between_ref)

    def changeTime(self):
        selection = int(self.comboBox.currentText())
        #  Convert seconds to ms.
        self.time_between_ref = selection * 1000
        #  Restart the timer.
        self.timer.start(self.time_between_ref)

    def closePlayerInfoTab(self):
        #  "Delete" whatever is in the player_table widget.
        self.player_table.setRowCount(0)
        self.servertable.clearSelection()
        #  Disable/hide selection dependent actions.
        self.closeInfoButton.setEnabled(False)
        self.closeInfoButton.setVisible(False)
        self.prefbutton.setEnabled(False)
        self.connectbutton.setEnabled(False)
        return

    def connectToServer(self):
        if self.servertable.selectedItems():
            server = self.servertable.selectedItems()[0].text()
            serv_ip = self.server_info[server][2]
            defAddress = "srb2kart://ip/" + serv_ip
            webbrowser.open(defAddress)
        else:
            alert = QMessageBox()
            alert.setText("You have not selected a server.")
            alert.exec_()
            return

    def manage_pref(self, name, inp, t, pref_state):
        tempName = name[0].text()
        #  Add server to preferred server list.
        if tempName not in self.pref_servers:
            self.pref_servers.append(tempName)
        #  Remove server from preferences if the server is already in the list.
        else:
            self.pref_servers.remove(tempName)
            #  Update the display
            self.searchHelper(inp, self.servertable, pref_state)
        #  Save server to file.
        with open(self.filepath + '/prefserv.csv', 'w') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(self.pref_servers)

    def showPrefHelper(self, t, pref_state, inp):
        #  This function is useless/redundant. Might delete later.
        self.searchHelper(inp, t, pref_state)

    def showserverinfo(self, info, indx, prefbutton, connectbutton):
        #  Enable buttons dependent on having a server selected.
        self.closeInfoButton.setEnabled(True)
        self.closeInfoButton.setVisible(True)
        self.prefbutton.setEnabled(True)
        self.connectbutton.setEnabled(True)
        connectbutton.setEnabled(True)
        prefbutton.setEnabled(True)
        #  "Delete" whatever is currently in player_table.
        info.setRowCount(0)
        server = indx[0].text()
        # If the amount ofe players in a server can't be found, do nothing and inform the user. Prevents crashing.
        if server not in self.results_sn:
            alert = QMessageBox()
            alert.setText("Server cannot be reached.")
            alert.exec_()
            return
        #  Show the players currently in the server in the player_table widget.
        x = 0
        info.setRowCount(len(self.server_info[server][1]))
        for player in self.server_info[server][1]:
            info.setItem(x, 0, QTableWidgetItem(player.text))
            x += 1

    def searchHelper(self, inp, tab, pref_state):
        displayservs =[]
        if pref_state:
            #  Only go through list of preferred servers if the option is toggled
            for server in self.pref_servers:
                if inp.lower() in server.lower():
                    displayservs.append(server)
        else:
            #  Search entire server list
            for server in self.results_sn:
                if inp.lower() in server.lower():
                    displayservs.append(server)
        #  Populate server table with results
        tab.setRowCount(0)
        tab.setRowCount(len(displayservs))
        incr = 0
        for serv in displayservs:
            tab.setItem(incr, 0, QTableWidgetItem(serv))
            if serv in self.results_sn:
                tab.setItem(incr, 1, QTableWidgetItem(self.server_info[serv][0]))
            else:
                tab.setItem(incr, 1, QTableWidgetItem("N/A"))
            incr += 1

    def makeprefs(self):
        #  If a VoKartTracker dir doesn't exist, make one.
        if not os.path.isdir(self.filepath):
            os.mkdir(self.filepath)
        #  If a prefserv file exists, open it and populate the preference list.
        if os.path.isfile(self.filepath + '/prefserv.csv'):
            with open(self.filepath + '/prefserv.csv', newline='') as prefs:
                readin = csv.reader(prefs)
                for row in readin:
                    for item in row:
                        self.pref_servers.append(item)

    def getserverinfo(self, names_t):
        url = "https://ms.kartkrew.org/"
        page = requests.get(url)
        soupme = BeautifulSoup(page.content, "html.parser")
        results = soupme.find_all("td", class_="copyout")

        #  Empty the GLOBAL server name list to prevent duplicates
        self.results_sn = []

        # Use BeautifulSoup to extract information about all servers on the SRB2Kart Masterlist
        for result in results:
            #  Extract names of the servers
            servname = result.find("h1", class_="servername")
            self.results_sn.append(servname.text)

            #  Extract Amount of players
            info = result.find("div", class_="gameinfo")
            num_playing = re.search("[0-9]+ /\n +[0-9]+", info.text)
            if num_playing:
                num_playing = (' '.join(num_playing.group(0).split()))  # Strip unnecessary whitespace from result
            ip = result.find("span", class_="ip")
            #  Extract player names from each server
            info_p = result.find("div", class_="players")
            listplayers = info_p.find_all("div")
            # Add information to the server_info dictionary which will be used to perform other functions
            self.server_info[self.results_sn[-1]] = [num_playing, listplayers, ip.text]

        x = 0
        names_t.setRowCount(len(self.results_sn))
        #  Fill the Main table
        for servername in self.results_sn:
            names_t.setItem(x, 0, QTableWidgetItem(servername))
            names_t.setItem(x, 1, QTableWidgetItem(self.server_info[servername][0]))
            x += 1
        #  Check if preferences are toggled or if the user has inputte a search query
        if self.prefToggle.isChecked() or self.searchbar.text():
            self.searchHelper(self.searchbar.text(), self.servertable, self.prefToggle.isChecked())

    def closeApp(self):
        sys.exit()


app = QApplication(sys.argv)
app.setStyle('Breeze')
window = MainWindow()

window.show()
app.exec_()
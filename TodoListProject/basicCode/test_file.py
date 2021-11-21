# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_file.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(705, 466)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 30, 256, 190))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(300, 40, 271, 191))
        self.TodayTab = QWidget()
        self.TodayTab.setObjectName(u"TodayTab")
        self.listWidget_2 = QListWidget(self.TodayTab)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(10, 20, 161, 71))
        self.tabWidget.addTab(self.TodayTab, "")
        self.LastTask = QWidget()
        self.LastTask.setObjectName(u"LastTask")
        self.listWidget = QListWidget(self.LastTask)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 10, 151, 81))
        self.tabWidget.addTab(self.LastTask, "")
        self.RandomTask = QWidget()
        self.RandomTask.setObjectName(u"RandomTask")
        self.pushButton = QPushButton(self.RandomTask)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 80, 75, 23))
        self.textBrowser = QTextBrowser(self.RandomTask)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 20, 201, 41))
        self.tabWidget.addTab(self.RandomTask, "")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(130, 310, 141, 18))
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.calendarWidget.raise_()
        self.radioButton.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 705, 22))
        self.menuA_thing = QMenu(self.menubar)
        self.menuA_thing.setObjectName(u"menuA_thing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuA_thing.menuAction())
        self.menuA_thing.addAction(self.actionNew)

        self.retranslateUi(MainWindow)
        self.calendarWidget.clicked.connect(self.listWidget_2.doItemsLayout)
        self.pushButton.clicked.connect(self.textBrowser.clear)
        self.pushButton.clicked.connect(self.textBrowser.reload)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TodayTab), QCoreApplication.translate("MainWindow", u"Today's Task", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LastTask), QCoreApplication.translate("MainWindow", u"Last Task", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load a thing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RandomTask), QCoreApplication.translate("MainWindow", u"Random Task", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.menuA_thing.setTitle(QCoreApplication.translate("MainWindow", u"A thing", None))
    # retranslateUi

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
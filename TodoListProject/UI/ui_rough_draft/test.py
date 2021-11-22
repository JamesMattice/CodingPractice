# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
from PyQt5 import QtCore, QtWidgets
sys.path.append(os.path.abspath('../basicCode'))
import TrackedTask


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 30, 256, 190))
        self.calendarWidget.setObjectName("calendarWidget")
        my_list = self.annoying()
        self.calendarWidget.clicked['QDate'].connect(lambda: self.write_task(my_list))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(300, 40, 271, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.TodayTab = QtWidgets.QWidget()
        self.TodayTab.setObjectName("TodayTab")
        self.today_list = QtWidgets.QListWidget(self.TodayTab)
        self.today_list.setGeometry(QtCore.QRect(10, 20, 161, 71))
        self.today_list.setObjectName("today_list")
        item = QtWidgets.QListWidgetItem()
        self.today_list.addItem(item)
        self.tabWidget.addTab(self.TodayTab, "")
        self.LastTask = QtWidgets.QWidget()
        self.LastTask.setObjectName("LastTask")
        self.last_task_list = QtWidgets.QListWidget(self.LastTask)
        self.last_task_list.setGeometry(QtCore.QRect(10, 10, 151, 81))
        self.last_task_list.setObjectName("last_task_list")
        self.tabWidget.addTab(self.LastTask, "")
        self.RandomTask = QtWidgets.QWidget()
        self.RandomTask.setObjectName("RandomTask")
        self.pushButton = QtWidgets.QPushButton(self.RandomTask)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.RandomTask)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 201, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.RandomTask, "")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(130, 310, 141, 18))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget.raise_()
        self.calendarWidget.raise_()
        self.radioButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 22))
        self.menubar.setObjectName("menubar")
        self.menuA_thing = QtWidgets.QMenu(self.menubar)
        self.menuA_thing.setObjectName("menuA_thing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuA_thing.addAction(self.actionNew)
        self.menubar.addAction(self.menuA_thing.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(self.textBrowser.clear) # type: ignore
        self.pushButton.clicked.connect(self.textBrowser.reload) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.today_list.isSortingEnabled()
        self.today_list.setSortingEnabled(False)
        item = self.today_list.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        self.today_list.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TodayTab), _translate("MainWindow", "Today\'s Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LastTask), _translate("MainWindow", "Last Task"))
        self.pushButton.setText(_translate("MainWindow", "Load a thing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RandomTask), _translate("MainWindow", "Random Task"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.menuA_thing.setTitle(_translate("MainWindow", "A thing"))
        self.actionNew.setText(_translate("MainWindow", "New"))

    def write_task(self, a_list):
        for task in a_list:
            self.today_list.addItem(task.get_task_name())

    def annoying(self):
        sample_list = []
        basic_task = TrackedTask.TrackedTask()
        basic_task.set_task_name("sleep")
        basic_task.set_frequency("daily")
        basic_task.set_max_completions(1)
        basic_task.complete_task()
        sample_list.append(basic_task)
        print(basic_task.get_frequency())
        another_task = TrackedTask.TrackedTask()
        another_task.set_task_name("more sleep")
        another_task.set_status("completed")
        print(another_task.get_status())
        print(another_task.get_frequency())
        print(basic_task.get_number_of_completions())
        sample_list.append(another_task)
        return sample_list

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
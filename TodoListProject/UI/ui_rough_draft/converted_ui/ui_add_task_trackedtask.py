# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_trackedtaskqnUAcO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_task_trackedtask(object):
    def setupUi(self, add_task_trackedtask):
        if not add_task_trackedtask.objectName():
            add_task_trackedtask.setObjectName(u"add_task_trackedtask")
        add_task_trackedtask.resize(408, 187)
        self.gridLayout_2 = QGridLayout(add_task_trackedtask)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_task_trackedtask)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(add_task_trackedtask)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(add_task_trackedtask)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(add_task_trackedtask)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(add_task_trackedtask)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.dateTimeEdit = QDateTimeEdit(add_task_trackedtask)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(add_task_trackedtask)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox = QSpinBox(add_task_trackedtask)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(178, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.pushButton_2 = QPushButton(add_task_trackedtask)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton = QPushButton(add_task_trackedtask)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)


        self.retranslateUi(add_task_trackedtask)

        QMetaObject.connectSlotsByName(add_task_trackedtask)
    # setupUi

    def retranslateUi(self, add_task_trackedtask):
        add_task_trackedtask.setWindowTitle(QCoreApplication.translate("add_task_trackedtask", u"Add TrackedTask", None))
        self.label.setText(QCoreApplication.translate("add_task_trackedtask", u"Task Name:", None))
        self.label_4.setText(QCoreApplication.translate("add_task_trackedtask", u"Frequency:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("add_task_trackedtask", u"Once", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("add_task_trackedtask", u"Hourly", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("add_task_trackedtask", u"Daily", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("add_task_trackedtask", u"Weekly", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("add_task_trackedtask", u"Fortnight", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("add_task_trackedtask", u"Monthly", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("add_task_trackedtask", u"Quarterly", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("add_task_trackedtask", u"Yearly", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("add_task_trackedtask", u"Infinite", None))

        self.label_2.setText(QCoreApplication.translate("add_task_trackedtask", u"Date of Next:", None))
        self.label_3.setText(QCoreApplication.translate("add_task_trackedtask", u"Max Completions:", None))
        self.pushButton_2.setText(QCoreApplication.translate("add_task_trackedtask", u"&Add Task", None))
        self.pushButton.setText(QCoreApplication.translate("add_task_trackedtask", u"&Cancel", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_prioritizedtaskXjIPVs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_task_prioritizedtask(object):
    def setupUi(self, add_task_prioritizedtask):
        if not add_task_prioritizedtask.objectName():
            add_task_prioritizedtask.setObjectName(u"add_task_prioritizedtask")
        add_task_prioritizedtask.resize(380, 236)
        self.gridLayout_3 = QGridLayout(add_task_prioritizedtask)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_task_prioritizedtask)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(add_task_prioritizedtask)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(add_task_prioritizedtask)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(add_task_prioritizedtask)
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
        self.label_2 = QLabel(add_task_prioritizedtask)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.dateTimeEdit = QDateTimeEdit(add_task_prioritizedtask)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(add_task_prioritizedtask)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox = QSpinBox(add_task_prioritizedtask)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(add_task_prioritizedtask)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox = QComboBox(add_task_prioritizedtask)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(178, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.pushButton_2 = QPushButton(add_task_prioritizedtask)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(197, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton = QPushButton(add_task_prioritizedtask)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 2, 2, 1, 1)


        self.retranslateUi(add_task_prioritizedtask)

        QMetaObject.connectSlotsByName(add_task_prioritizedtask)
    # setupUi

    def retranslateUi(self, add_task_prioritizedtask):
        add_task_prioritizedtask.setWindowTitle(QCoreApplication.translate("add_task_prioritizedtask", u"Add PrioritizedTask", None))
        self.label.setText(QCoreApplication.translate("add_task_prioritizedtask", u"Task Name:", None))
        self.label_4.setText(QCoreApplication.translate("add_task_prioritizedtask", u"Frequency:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("add_task_prioritizedtask", u"Once", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("add_task_prioritizedtask", u"Hourly", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("add_task_prioritizedtask", u"Daily", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("add_task_prioritizedtask", u"Weekly", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("add_task_prioritizedtask", u"Fortnight", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("add_task_prioritizedtask", u"Monthly", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("add_task_prioritizedtask", u"Quarterly", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("add_task_prioritizedtask", u"Yearly", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("add_task_prioritizedtask", u"Infinite", None))

        self.label_2.setText(QCoreApplication.translate("add_task_prioritizedtask", u"Date of Next:", None))
        self.label_3.setText(QCoreApplication.translate("add_task_prioritizedtask", u"Max Completions:", None))
        self.label_5.setText(QCoreApplication.translate("add_task_prioritizedtask", u"Priority Level:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("add_task_prioritizedtask", u"Highest", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("add_task_prioritizedtask", u"High", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("add_task_prioritizedtask", u"Medium", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("add_task_prioritizedtask", u"Low", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("add_task_prioritizedtask", u"Lowest", None))

        self.pushButton_2.setText(QCoreApplication.translate("add_task_prioritizedtask", u"&Add Task", None))
        self.pushButton.setText(QCoreApplication.translate("add_task_prioritizedtask", u"&Cancel", None))
    # retranslateUi


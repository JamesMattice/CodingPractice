# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_type_pickaGqxcs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_task_type_pick(object):
    def setupUi(self, add_task_type_pick):
        if not add_task_type_pick.objectName():
            add_task_type_pick.setObjectName(u"add_task_type_pick")
        add_task_type_pick.resize(217, 88)
        self.gridLayout = QGridLayout(add_task_type_pick)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(add_task_type_pick)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(add_task_type_pick)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(add_task_type_pick)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(add_task_type_pick)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(add_task_type_pick)
        self.pushButton_2.clicked.connect(add_task_type_pick.reject)
        self.pushButton.clicked.connect(add_task_type_pick.open)

        QMetaObject.connectSlotsByName(add_task_type_pick)
    # setupUi

    def retranslateUi(self, add_task_type_pick):
        add_task_type_pick.setWindowTitle(QCoreApplication.translate("add_task_type_pick", u"AddTaskType", None))
        self.label_3.setText(QCoreApplication.translate("add_task_type_pick", u"Type of Task:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("add_task_type_pick", u"SuperBasicTask", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("add_task_type_pick", u"TrackedTask", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("add_task_type_pick", u"PrioritizedTask", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("add_task_type_pick", u"TimedTask", None))

        self.pushButton.setText(QCoreApplication.translate("add_task_type_pick", u"&Ok", None))
        self.pushButton_2.setText(QCoreApplication.translate("add_task_type_pick", u"&Cancel", None))
    # retranslateUi


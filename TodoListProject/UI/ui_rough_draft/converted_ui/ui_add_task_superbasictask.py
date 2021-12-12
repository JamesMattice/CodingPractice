# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_superbasictaskUYuyse.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_task_superbasictask(object):
    def setupUi(self, add_task_superbasictask):
        if not add_task_superbasictask.objectName():
            add_task_superbasictask.setObjectName(u"add_task_superbasictask")
        add_task_superbasictask.resize(301, 184)
        self.gridLayout = QGridLayout(add_task_superbasictask)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_task_superbasictask)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(add_task_superbasictask)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(add_task_superbasictask)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(add_task_superbasictask)
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

        self.horizontalLayout_3.addWidget(self.comboBox_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(add_task_superbasictask)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dateTimeEdit = QDateTimeEdit(add_task_superbasictask)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(178, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.pushButton_2 = QPushButton(add_task_superbasictask)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.pushButton = QPushButton(add_task_superbasictask)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)


        self.retranslateUi(add_task_superbasictask)

        QMetaObject.connectSlotsByName(add_task_superbasictask)
    # setupUi

    def retranslateUi(self, add_task_superbasictask):
        add_task_superbasictask.setWindowTitle(QCoreApplication.translate("add_task_superbasictask", u"Add SuperBasicTask", None))
        self.label.setText(QCoreApplication.translate("add_task_superbasictask", u"Task Name:", None))
        self.label_4.setText(QCoreApplication.translate("add_task_superbasictask", u"Frequency:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("add_task_superbasictask", u"Once", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("add_task_superbasictask", u"Hourly", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("add_task_superbasictask", u"Daily", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("add_task_superbasictask", u"Weekly", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("add_task_superbasictask", u"Fortnight", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("add_task_superbasictask", u"Monthly", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("add_task_superbasictask", u"Quarterly", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("add_task_superbasictask", u"Yearly", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("add_task_superbasictask", u"Infinite", None))

        self.label_2.setText(QCoreApplication.translate("add_task_superbasictask", u"Date of Next:", None))
        self.pushButton_2.setText(QCoreApplication.translate("add_task_superbasictask", u"&Add Task", None))
        self.pushButton.setText(QCoreApplication.translate("add_task_superbasictask", u"&Cancel", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_tasklistacEXUM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_new_tasklist(object):
    def setupUi(self, new_tasklist):
        if not new_tasklist.objectName():
            new_tasklist.setObjectName(u"new_tasklist")
        new_tasklist.resize(276, 69)
        new_tasklist.setModal(False)
        self.gridLayout_2 = QGridLayout(new_tasklist)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_2 = QPushButton(new_tasklist)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(new_tasklist)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(new_tasklist)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(new_tasklist)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)


        self.retranslateUi(new_tasklist)
        self.pushButton.clicked.connect(new_tasklist.reject)

        QMetaObject.connectSlotsByName(new_tasklist)
    # setupUi

    def retranslateUi(self, new_tasklist):
        new_tasklist.setWindowTitle(QCoreApplication.translate("new_tasklist", u"New Task", None))
        self.pushButton_2.setText(QCoreApplication.translate("new_tasklist", u"Create List", None))
        self.pushButton.setText(QCoreApplication.translate("new_tasklist", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("new_tasklist", u"Name for Task List:", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Resa_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 311)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 250, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 21))
        self.label.setObjectName("label")
        self.obj_resa_nom = QtWidgets.QComboBox(Dialog)
        self.obj_resa_nom.setGeometry(QtCore.QRect(90, 20, 191, 22))
        self.obj_resa_nom.setEditable(True)
        self.obj_resa_nom.setObjectName("obj_resa_nom")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 60, 191, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 100, 191, 22))
        self.spinBox.setObjectName("spinBox")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 140, 191, 22))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTime(QtCore.QTime(8,0,0))
        self.dateTimeEdit.setDate(QtCore.QDate.currentDate())
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 61, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 180, 191, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(293, 20, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(320, 20, 161, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(320, 50, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(320, 80, 111, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(320, 110, 111, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(320, 140, 111, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(320, 170, 111, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(320, 200, 111, 21))
        self.label_12.setObjectName("label_12")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(410, 50, 161, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(410, 80, 161, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(410, 110, 161, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(410, 140, 161, 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(410, 170, 161, 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(410, 200, 161, 22))
        self.spinBox_7.setObjectName("spinBox_7")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajouter une r??servation"))
        self.label.setText(_translate("Dialog", "Nom : "))
        self.label_2.setText(_translate("Dialog", "Destination : "))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Priay"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Gevrieux"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Chazey"))
        self.label_3.setText(_translate("Dialog", "Nbr pers : "))
        self.label_4.setText(_translate("Dialog", "Date / Heure : "))
        self.label_5.setText(_translate("Dialog", "Bus : "))
        self.label_6.setText(_translate("Dialog", "Nombre de bateau : "))
        self.label_7.setText(_translate("Dialog", "Cano?? : "))
        self.label_8.setText(_translate("Dialog", "Cano?? confort : "))
        self.label_9.setText(_translate("Dialog", "Kayak : "))
        self.label_10.setText(_translate("Dialog", "Canadien : "))
        self.label_11.setText(_translate("Dialog", "Paddle : "))
        self.label_12.setText(_translate("Dialog", "Bigsup : "))

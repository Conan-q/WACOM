# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MG_Rep_Viewer_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(708, 566)
        self.MgCgTnList = QtWidgets.QListWidget(Dialog)
        self.MgCgTnList.setGeometry(QtCore.QRect(358, 313, 331, 211))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MgCgTnList.setFont(font)
        self.MgCgTnList.setObjectName("MgCgTnList")
        self.mgviewResPD = QtWidgets.QPushButton(Dialog)
        self.mgviewResPD.setGeometry(QtCore.QRect(500, 251, 90, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.mgviewResPD.setFont(font)
        self.mgviewResPD.setObjectName("mgviewResPD")
        self.label_MgPdTn = QtWidgets.QLabel(Dialog)
        self.label_MgPdTn.setGeometry(QtCore.QRect(358, 14, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_MgPdTn.setFont(font)
        self.label_MgPdTn.setObjectName("label_MgPdTn")
        self.label_MgCgTn = QtWidgets.QLabel(Dialog)
        self.label_MgCgTn.setGeometry(QtCore.QRect(358, 291, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_MgCgTn.setFont(font)
        self.label_MgCgTn.setObjectName("label_MgCgTn")
        self.mgviewResCG = QtWidgets.QPushButton(Dialog)
        self.mgviewResCG.setGeometry(QtCore.QRect(500, 530, 90, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.mgviewResCG.setFont(font)
        self.mgviewResCG.setObjectName("mgviewResCG")
        self.MgPdTnList = QtWidgets.QListWidget(Dialog)
        self.MgPdTnList.setGeometry(QtCore.QRect(358, 33, 331, 211))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MgPdTnList.setFont(font)
        self.MgPdTnList.setObjectName("MgPdTnList")
        self.MgPdRecTypeList = QtWidgets.QListWidget(Dialog)
        self.MgPdRecTypeList.setGeometry(QtCore.QRect(20, 33, 251, 211))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MgPdRecTypeList.setFont(font)
        self.MgPdRecTypeList.setObjectName("MgPdRecTypeList")
        self.MgPdRecTypeList_2 = QtWidgets.QListWidget(Dialog)
        self.MgPdRecTypeList_2.setGeometry(QtCore.QRect(20, 313, 251, 211))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MgPdRecTypeList_2.setFont(font)
        self.MgPdRecTypeList_2.setObjectName("MgPdRecTypeList_2")
        self.viewMgPdTnBtn = QtWidgets.QPushButton(Dialog)
        self.viewMgPdTnBtn.setGeometry(QtCore.QRect(282, 117, 65, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.viewMgPdTnBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("appRes/right.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewMgPdTnBtn.setIcon(icon)
        self.viewMgPdTnBtn.setObjectName("viewMgPdTnBtn")
        self.viewMgCgTnBtn = QtWidgets.QPushButton(Dialog)
        self.viewMgCgTnBtn.setGeometry(QtCore.QRect(282, 397, 65, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.viewMgCgTnBtn.setFont(font)
        self.viewMgCgTnBtn.setIcon(icon)
        self.viewMgCgTnBtn.setObjectName("viewMgCgTnBtn")
        self.label_MgPdTt = QtWidgets.QLabel(Dialog)
        self.label_MgPdTt.setGeometry(QtCore.QRect(20, 13, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_MgPdTt.setFont(font)
        self.label_MgPdTt.setObjectName("label_MgPdTt")
        self.label_MgCgTt = QtWidgets.QLabel(Dialog)
        self.label_MgCgTt.setGeometry(QtCore.QRect(20, 290, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_MgCgTt.setFont(font)
        self.label_MgCgTt.setObjectName("label_MgCgTt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mgviewResPD.setText(_translate("Dialog", "View Result.."))
        self.label_MgPdTn.setText(_translate("Dialog", "PD Testnames of Selected Record:"))
        self.label_MgCgTn.setText(_translate("Dialog", "CG Testnames of Selected Record:"))
        self.mgviewResCG.setText(_translate("Dialog", "View Result.."))
        self.viewMgPdTnBtn.setText(_translate("Dialog", "View\nTests"))
        self.viewMgCgTnBtn.setText(_translate("Dialog", "View\nTests"))
        self.label_MgPdTt.setText(_translate("Dialog", "PD Test-types of Selected Record:"))
        self.label_MgCgTt.setText(_translate("Dialog", "CG Test-types of Selected Record:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

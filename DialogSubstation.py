# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSubstation.ui'
#
# Created: Mon Mar  2 22:55:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys

class SubstationDialog(QtGui.QWidget):

    def __init__(self, item):
        super(SubstationDialog, self).__init__()
        self.dialog = QtGui.QDialog(self)
        self.item = item
        self.setupUi(self.dialog)
        self.dialog.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 320)
        #Define o tamanho da caixa dialogo 
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 280, 341, 32))
        #Define o tamanho do layout dos botões do dialogo
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 350, 260))
        #Define a localização do layout das propriedades (coordenada x do ponto, coordenada y do ponto, dimensão em x, dimensão em y)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        #definição da propriedade NOME
        self.nomeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.nomeLabel.setObjectName("nomeLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nomeLabel)
        self.nomeLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.nomeLineEdit.setPlaceholderText(str(self.item.substation.nome))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nomeLineEdit)
        self.nomeLineEdit.textChanged.connect(self.en_dis_button)

        #definição da propriedade TENSÃO PRIMÁRIO
        self.tpLabel = QtGui.QLabel(self.formLayoutWidget)
        self.tpLabel.setObjectName("tpLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.tpLabel)
        self.tpLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.tpLineEdit.setObjectName("tpLineEdit")
        self.tpLineEdit.setPlaceholderText(str(self.item.substation.tensao_primario))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.tpLineEdit)

        #definição da propriedade TENSÃO SECUNDÁRIO
        self.tsLabel = QtGui.QLabel(self.formLayoutWidget)
        self.tsLabel.setObjectName("tsLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.tsLabel)
        self.tsLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.tsLineEdit.setObjectName("tsLineEdit")
        self.tsLineEdit.setPlaceholderText(str(self.item.substation.tensao_secundario))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.tsLineEdit)

        #definição da propriedade POTENCIA APARENTE
        self.potLabel = QtGui.QLabel(self.formLayoutWidget)
        self.potLabel.setObjectName("potLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.potLabel)
        self.potLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.potLineEdit.setObjectName("potLineEdit")
        self.potLineEdit.setPlaceholderText(str(self.item.substation.potencia))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.potLineEdit)

        #definição da propriedade IMPEDANCIA POSITIVA
        self.zPLabel = QtGui.QLabel(self.formLayoutWidget)
        self.zPLabel.setObjectName("zPLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.zPLabel)
        

        #definição da propriedade resistencia
        self.resistenciaposLabel = QtGui.QLabel(self.formLayoutWidget)
        self.resistenciaposLabel.setObjectName("resistenciaposLabel")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.resistenciaposLabel)
        self.resistenciaposLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.resistenciaposLineEdit.setObjectName("resistenciaposLineEdit")
        self.resistenciaposLineEdit.setPlaceholderText(str(self.item.substation.impedancia_pos.real))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.resistenciaposLineEdit)

        #definição da propriedade reatancia
        self.reaposLabel = QtGui.QLabel(self.formLayoutWidget)
        self.reaposLabel.setObjectName("reaposLabel")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.reaposLabel)
        self.reaposLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.reaposLineEdit.setObjectName("reaposLineEdit")
        self.reaposLineEdit.setPlaceholderText(str(self.item.substation.impedancia_pos.imag))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.reaposLineEdit)

        #definição da propriedade IMPEDANCIA ZERO
        self.zZLabel = QtGui.QLabel(self.formLayoutWidget)
        self.zZLabel.setObjectName("zZLabel")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.zZLabel)
        # self.zZLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        # self.zZLineEdit.setObjectName("zZLineEdit")
        # self.zZLineEdit.setPlaceholderText(str(self.item.substation.impedancia_zero))
        # self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.zZLineEdit)

        #definição da propriedade resistencia
        self.resistenciazeroLabel = QtGui.QLabel(self.formLayoutWidget)
        self.resistenciazeroLabel.setObjectName("resistenciazeroLabel")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.resistenciazeroLabel)
        self.resistenciazeroLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.resistenciazeroLineEdit.setObjectName("resistenciazeroLineEdit")
        self.resistenciazeroLineEdit.setPlaceholderText(str(self.item.substation.impedancia_zero.real))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.resistenciazeroLineEdit)

        #definição da propriedade reatancia
        self.reazeroLabel = QtGui.QLabel(self.formLayoutWidget)
        self.reazeroLabel.setObjectName("reazeroLabel")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.reazeroLabel)
        self.reazeroLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.reazeroLineEdit.setObjectName("reazeroLineEdit")
        self.reazeroLineEdit.setPlaceholderText(str(self.item.substation.impedancia_zero.imag))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.reazeroLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        if self.nomeLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)
        if self.nomeLineEdit.placeholderText() != "":
            self.buttonBox.buttons()[0].setEnabled(True)

    def en_dis_button(self):

        if self.nomeLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)

    def retranslateUi(self, Dialog):
        #Tradução dos nomes dados aos objetos para os nomes gráficos do programa
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Subestacao - Propriedades", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeLabel.setText(QtGui.QApplication.translate("Dialog", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.tpLabel.setText(QtGui.QApplication.translate("Dialog", "Tensao Primario:", None, QtGui.QApplication.UnicodeUTF8))
        self.tsLabel.setText(QtGui.QApplication.translate("Dialog", "Tensao Secundario:", None, QtGui.QApplication.UnicodeUTF8))
        self.potLabel.setText(QtGui.QApplication.translate("Dialog", "Potencia Aparente:", None, QtGui.QApplication.UnicodeUTF8))
        self.zPLabel.setText(QtGui.QApplication.translate("Dialog", "Impedancia Positiva", None, QtGui.QApplication.UnicodeUTF8))
        self.zZLabel.setText(QtGui.QApplication.translate("Dialog", "Impedancia Zero", None, QtGui.QApplication.UnicodeUTF8))
        self.resistenciaposLabel.setText(QtGui.QApplication.translate("Dialog", "Resistencia", None, QtGui.QApplication.UnicodeUTF8))
        self.reaposLabel.setText(QtGui.QApplication.translate("Dialog", "Reatancia", None, QtGui.QApplication.UnicodeUTF8))
        self.resistenciazeroLabel.setText(QtGui.QApplication.translate("Dialog", "Resistencia", None, QtGui.QApplication.UnicodeUTF8))
        self.reazeroLabel.setText(QtGui.QApplication.translate("Dialog", "Reatancia", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    SubstationDialog = SubstationDialog()
    sys.exit(app.exec_())

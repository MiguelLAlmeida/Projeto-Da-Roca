# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmDepto.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QToolBar, QWidget)
import recursos_rc

class Ui_DRprods(object):
    def setupUi(self, DRprods):
        if not DRprods.objectName():
            DRprods.setObjectName(u"DRprods")
        DRprods.resize(349, 292)
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        DRprods.setFont(font)
        self.action_Salvar = QAction(DRprods)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon = QIcon()
        icon.addFile(u":/depto/Save.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon)
        font1 = QFont()
        font1.setKerning(False)
        self.action_Salvar.setFont(font1)
        self.action_Sair = QAction(DRprods)
        self.action_Sair.setObjectName(u"action_Sair")
        icon1 = QIcon()
        icon1.addFile(u":/depto/CLOSE1.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Sair.setIcon(icon1)
        self.centralwidget = QWidget(DRprods)
        self.centralwidget.setObjectName(u"centralwidget")
        self.abas = QTabWidget(self.centralwidget)
        self.abas.setObjectName(u"abas")
        self.abas.setGeometry(QRect(10, 0, 321, 211))
        font2 = QFont()
        font2.setPointSize(11)
        self.abas.setFont(font2)
        self.tabCadastro = QWidget()
        self.tabCadastro.setObjectName(u"tabCadastro")
        self.gridLayout = QGridLayout(self.tabCadastro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.descProd = QLineEdit(self.tabCadastro)
        self.descProd.setObjectName(u"descProd")
        self.descProd.setMaxLength(20)

        self.gridLayout.addWidget(self.descProd, 4, 2, 1, 1)

        self.label = QLabel(self.tabCadastro)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.valorProd = QDoubleSpinBox(self.tabCadastro)
        self.valorProd.setObjectName(u"valorProd")

        self.gridLayout.addWidget(self.valorProd, 3, 2, 1, 1)

        self.nomeProd = QLineEdit(self.tabCadastro)
        self.nomeProd.setObjectName(u"nomeProd")
        self.nomeProd.setMaxLength(20)

        self.gridLayout.addWidget(self.nomeProd, 1, 2, 1, 1)

        self.label_2 = QLabel(self.tabCadastro)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.tabCadastro)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.tabCadastro)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.imgProd = QLineEdit(self.tabCadastro)
        self.imgProd.setObjectName(u"imgProd")
        self.imgProd.setMaxLength(11)

        self.gridLayout.addWidget(self.imgProd, 2, 2, 1, 1)

        self.label_5 = QLabel(self.tabCadastro)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.categProd = QSpinBox(self.tabCadastro)
        self.categProd.setObjectName(u"categProd")
        self.categProd.setMinimum(1)

        self.gridLayout.addWidget(self.categProd, 0, 2, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/depto/COPY.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.abas.addTab(self.tabCadastro, icon2, "")
        DRprods.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DRprods)
        self.statusbar.setObjectName(u"statusbar")
        DRprods.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(DRprods)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        DRprods.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Salvar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Sair)

        self.retranslateUi(DRprods)

        self.abas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DRprods)
    # setupUi

    def retranslateUi(self, DRprods):
        DRprods.setWindowTitle(QCoreApplication.translate("DRprods", u"Cadastro de Produtos", None))
        self.action_Salvar.setText(QCoreApplication.translate("DRprods", u"&Salvar", None))
        self.action_Salvar.setIconText(QCoreApplication.translate("DRprods", u"Adicionar", None))
#if QT_CONFIG(tooltip)
        self.action_Salvar.setToolTip(QCoreApplication.translate("DRprods", u"Grava o Produto atual no banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.action_Sair.setText(QCoreApplication.translate("DRprods", u"Sai&r", None))
#if QT_CONFIG(tooltip)
        self.action_Sair.setToolTip(QCoreApplication.translate("DRprods", u"Fecha a conex\u00e3o, salva dados e fecha o formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DRprods", u"Categoria:", None))
        self.label_2.setText(QCoreApplication.translate("DRprods", u"Nome:", None))
        self.label_4.setText(QCoreApplication.translate("DRprods", u"Valor:", None))
        self.label_3.setText(QCoreApplication.translate("DRprods", u"Imagem:", None))
        self.label_5.setText(QCoreApplication.translate("DRprods", u"Descri\u00e7\u00e3o:", None))
        self.abas.setTabText(self.abas.indexOf(self.tabCadastro), QCoreApplication.translate("DRprods", u"Cadastro de Produtos no Da Ro\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.abas.setTabToolTip(self.abas.indexOf(self.tabCadastro), QCoreApplication.translate("DRprods", u"Cadastro de Produtos no SQL do Da Ro\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("DRprods", u"toolBar", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'biblioKUeNdx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 855)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.actionSauvegarder_sous = QAction(MainWindow)
        self.actionSauvegarder_sous.setObjectName(u"actionSauvegarder_sous")
        self.actionOuvrir_2 = QAction(MainWindow)
        self.actionOuvrir_2.setObjectName(u"actionOuvrir_2")
        self.actionSauvegarder = QAction(MainWindow)
        self.actionSauvegarder.setObjectName(u"actionSauvegarder")
        self.actionSauvegarder_sous_2 = QAction(MainWindow)
        self.actionSauvegarder_sous_2.setObjectName(u"actionSauvegarder_sous_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.transactions = QWidget()
        self.transactions.setObjectName(u"transactions")
        self.gridLayout_8 = QGridLayout(self.transactions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.transactions)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.transactions)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.transactions)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.label_5 = QLabel(self.transactions)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 5, 0, 1, 1)

        self.dateEdit = QDateEdit(self.transactions)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_7.addWidget(self.dateEdit, 6, 3, 1, 1)

        self.line_2 = QFrame(self.transactions)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 3, 0, 1, 4)

        self.comboBox_3 = QComboBox(self.transactions)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_7.addWidget(self.comboBox_3, 6, 2, 1, 1)

        self.label_6 = QLabel(self.transactions)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 5, 1, 1, 1)

        self.tableView_2 = QTableView(self.transactions)
        self.tableView_2.setObjectName(u"tableView_2")

        self.gridLayout_7.addWidget(self.tableView_2, 2, 0, 1, 4)

        self.comboBox_2 = QComboBox(self.transactions)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_7.addWidget(self.comboBox_2, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.transactions)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_7.addWidget(self.comboBox, 1, 0, 1, 2)

        self.label_12 = QLabel(self.transactions)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 5, 2, 1, 1)

        self.label_13 = QLabel(self.transactions)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 5, 3, 1, 1)

        self.pushButton = QPushButton(self.transactions)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_7.addWidget(self.pushButton, 7, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.transactions)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_7.addWidget(self.pushButton_2, 7, 2, 1, 2)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.transactions, "")
        self.membres = QWidget()
        self.membres.setObjectName(u"membres")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.membres.sizePolicy().hasHeightForWidth())
        self.membres.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.membres)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelMembres2 = QLabel(self.membres)
        self.labelMembres2.setObjectName(u"labelMembres2")

        self.gridLayout_2.addWidget(self.labelMembres2, 4, 0, 1, 1)

        self.tableMembres = QTableView(self.membres)
        self.tableMembres.setObjectName(u"tableMembres")
        sizePolicy1.setHeightForWidth(self.tableMembres.sizePolicy().hasHeightForWidth())
        self.tableMembres.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.tableMembres, 1, 0, 1, 4)

        self.inputMembresContact = QLineEdit(self.membres)
        self.inputMembresContact.setObjectName(u"inputMembresContact")
        sizePolicy.setHeightForWidth(self.inputMembresContact.sizePolicy().hasHeightForWidth())
        self.inputMembresContact.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.inputMembresContact, 5, 2, 1, 1)

        self.line = QFrame(self.membres)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 4)

        self.inputMembresNom = QLineEdit(self.membres)
        self.inputMembresNom.setObjectName(u"inputMembresNom")
        sizePolicy.setHeightForWidth(self.inputMembresNom.sizePolicy().hasHeightForWidth())
        self.inputMembresNom.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.inputMembresNom, 5, 0, 1, 1)

        self.label = QLabel(self.membres)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.btAnnulerMembres = QPushButton(self.membres)
        self.btAnnulerMembres.setObjectName(u"btAnnulerMembres")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btAnnulerMembres.sizePolicy().hasHeightForWidth())
        self.btAnnulerMembres.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.btAnnulerMembres, 6, 0, 1, 2)

        self.inputMembresDate = QDateEdit(self.membres)
        self.inputMembresDate.setObjectName(u"inputMembresDate")

        self.gridLayout_2.addWidget(self.inputMembresDate, 5, 3, 1, 1)

        self.labelMembres3 = QLabel(self.membres)
        self.labelMembres3.setObjectName(u"labelMembres3")

        self.gridLayout_2.addWidget(self.labelMembres3, 4, 1, 1, 1)

        self.labelMembres4 = QLabel(self.membres)
        self.labelMembres4.setObjectName(u"labelMembres4")

        self.gridLayout_2.addWidget(self.labelMembres4, 4, 2, 1, 1)

        self.inputMembresAdhesion = QLineEdit(self.membres)
        self.inputMembresAdhesion.setObjectName(u"inputMembresAdhesion")
        sizePolicy.setHeightForWidth(self.inputMembresAdhesion.sizePolicy().hasHeightForWidth())
        self.inputMembresAdhesion.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.inputMembresAdhesion, 5, 1, 1, 1)

        self.labelMembres5 = QLabel(self.membres)
        self.labelMembres5.setObjectName(u"labelMembres5")

        self.gridLayout_2.addWidget(self.labelMembres5, 4, 3, 1, 1)

        self.btAjouterMembres = QPushButton(self.membres)
        self.btAjouterMembres.setObjectName(u"btAjouterMembres")

        self.gridLayout_2.addWidget(self.btAjouterMembres, 6, 2, 1, 2)

        self.labelMembres1 = QLabel(self.membres)
        self.labelMembres1.setObjectName(u"labelMembres1")

        self.gridLayout_2.addWidget(self.labelMembres1, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.membres, "")
        self.livres = QWidget()
        self.livres.setObjectName(u"livres")
        self.gridLayout_6 = QGridLayout(self.livres)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.livres)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_2 = QLabel(self.livres)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.livres)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_10 = QLabel(self.livres)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 6, 1, 1, 1)

        self.label_11 = QLabel(self.livres)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 6, 2, 1, 1)

        self.tableView = QTableView(self.livres)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_5.addWidget(self.tableView, 1, 0, 1, 3)

        self.line_3 = QFrame(self.livres)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 4, 0, 1, 3)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.livres, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addAction(self.actionOuvrir_2)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuFichier.addAction(self.actionSauvegarder_sous_2)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.actionSauvegarder_sous.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder sous", None))
        self.actionOuvrir_2.setText(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
        self.actionSauvegarder.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.actionSauvegarder_sous_2.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder sous", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ajout d'une transaction", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Choisir une personne", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Membres", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transactions), QCoreApplication.translate("MainWindow", u"Page", None))
        self.labelMembres2.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nouvelle personne", None))
        self.btAnnulerMembres.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.labelMembres3.setText(QCoreApplication.translate("MainWindow", u"Adhesion", None))
        self.labelMembres4.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.labelMembres5.setText(QCoreApplication.translate("MainWindow", u"Date (DD/MM/AAAA)", None))
        self.btAjouterMembres.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.labelMembres1.setText(QCoreApplication.translate("MainWindow", u"Liste des membres", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.membres), QCoreApplication.translate("MainWindow", u"Membres", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ajout d'un livre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Liste des livres", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.livres), QCoreApplication.translate("MainWindow", u"Livres", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
    # retranslateUi


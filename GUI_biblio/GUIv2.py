import sys
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMenuBar, QFrame, QCheckBox, QVBoxLayout, QApplication, QMessageBox, QLabel, QMainWindow, QGridLayout, QFileDialog, QWidget, QPushButton, QComboBox, QTableView, QLineEdit, QTabWidget
from PyQt5 import QtGui
import GUI_biblio as bib
import pandas as pd
import sqlite3


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DB Port-Mort")
        self.resize(900, 600)
        
        # Central widget and layout
        central_widget = QWidget()
        layout_main = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # DB connection
        self.con = sqlite3.connect("biblio.db")
        self.cur = self.con.cursor()

        # UI element definition
        self.file_path_label = QLabel()
        self.names_combo = QComboBox()
        self.df_membres = pd.read_sql("SELECT * FROM Members", self.con)  # data frame from the excel file, that has been processed in self.open()
        self.df_livres = pd.read_sql("SELECT * FROM Books", self.con)

        self.table_membres = QTableView()
        self.table_livres = QTableView()
        self.table_adhesion = QTableView()
        self.table_missing = QTableView()

         # Affichages des df initiaux
        self.model_membres = pandasModel(self.df_membres)
        self.table_membres.setModel(self.model_membres)
        print(self.model_membres)

        # Menu bar
        menu_bar = self.menuBar()
        fichier = menu_bar.addMenu("Fichier")
        fichier.addAction("Ouvrir", self.open)
        fichier.addAction("Sauvegarde", self.save_file)

        # Definition des tabs
        self.tabs = QTabWidget()
        self.tab_membres = QWidget()
        self.tab_livres = QWidget()
        self.tab_adhesion = QWidget()

        self.tabs.addTab(self.tab_membres, "Membres")
        self.tabs.addTab(self.tab_livres, "Livres")
        self.tabs.addTab(self.tab_adhesion, "Adhésions")

        # Label pour le tab_modif
        

        # Definition des différents layouts
        self.tab_membres.layout = QGridLayout()
        self.tab_livres.layout = QGridLayout()
        self.tab_adhesion.layout = QGridLayout()

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setFrameShadow(QFrame.Sunken)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setFrameShadow(QFrame.Sunken)
        separator3 = QFrame()
        separator3.setFrameShape(QFrame.HLine)
        separator3.setFrameShadow(QFrame.Sunken)

        # layout_main.addWidget(self.table)
        layout_main.addWidget(self.tabs)

        # Layout des tabs
        self.tab_membres.layout.addWidget(self.table_membres, 0, 0, 1, 1)
        self.tab_livres.layout.addWidget(self.table_livres, 0, 0, 1, 1)
        self.tab_adhesion.layout.addWidget(self.table_adhesion, 0, 0, 1, 1)

        layout_main.addWidget(separator3)
        layout_main.addWidget(self.file_path_label)

        # Ajout des layouts aux widgets



        # Définition des variables de la classe
        self.excel_filename = None # Will hold the image address location
        self.con = None # Stores the connexion to the database

    def box_single(self):
        name = self.names_combo.currentText()
        if self.check_single.isChecked():
            missing = self.df[name][self.df[name]["RENDU LE"].isnull()]
            print(missing)
            self.display_missing(missing)
        return
    
    def box_all(self):
        if self.check_all.isChecked():
            missing = []
            for name in self.df.keys():
                missing.append(self.df[name][self.df[name]["RENDU LE"].isnull()])
            self.display_missing(missing)
            print(missing)
        return
    
    def open(self):
        return

    def save_file(self):
        return
    
    def current_text_combo(self, _):
        ctext = self.names_combo.currentText()
        self.display_df(ctext)

    def display_df(self, name):
        model = pandasModel(self.df[name])
        self.table.setModel(model)

    def display_missing(self, arendre):
        model = pandasModel(pd.DataFrame(arendre))
        self.table_missing.setModel(model)

    def ajout_ligne(self):
        ctext = self.names_combo.currentText()
        dict = {'CODE':[int(self.code_input.text())],
                'AUTEUR':[self.auteur_input.text()],
                'PRENOM':[self.prenom_input.text()],
                'TITRE  DU LIVRE':[self.titre_input.text()],
                'EMPRUNTE LE':[self.emprunt_input.text()],
                'RENDU LE':[self.rendu_input.text()]}
        df2 = pd.DataFrame(dict)
        self.df[ctext] = pd.concat([self.df[ctext], df2], ignore_index=True)

        # Nouvel affichage pour prendre en compte le changement
        self.display_df(ctext)
        return
    
    def supp_ligne(self):
        ctext = self.names_combo.currentText()
        row = self.code_supp_input.text()
        self.df[ctext].drop(labels=int(row), inplace=True)

        self.display_df(ctext)
        return

    def connect_to_db(self, MainWindow):
        # Create the connection
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("GUI_biblio/DATA/database/test_database")
        
        # Try to open the connection and handle possible errors
        if not self.con.open():
            QMessageBox.critical(
                None,
                "App Name - Error!",
                "Database Error: %s" % self.con.lastError().databaseText(),
            )
            sys.exit(1)


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])

        return None

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
    








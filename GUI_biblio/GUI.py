import sys
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMenuBar, QFrame, QCheckBox, QVBoxLayout, QApplication, QMessageBox, QLabel, QMainWindow, QGridLayout, QFileDialog, QWidget, QPushButton, QComboBox, QTableView, QLineEdit, QTabWidget
from PyQt5 import QtGui
import GUI_biblio as bib
import pandas as pd
import pandas_xlwt


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DB Port-Mort")
        self.resize(900, 600)
        
        # Central widget and layout
        central_widget = QWidget()
        layout_main = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # UI element definition
        self.file_path_label = QLabel()
        self.names_combo = QComboBox()
        self.df = None  # data frame from the excel file, that has been processed in self.open()
        self.table = QTableView()
        self.table_missing = QTableView()
        self.ajout_button = QPushButton("ajouter")
        self.ajout_button.clicked.connect(self.ajout_ligne)
        self.supp_button = QPushButton("supprimer")
        self.supp_button.clicked.connect(self.supp_ligne)
        self.output_file_button = QPushButton("...")
        self.output_file_button.clicked.connect(self.save_file)
        self.check_single = QCheckBox("Single")
        self.check_single.toggled.connect(self.box_single)
        self.check_all = QCheckBox("All")
        self.check_all.toggled.connect(self.box_all)

        # Menu bar
        menu_bar = self.menuBar()
        fichier = menu_bar.addMenu("Fichier")
        fichier.addAction("Ouvrir", self.open)
        fichier.addAction("Sauvegarde", self.save_file)

        # Definition des tabs
        self.tabs = QTabWidget()
        self.tab_modif = QWidget()
        self.tab_arendre = QWidget()
        self.tab_save = QWidget()

        self.tabs.addTab(self.tab_modif, "Modification")
        self.tabs.addTab(self.tab_arendre, "À rendre")
        self.tabs.addTab(self.tab_save, "Sauvegarde")

        # Label pour le tab_modif
        self.ajout_text = QLabel("AJOUT D'UNE ENTRÉE")
        self.ajout_text.setAlignment(Qt.AlignCenter)
        self.supp_text = QLabel("SUPPRESION D'UNE ENTRÉE")
        self.supp_text.setAlignment(Qt.AlignCenter)
        self.code_text1 = QLabel("Code")
        self.code_text2 = QLabel("Index")
        self.auteur_text = QLabel("Auteur")
        self.prenom_text = QLabel("Prenom")
        self.titre_text = QLabel("Titre du livre")
        self.emprunt_text = QLabel("Emprunté le")
        self.rendu_text = QLabel("Rendu le")

        self.text_save = QLabel("SAUVEGARDE")
        self.text_save.setAlignment(Qt.AlignCenter)

        self.output_file_input = QLineEdit(self)
        self.code_input = QLineEdit(self)
        self.code_supp_input = QLineEdit(self)
        self.auteur_input = QLineEdit(self)
        self.prenom_input = QLineEdit(self)
        self.titre_input = QLineEdit(self)
        self.emprunt_input = QLineEdit(self)
        self.rendu_input = QLineEdit(self)

        # Definition des différents layouts
        self.tab_modif.layout = QGridLayout()
        self.tab_arendre.layout = QGridLayout()
        self.tab_save.layout = QGridLayout()

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setFrameShadow(QFrame.Sunken)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setFrameShadow(QFrame.Sunken)
        separator3 = QFrame()
        separator3.setFrameShape(QFrame.HLine)
        separator3.setFrameShadow(QFrame.Sunken)

        layout_main.addWidget(self.names_combo)
        layout_main.addWidget(self.table)
        layout_main.addWidget(self.tabs)

        # Layout de tab_modif
        self.tab_modif.layout.addWidget(self.ajout_text, 0, 0, 1, 7)
        self.tab_modif.layout.addWidget(self.code_text1, 1, 0, 1, 1)
        self.tab_modif.layout.addWidget(self.auteur_text, 1, 1)
        self.tab_modif.layout.addWidget(self.prenom_text, 1, 2)
        self.tab_modif.layout.addWidget(self.titre_text, 1, 3)
        self.tab_modif.layout.addWidget(self.emprunt_text, 1, 4)
        self.tab_modif.layout.addWidget(self.rendu_text, 1, 5)
        self.tab_modif.layout.addWidget(separator2, 3, 0, 1, 8)
        self.tab_modif.layout.addWidget(self.supp_text, 4, 0, 1, 7)
        self.tab_modif.layout.addWidget(self.code_text2, 5, 4, 1, 1)
        self.code_text2.setAlignment(Qt.AlignRight)

        self.tab_modif.layout.addWidget(self.code_input, 2, 0, 1, 1)
        self.tab_modif.layout.addWidget(self.auteur_input, 2, 1)
        self.tab_modif.layout.addWidget(self.prenom_input, 2, 2)
        self.tab_modif.layout.addWidget(self.titre_input, 2, 3)
        self.tab_modif.layout.addWidget(self.emprunt_input, 2, 4)
        self.tab_modif.layout.addWidget(self.rendu_input, 2, 5)
        self.tab_modif.layout.addWidget(self.ajout_button, 2, 6)
        self.tab_modif.layout.addWidget(self.code_supp_input, 5, 5, 1, 1)
        self.tab_modif.layout.addWidget(self.supp_button, 5, 6, 1, 1)

        # Layout de tab_save
        self.tab_save.layout.addWidget(self.text_save, 0, 0, 1, 2)
        self.tab_save.layout.addWidget(self.output_file_input, 1, 0)
        self.tab_save.layout.addWidget(self.output_file_button, 1, 1)

        # Layout de tab_arendre
        self.tab_arendre.layout.addWidget(self.check_single, 0, 0)
        self.tab_arendre.layout.addWidget(self.check_all, 0, 1)
        self.tab_arendre.layout.addWidget(self.table_missing, 1, 0, 1, 2)

        layout_main.addWidget(separator3)
        layout_main.addWidget(self.file_path_label)

        # Ajout des layouts aux widgets
        self.tab_modif.setLayout(self.tab_modif.layout)
        self.tab_arendre.setLayout(self.tab_arendre.layout)
        self.tab_save.setLayout(self.tab_save.layout)



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
        fileName, _ = QFileDialog.getOpenFileName(self, "OpenFile")
        print("Filename =", fileName)
        if not fileName:
            return
        try:
            self.excel_filename = fileName
            print("Filename = ", self.excel_filename)
            self.file_path_label.setText(self.excel_filename)
            
            df = bib.load_excel(self.excel_filename, sheets_to_exclude=["mode d'emploi",
                                                                        "adherents 23-24",
                                                                        "Modèle",
                                                                        "adherents mars24",
                                                                        "adherents AGjuin23",
                                                                        "adherents recap22-23",
                                                                        "Feuil2"])
            df = bib.df_filtering(df)
            self.df = df
            
            # Creation de la combo box pour chaque personne dans le df
            self.names_combo.addItems(self.df.keys())
            self.names_combo.activated.connect(self.current_text_combo)
        except Exception as e:
            QMessageBox.warning(self, 'Error', 
            f'The following error occurred:\n{type(e)}: {e}')
        return

    def save_file(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "File name", "", "Excel Files (*.xlsx)")
        if not fileName:
            return
        try:
            writer = pd.ExcelWriter(fileName, mode='a', if_sheet_exists='overlay')
            for name in self.df.keys():
                self.df[name].to_excel(excel_writer=writer, sheet_name=name, startrow=500)

            self.output_file_input.insert(fileName)
            writer.close()
        except Exception as e:
            QMessageBox.warning(self, 'Error', 
            f'The following error occurred:\n{type(e)}: {e}')
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
    








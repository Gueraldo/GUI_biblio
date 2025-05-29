from PySide6 import QtWidgets, QtCore
from ui_biblio import Ui_MainWindow
import sqlite3
import pandas as pd
Qt = QtCore.Qt

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None



class MainWindoow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Linking the buttons
        self.ui.actionOuvrir_2.triggered.connect(self.open)

    def open(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, caption="Ouvrir un fichier", filter="*.db")
        if not fileName:
            return
        else:
            self.db_filename = fileName
            self.con = sqlite3.connect(fileName[0])
            self.cur = self.con.cursor()

            self.loadMembers()
            self.loadLivres()
            self.loadTransactions()
        return
    

    def loadMembers(self):
        self.df_membres = pd.read_sql("SELECT * FROM Members", con=self.con)
        self.modelMembres = PandasModel(self.df_membres)

        self.ui.tableMembres.setModel(self.modelMembres)

        return
    
    def loadLivres(self):
        return
    
    def loadTransactions(self):
        self.ui.comboBox.addItems(self.df_membres["name"])
        return
    
    def displayTransactions(self):
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindoow()
    window.show()
    app.exec()
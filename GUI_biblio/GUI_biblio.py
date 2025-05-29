import pandas as pd
import numpy as np
import sqlite3

def load_excel(filepath, sheets_to_exclude, skip_rows=6):
    xls = pd.ExcelFile(filepath)
    all_sheets_names = xls.sheet_names
    sheets_to_import = [sheet for sheet in all_sheets_names if sheet not in sheets_to_exclude]

    df = pd.read_excel(filepath,
                    sheet_name=sheets_to_import, # Use sheet_name=None for all sheets
                    header=0,
                    skiprows=lambda x: x in [i for i in range(skip_rows)],
                    ) 
    
    return df


def df_filtering(df):
    for key in df.keys():
        dfi = df[key]
        check_na = dfi.isna()
        rows_to_keep = np.array(check_na).all(axis=1)

        dfi = dfi[~pd.Series(rows_to_keep)].reset_index(drop=True)
        
        df[key] = dfi

    return df


def create_database():
    conn = sqlite3.connect("test_database")
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS products
        ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
        """
    )

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS prices
        ([product_id] INTEGER, [price] INTEGER)
        """
    )

    conn.commit()

    return


def main():
    sheet_path = "GUI_biblio/DATA/ADHERENTS_EMPRUNTS_v9_240713.xls"

    unwanted_sheets = ["mode d'emploi",
                  "adherents 23-24",
                  "Modèle",
                  "adherents mars24",
                  "adherents AGjuin23",
                  "asherents recap22-23",
                  "Feuil2"]
    
    df_bib = load_excel(sheet_path, sheets_to_exclude=unwanted_sheets)
    df_bib = df_filtering(df_bib)

    print(df_bib["Noah"])

if __name__ == "__main__":
    main()

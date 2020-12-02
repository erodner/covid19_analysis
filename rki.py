import pandas as pd
import xlrd

def get_positive_cases(state="Gesamt"):

  df = pd.read_excel("Fallzahlen_Kum_Tab.xlsx", sheet_name="BL_7-Tage-Fallzahlen", skiprows=2, index_col=0)

  df = df.T

  dates = df.index.tolist()
  cases = df[state].tolist()

  return dates, cases
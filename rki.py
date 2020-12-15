import pandas as pd
import xlrd


def load_data():
  df = pd.read_excel("Fallzahlen_Kum_Tab.xlsx", sheet_name="BL_7-Tage-Fallzahlen", skiprows=2, index_col=0)
  df = df.T

  return df


def get_cases_last7days(state="Gesamt"):
  df = load_data()
  dates = df.index.tolist()
  cases = df[state].tolist()

  return dates, cases
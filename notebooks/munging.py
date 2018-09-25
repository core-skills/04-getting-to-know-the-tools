import pandas as pd

def load_data(data_file, sht_name):
    df = pd.read_excel(io=data_file, sheet_name = sht_name)

    return df

import pandas as pd

def read_thermometer_file(file_path: str):
    data = pd.read_csv(f"{file_path}", encoding="gbk", skiprows=31, names=["Date", "Time", "Temp", "drop_a","drop_b","drop_c","drop_d"]).dropna(how='any', axis=1, inplace=False)
    
    return data

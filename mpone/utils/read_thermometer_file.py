import pandas as pd

def read_thermometer_file(file):
    data = pd.read_csv(file, encoding="gbk", skiprows=31, names=["Date", "Time", "Temp", "drop_a","drop_b","drop_c","drop_d"]).dropna(how='any', axis=1, inplace=False).drop("Date", axis=1)
    
    return data

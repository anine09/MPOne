import pandas as pd

def read_Illuminance_file(file):
    data = pd.read_excel(file)
    time_data =pd.read_excel(file, sheet_name="Metadata Time")

    start_time = time_data.loc[time_data['event'] == 'START', 'system time text'].item()[:-10]

    data['Time (s)'] = pd.to_datetime(start_time) + pd.to_timedelta(data['Time (s)'], unit='s')
    data['Time (s)'] = data['Time (s)'].dt.strftime('%H:%M:%S')

    data_mean = data.groupby("Time (s)")["Illuminance (lx)"].mean().reset_index()
    data_result = data_mean[data_mean["Illuminance (lx)"].notnull()].drop_duplicates()
    data_result = data_result.rename(columns={'Time (s)': 'Time'})
    data_result = data_result.rename(columns={'Illuminance (lx)': 'Illuminance'})
    
    return data_result
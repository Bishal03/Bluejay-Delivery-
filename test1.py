import pandas as pd
from datetime import datetime, timedelta

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def analyze_consecutive_days(df):
    # Assuming 'Employee Name', 'Time Out', and 'Position ID' are relevant columns
    df['Time Out'] = pd.to_datetime(df['Time Out'])
    df['Day Difference'] = df.groupby('Employee Name')['Time Out'].diff().dt.days.fillna(0)

    consecutive_days = df[df['Day Difference'] == 1]

    for _, row in consecutive_days.iterrows():
        print(f"Employee: {row['Employee Name']}, Position ID: {row['Position ID']} worked for 7 consecutive days.")

def analyze_shift_gaps(df):
    # Assuming 'Employee Name', 'Time Out', 'Position ID', and 'Timecard Hours (as Time)' are relevant columns
    df['Time Out'] = pd.to_datetime(df['Time Out'])
    df['Timecard Hours (as Time)'] = pd.to_numeric(df['Timecard Hours (as Time)'], errors='coerce')  # Convert to numeric
    df['Shift Gap'] = df['Time Out'].diff() / pd.Timedelta(hours=1) - df['Timecard Hours (as Time)'].shift()

    shift_gaps = df[(df['Shift Gap'] > 1) & (df['Shift Gap'] < 10)]

    for _, row in shift_gaps.iterrows():
        print(f"Employee: {row['Employee Name']}, Position ID: {row['Position ID']} has a shift gap between shifts of {row['Shift Gap']} hours.")

def analyze_long_shifts(df):
    # Assuming 'Employee Name', 'Time Out', 'Position ID', and 'Timecard Hours (as Time)' are relevant columns
    df['Timecard Hours (as Time)'] = pd.to_numeric(df['Timecard Hours (as Time)'], errors='coerce')  # Convert to numeric
    long_shifts = df[df['Timecard Hours (as Time)'] > 14]

    for _, row in long_shifts.iterrows():
        print(f"Employee: {row['Employee Name']}, Position ID: {row['Position ID']} worked for more than 14 hours in a single shift.")

def main(file_path):
    data = load_data(file_path)
    analyze_consecutive_days(data)
    analyze_shift_gaps(data)
    analyze_long_shifts(data)

if __name__ == "__main__":
    file_path = "C:/Users/bisha/Downloads/Assignment_Timecard.xlsx"
    main(file_path)


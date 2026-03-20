import pandas as pd

def transform_data(df):
    df.columns = df.columns.str.strip()

    df = df.drop_duplicates()
    df = df.fillna(0)

    # 🔥 DATE FIX (Python me)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    df['Month'] = df['Order_Date'].dt.month

    # KPI
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()

    print("Total Sales:", total_sales)
    print("Total Profit:", total_profit)

    return df
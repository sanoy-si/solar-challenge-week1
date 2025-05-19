import pandas as pd

def load_country_data(country):
    return pd.read_csv(f"data/{country.lower()}_clean.csv")

def get_summary_stats(df):
    return df[['GHI', 'DNI', 'DHI']].describe()

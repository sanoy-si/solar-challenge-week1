import pandas as pd

def load_country_data(country):
    return pd.read_csv(f"https://raw.githubusercontent.com/sanoy-si/solar-clean-data/main/{country.lower()}_clean.csv")
    


def get_summary_stats(df):
    return df[['GHI', 'DNI', 'DHI']].describe()

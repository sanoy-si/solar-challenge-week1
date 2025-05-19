import streamlit as st
from utils import load_country_data, get_summary_stats
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar Data Dashboard")

country = st.selectbox("Select Country", ["Benin", "SierraLeone", "Togo"])
df = load_country_data(country)

st.subheader("Summary Statistics")
st.write(get_summary_stats(df))

st.subheader("GHI Boxplot")
fig, ax = plt.subplots()
sns.boxplot(y=df['GHI'], ax=ax)
st.pyplot(fig)

st.subheader("Top 5 GHI Readings")
st.write(df.sort_values(by="GHI", ascending=False).head(5))

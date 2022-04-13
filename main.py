import api
import streamlit as st

st.title("Bitcoin Prices")
days_slider = st.slider("No of Days", max_value=365, min_value=1, value=30)
currency_radio = st.radio(
     "Currency",
     ('CAD', 'INR', 'USD'))

def plot_line(df, currency):
    if df is None:
        print("Failed to fetch data")
    else:
        st.line_chart(df)
        avg = df[currency.upper()].mean()
        st.write("Average price during this time was {:.2f} {}".format(avg, currency.upper()))

if __name__ == "__main__":
    api = api.API()
    df = api.fetchData('bitcoin', currency_radio, days_slider)
    plot_line(df, currency_radio)

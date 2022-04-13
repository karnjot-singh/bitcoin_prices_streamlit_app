import api
import streamlit as st

st.title("Bitcoin Prices")
days_slider = st.slider("No of Days", max_value=365, min_value=1, value=30)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
currency_radio = st.radio(
     "Currency",
     ('CAD', 'INR', 'USD'))

coin_radio = st.radio(
     "Crypto Coin",
     ('BITCOIN', 'DOGECOIN', 'ETHEREUM'))

def plot_line(df, currency):
    if df is None:
        st.error("Failed to fetch data")
    else:
        st.line_chart(df)
        avg = df[currency.upper()].mean()
        st.markdown("Average price during this time was **{:.2f} {}**".format(avg, currency.upper()))

if __name__ == "__main__":
    api = api.API()
    df = api.fetchData(coin_radio.lower(), currency_radio, days_slider)
    plot_line(df, currency_radio)

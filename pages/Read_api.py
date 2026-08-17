
import streamlit as st
import requests

st.title("API Data Fetching")
amount = st.number_input("Enter the amount in USD", min_value=1)

target_curr= st.selectbox("Select the currency to convert to",  ["EUR", "GBP", "JPY","INR"])

if st.button("Convert"):
    url = "https://v6.exchangerate-api.com/v6/345f4ef028f778679b62d95c/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["conversion_rates"].get(target_curr)
        st.write(f"Exchange Rate (USD to {target_curr}): {exchange_rate}")
        if exchange_rate:
            converted_amount = amount * exchange_rate
            st.success(f"{amount} USD = {converted_amount:.2f} {target_curr}.")
        else:
            st.error("Currency not found in the API response.")
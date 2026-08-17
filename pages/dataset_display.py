import streamlit as st
import pandas as pd

st.title("Dataset Dashboard")

# file=st.file_uploader("Upload your dataset", type=["csv"])

# if file:
    # df = pd.read_csv("E:\MCA 2021-23\MCA Sem-3\ML\ML Practical\pages\house_dataset.csv") 
    # st.subheader("Dataset Preview")
    # st.dataframe(df)

df = pd.read_csv("E:\MCA 2021-23\MCA Sem-3\ML\ML Practical\pages\house_dataset.csv") 
st.subheader("Dataset Preview")
st.dataframe(df)

st.write("Dataset Summary:")
st.write(df.describe())

Bedrooms= df['Bedrooms'].unique()
st.write("Unique Bedrooms:", Bedrooms)
select_Bedroom = st.selectbox("Select no of bedroom:", Bedrooms)

filered_data= df[df['Bedrooms'] == select_Bedroom]
st.write(f"Properties with {select_Bedroom} bedrooms:")
st.write(filered_data)

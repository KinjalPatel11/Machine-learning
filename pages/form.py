import streamlit as st


st.title("Job Registration Form")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100)
dob = st.date_input("Date of Birth")
qualification = st.selectbox("Select your qualification:", ["High School", "Bachelor's", "Master's", "PhD"])
exp = st.radio("Do you have a Exprience?", ["Yes", "No"])
experience = st.slider("Experience (in years)", 0, 5,2 )
job_position = st.selectbox("Willing to apply for position: ", ['Developer', 'Data Scientist', 'Designer', 'Tester'])

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write(f"Date of Birth: {dob}")
    st.write(f"Qualification: {qualification}")
    st.write(f"Exprience: {exp}")
    st.write(f"Experience (in years): {experience}")
    st.write(f"Willing to apply for position: {job_position}")

import streamlit as st

st.title("Day 1: Introduction to Streamlit and Python Basics")
st.subheader("Welcome to the first day of our ML learning journey!.")

#hello world
st.write("Hello World , Good Morning")

# Variables and Data Types
name = "Alice"
Age = 30
st.write("Name:", name)
st.write("Age:", Age)
st.write("1+1 = ",1+1)
# arithmetic operations

# Creating a list
my_list = [1, 2, 3, 4, 5]
st.write("List:", my_list)

# select box
qualification = st.selectbox("Select your qualification:", ["High School", "Bachelor's", "Master's", "PhD"])
st.write(f"Your Qualification is {qualification}.")

# checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing to the terms and conditions.")

#creat markdown
st.markdown("# This is a markdown heading 1")

st.markdown("## This is a markdown heading 2")

st.markdown("### This is a markdown heading 3")

st.markdown("#### This is a markdown heading 4")


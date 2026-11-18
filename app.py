import streamlit as st
from groq import Groq
st.set_page_config(page_title="Student Profile",page_icon="🎓",layout="centered")
st.title("🎓 Student Profile")
st.caption("My Profile")
st.header("Personal Information")
name = st.text_input("Enter Student Name", "xxxxxxxxx")
usn = st.text_input(" Enter USN", "xxxxxxxxx")
department= st.selectbox("department", ["CSE", "ISE", "ECE", "EEE", "ME"])
year = st.radio("Current Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
if st.button("View My Profile"):
   st.markdown("###:Profile submitted successfully")
   st.write("### Profile Details")
   st.write("**Name:**", name)
   st.write("**USN:**", usn)
   st.write("**department:**", department)
   st.write("**year:**", year)
  

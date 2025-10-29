import streamlit as st
st.title("new app")
st.write("hello")
name=st.text_input("name?")
if st.button("nihao"):
    st.success(f"안녕하세요{name}님")




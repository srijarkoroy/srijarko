import streamlit as st
from utils.constants import *

def publication():
    st.header("📚 Publications",divider='red')
    st.write("")

    def publication_unit(title, position, date, location, content, button_name, button_link, code_name, code_link):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(title)
        with col3:
            st.write("")
            st.markdown("######   " + date)
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("###### " + position)
        with col3:
            st.markdown("######   " + location)
        st.write(content)
        st.link_button(button_name, button_link)
        st.link_button(code_name, code_link)
        st.divider()

    for exp in Publication:
        publication_unit(exp[0],exp[1],exp[2],exp[3],exp[4],exp[5],exp[6],exp[7],exp[8])
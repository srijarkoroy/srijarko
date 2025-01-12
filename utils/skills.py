import streamlit as st
from utils.constants import *

def skills(): 
    # skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("🔎 Skills",divider='red') 

    def skill_tab():
        rows, cols = len(info['skills'])//skill_col_size, skill_col_size
        skills = iter(info['skills'])
        if len(info['skills'])%skill_col_size!=0:
            rows+=1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    columns[index_].error(next(skills))
                except:
                    break
    with st.spinner(text="Loading section..."):
        skill_tab()
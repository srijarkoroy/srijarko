import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from streamlit_theme import st_theme

from utils.home import *
from utils.skills import *
from utils.experience import *
from utils.education import *
from utils.certifications import *
from utils.publication import *
from utils.projects import *

st.set_page_config(page_title="Srijarko Roy", layout="wide")

try:

    with st.sidebar:

        html_temp = """
            <div>
            <h1></h1>
            </div>
        """

        st.markdown(html_temp, unsafe_allow_html=True)

        
        theme = st_theme()
        if theme["base"] == "light":
            opt = option_menu("Srijarko Roy", ["Home", "Experience", "Skills", "Education", "Certifications", "Research and Projects", "Publications"],
                            icons=['house', 'bookmarks', 'code-slash', 'book', 'award','kanban','journal-bookmark'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#0e117"},
            "icon": {"color": "#FF4B4B", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#d3d3d3"},
            "nav-link-selected": {"background-color": "#898c8a"},
        }
        )
        else:
            opt = option_menu("Srijarko Roy", ["Home", "Experience", "Skills", "Education", "Certifications", "Research and Projects", "Publications"],
                                icons=['house', 'bookmarks', 'code-slash', 'book', 'award','kanban','journal-bookmark'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#0e117"},
                "icon": {"color": "#FF4B4B", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
                "nav-link-selected": {"background-color": "#262730"},
            }
            )

        html_temp = """
            <div>
            <h1></h1>
            </div>
        """

        st.markdown(html_temp, unsafe_allow_html=True)
        st.header("")

        left_co, cent1_co, cent2_co, cent3_co, cent4_co, last_co = st.columns(6)

        if theme["base"] == "light":
            with cent1_co:
                st.markdown("[![Git](https://img.icons8.com/?size=35&id=16318&format=png&color=898c8a)](https://github.com/srijarkoroy)")
            with cent2_co:
                st.markdown("[![Link](https://img.icons8.com/?size=35&id=98960&format=png&color=898c8a)](https://www.linkedin.com/in/srijarko-roy-9193751b0/)")
            with cent3_co:
                st.markdown("[![Insta](https://img.icons8.com/?size=35&id=32320&format=png&color=898c8a)](https://www.instagram.com/srijarko/)")
            with cent4_co:
                st.markdown("[![Med](https://img.icons8.com/?size=35&id=bocK2vOACVtF&format=png&color=898c8a)](https://medium.com/@srijarkoroy4u)")
        else:
            with cent1_co:
                st.markdown("[![Git](https://img.icons8.com/?size=35&id=16318&format=png&color=d3d3d3)](https://github.com/srijarkoroy)")
            with cent2_co:
                st.markdown("[![Link](https://img.icons8.com/?size=35&id=98960&format=png&color=d3d3d3)](https://www.linkedin.com/in/srijarko-roy-9193751b0/)")
            with cent3_co:
                st.markdown("[![Insta](https://img.icons8.com/?size=35&id=32320&format=png&color=d3d3d3)](https://www.instagram.com/srijarko/)")
            with cent4_co:
                st.markdown("[![Med](https://img.icons8.com/?size=35&id=bocK2vOACVtF&format=png&color=d3d3d3)](https://medium.com/@srijarkoroy4u)")

    if opt == "Home":
        home()

    elif opt == "Skills":
        skills()

    elif opt == "Experience":
        experience()
        
    elif opt == "Education":
        education()

    elif opt == "Certifications":
        certification()

    elif opt == "Publications":
        publication()

    elif opt == "Research and Projects":
        project()

except:
    st.spinner('Loading . . .')
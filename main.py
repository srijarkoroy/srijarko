import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

from utils.home import *
from utils.skills import *
from utils.experience import *
from utils.education import *
from utils.certifications import *
from utils.publication import *

st.set_page_config(layout="wide")

with st.sidebar:

    html_temp = """
        <div>
        <h1></h1>
        </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
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
    with cent1_co:
        st.markdown("[![Git](https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/github-white-icon.png)](https://github.com/srijarkoroy)")
    with cent2_co:
        st.markdown("[![Link](https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/linkedin-app-white-icon.png)](https://www.linkedin.com/in/srijarko-roy-9193751b0/)")
    with cent3_co:
        st.markdown("[![Insta](https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/instagram-white-icon.png)](https://www.instagram.com/srijarko/)")
    with cent4_co:
        st.markdown("[![Med](https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/medium-white-icon.png)](https://medium.com/@srijarkoroy4u)")

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
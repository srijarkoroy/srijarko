import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

from utils.home import *
from utils.footer import *

st.set_page_config(layout="wide")

with st.sidebar:

    html_temp = """
        <div>
        <h1></h1>
        </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("")
    
    opt = option_menu("Srijarko Roy", ["Home", "Experience", "Skills", "Education", "Licenses and Certification", "Research and Projects", "Publications", "Contact Me"],
                         icons=['house', 'bookmarks', 'code-slash', 'book', 'award','kanban','journal-bookmark','bar-chart-line'],
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
        <h1></h1>
        <h1></h1>
        <h1></h1>
        <h1></h1>
        <h1></h1>
        </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("")

    # html_temp = """
    #     <div>
    #     <img src= "/images/about/github.png">
    #     </div>
    # """

    # st.markdown(html_temp, unsafe_allow_html=True)
    # st.markdown("[![Foo](https://user-images.githubusercontent.com/66861243/236678652-807d9e9d-b30d-405f-ab78-47b83e5d0f17.png)](http://google.com.au/)")

if opt == "Home":

    home()

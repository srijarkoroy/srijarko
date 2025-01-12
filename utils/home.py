import streamlit as st

def home():

    left_co, cent1_co, last_co = st.columns(3)
    with cent1_co:
        st.image("images/about/srijarko.png", width=300)

    html_temp = """
        <div>
        <h5></h5>
        <center><h1>Hello, I'm Srijarko Roy!</h1></center>
        <center><h3>Software Engineer <br>(Digital Technology and Innovation) <br>at Wells Fargo</h3></center>
        </div>
        <hr>
        <div>
        <center><h4>Ex-Member @McCarthy Lab | Computer Vision | Deep Learning</h4></center>
        </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("")

import streamlit as st

def home():

    html_temp = """
        <div>
        <h5></h5>
        <center><img src = "https://raw.githubusercontent.com/srijarkoroy/srijarko/refs/heads/main/images/about/srijarko.png" height=350 width=350></center>
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

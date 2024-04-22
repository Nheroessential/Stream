# requirements.txt
vega_datasets==0.9.0
pandas==1.2.5
streamlit==0.86.0
altair==4.1.0
...

import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My Webpage", page_icon=":tada", layout = "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("/workspaces/Stream/style.css")


# ----Animation-------
lottie_coding = 'https://assets6.lottiefiles.com/private_files/lf30_zSGy1w.json'

# ------HEADER SECTION-----
with st.container():
    st.subheader('Hi,I am Tofunmi :wave')
    st.title("A Data Analyst")
    st.write("I am passionate about Data")
    st.write('[Learn more >]()')


# -----What I do--------
with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')

    with right_column:
        st_lottie(lottie_coding, height=300, key='Coding')

with st.container():
    st.write('---------------')
    st.header('My Projects')
    st.write('##')
    image_column, text_column = st.columns((1, 2))


# -----CONTACT-----
with st.container():
    st.write("-------")
    st.header("Reach out to me")
    st.write("##")

    contact_form = """
    <form action = "https://formsubmit.co/tofunmiareoye@gmail.com" method = "POST">
        <input type = "hidden" name = "_captcha" value = "false>
        <input type = "text" name = "name" placeholder = "Your name" required>
        <input type = "email" name = "email" placeholder = "Your email" required>
        <textarea name = "Message" placeholder = "Your message here" required></textarea>
        <button type = "submit"> Send </button>
</form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

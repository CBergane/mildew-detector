import streamlit as st


bckgr_img = '/workspace/mildew-detector/images/cherry.png'

# Define CSS style
def set_background(bckgr_img):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{bckgr_img}");
        background-size: 18%;
        background-position: top right;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")

        set_background(bckgr_img)
    
    def add_page(self, title, func) -> None: 
        self.pages.append({"title": title, "function": func })

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']() 
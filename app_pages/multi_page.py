import streamlit as st


bckgr_img = 'https://png.pngtree.com/png-clipart/20220220/original/pngtree-beautiful-border-with-falling-cherry-blossoms-in-spring-png-image_7272566.png'

# Define CSS style
def set_background(image):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{image}");
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
    
    def add_page(self, title, func) -> None: 
        self.pages.append({"title": title, "function": func })

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']() 
import streamlit as st


bckgr_img = 'https://www.kindpng.com/picc/m/37-371135_japanese-flowering-cherry-png-clipart-cherry-blossoms-no.png" alt="Japanese Flowering Cherry Png Clipart - Cherry Blossoms No Background, Transparent Png@kindpng.com'

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
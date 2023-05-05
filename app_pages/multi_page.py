import streamlit as st
import base64


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('images/cherry.png')

bckgr_img = 'https://i.pinimg.com/564x/96/f8/80/96f8800ed069252f58d52937c7d92572.jpg'


# Define CSS style
def set_background(image):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{image}");
        background-size: 100%;
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
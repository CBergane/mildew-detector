import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.leaf_visualiser import page_leaf_visualiser_body
from app_pages.performance import page_performance_body
from app_pages.mildew_detector import page_mildew_detection_page
from app_pages.page_usage import page_usage_body

background_image = 'https://images.unsplash.com/photo-1525006414893-50996169b77d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1674&q=80'

page_bg_img = '''
<style>
body {
background-image: url("%s");
background-size: cover;
}
</style>
''' % background_image

st.set_page_config(page_title='My App', page_icon=':smiley:', layout='wide', page_bg_img=page_bg_img)

app = MultiPage(app_name = "Cherry Leaf Mildew Detector")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Usage", page_usage_body)
app.add_page("Project Hypothesis", page_hypothesis_body)
app.add_page("Cherry Leaf Visualizer", page_leaf_visualiser_body)
app.add_page("ML Performance Metric", page_performance_body)
app.add_page("Mildew Detector", page_mildew_detection_page)

app.run()

import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.leaf_visualiser import page_leaf_visualiser_body
from app_pages.performance import page_performance_body
from app_pages.mildew_detector import page_mildew_detection_page
from app_pages.page_usage import page_usage_body

page_bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1525006414893-50996169b77d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1674&q=80");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
app = MultiPage(app_name = "Cherry Leaf Mildew Detector")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Usage", page_usage_body)
app.add_page("Project Hypothesis", page_hypothesis_body)
app.add_page("Cherry Leaf Visualizer", page_leaf_visualiser_body)
app.add_page("ML Performance Metric", page_performance_body)
app.add_page("Mildew Detector", page_mildew_detection_page)


app.run()
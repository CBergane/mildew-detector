import streamlit as st

def page_usage_body():
    st.write("**Here are useful guidelines for your Streamlit dashboard:**")

    st.info(
        f"1. This page summarizes the project, including the dataset, problem "
        f"statement, and methodology used."
    )

    st.info(
        f"2. Compare healthy and powdery mildew-infected cherry leaves with "
        f"our accurate visualizer tool. Identify visual markers for the disease "
        f"and assist the model for optimal accuracy through machine learning "
        f"and human supervision."
    )

    st.success(
        f"**Step by step**\n\n"
        f"To study the features of healthy and infected leaves, follow "
        f"these simple steps and make use of the image montage feature:"
        f"1. Check the last checkbox labelled **Image Montage.**"
        f"2. Select the label you want to study from the dropdown menu."
        f"3. Click the **Create Montage** button."
    )

    st.info(
        f"3. **Mildew Detector**"
        f"You can effortlessly determine whether a cherry leaf has powdery "
        f"mildew disease or not by uploading an image. Simply click on "
        f"the Browse Files button and select an image from your local "
        f"machine to get started. Once uploaded, the page will display "
        f"the prediction result, along with a confidence score."
        f"Furthermore, you can view the predicted probabilities of the "
        f"input image for each class."
    )

    st.success(
        f"To successfully detect powdery mildew disease, follow these simple steps:"
        f"1. Easily access the Streamlit dashboard on your web browser."
        f"2. Effortlessly navigate to the Powdery Mildew Detection page "
        f"by clicking on the tab in the sidebar menu."
        f"3. Select an image or a batch from your local machine by "
        f"clicking **Browse files,** and upload it without any "
        f"complications. Or use the drag and drop feature."
        f"4. Observe the model's predictions accurately displayed below. "
        f"Analyze the features and metrics as necessary. To see the "
        f"prediction result, locate the predicted class and corresponding "
        f"confidence score."
        f"5. If the model appears uncertain, you can confidently make "
        f"the decision yourself by scrolling through the predictions."
        f"6. Finally, at the bottom of the page, download a prediction "
        f"report with ease."
    )

    st.info(
        f"4. *Project Hypothesies:* The aim of this page is to provide a succinct summary of the "
        f"Machine Learning project and its anticipated outputs. This data "
        f"holds immense significance for stakeholders, business "
        f"proprietors, executives, and managers who rely on the "
        f"project's consequences to make informed strategic decisions."
    )

    st.info(
        f"5. *ML Performance Metric* for the machine learning model used in "
        f"the project can be found on this page. Technical staff members "
        f"can explore the model's precision, recall, F1 score, and "
        f"confusion matrix to gain a deeper understanding of its "
        f"performance. This information is crucial for building and "
        f"refining the model, and it can also be valuable for other "
        f"stakeholders seeking to comprehend the technical aspects of "
        f"the project."
    )
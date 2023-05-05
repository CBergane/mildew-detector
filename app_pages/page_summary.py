import streamlit as st


def page_summary_body():
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"I wanted to share some important information with "
        f"fungal infection called powdery mildew? However, manually "
        f"inspecting the leaves to detect this infection is not practical or "
        f"efficient for farms with a large number of trees. That's why a "
        f"machine learning (ML) system has been proposed to solve this "
        f"problem. This amazing system can quickly analyze an image of "
        f"a cherry leaf and accurately determine if it's healthy or infected "
        f"with powdery mildew. The system was developed using a "
        f"dataset of cherry leaf images provided by Farmy & Foods’ "
        f"crops."
        )

    st.write(
        f"* For additional information on the dataset and data preparation, "
        f"see the [README file]"
        f"https://github.com/CBergane/mildew-detector/blob/main/README.md")

    st.success(
        f"**Business requirements:**\n"
        f"* 1 - A study is being planned to differentiate healthy cherry "
        f"leaves from those infected with powdery mildew.\n"
        f"* 2 - A quick and accurate method is needed to determine if a "
        f"cherry tree is healthy or diseased.\n"
        f"* 3 - The client also desires a dashboard that fulfils these criteria.\n"
        f"* 4 - Clear explanations of the results are expected by the client.\n"
    )

    st.info(
        f"**Objectives\n\n"
        f"* This system can accurately determine the health of a cherry "
        f"leaf and detect powdery mildew infections based on an image "
        f"of the leaf."
        f"* I believe our solution will greatly improve the detection of "
        f"powdery mildew on cherry trees in different farms, providing a "
        f"timely and flexible response."
    )

    st.info(
        f"**Processes\n\n"
        f"1. Collect the cherry leaf images dataset provided by Farmy & Foods.\n"
        f"2. Preprocess the images by cleaning, resizing, and "
        f"normalizing them to ensure they are ready for ML algorithms.\n"
        f"3. Augment the training dataset images to significantly "
        f"improve the model's performance.\n"
        f"4. Develop a highly effective supervised ML model, such as "
        f"Convolutional Neural Networks (CNNs), to accurately classify "
        f"cherry leaves as healthy or infected with powdery mildew.\n"
        f"5. Train the model using the preprocessed dataset and validate "
        f"its performance on a separate test dataset.\n"
        f"6. Deploy the trained model to a dashboard that displays its "
        f"predictions and meets the client's requirements.\n"
        f"7. Conduct a thorough study to visually distinguish between "
        f"healthy and powdery mildew-infected cherry leaves and "
        f"predict the health of cherry trees using the deployed model.\n"
        f"8. Provide the client with a range of possible outcomes and "
        f"explanations to facilitate informed decision-making."
    )
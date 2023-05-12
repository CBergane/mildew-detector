import streamlit as st


def page_hypothesis_body():
    st.write("### Project Hypothesis One and validation")

    st.success(
        f"Through the utilization of machine learning algorithms, it is feasible "
        f"to discriminate between cherry leaves that are contaminated with "
        f"powdery mildew and those that are healthy based on their "
        f"distinctive visual attributes. In general, cherry leaves that have been "
        f"affected by powdery mildew display a visible powdery white or "
        f"greyish coating on their surface, accompanied by prominent white "
        f"or greyish marks."
    )
    st.info(
        f"The machine learning model effectively differentiated among "
        f"various data points and used this knowledge to accurately forecast "
        f"outcomes on new data without relying excessively on the training "
        f"set. As a result, the model can offer reliable predictions for future "
        f"observations by generalizing its forecasts. Instead of simply "
        f"memorizing the correlations between features and labels in the "
        f"training data, the model comprehends overall patterns, which "
        f"boosts its predictive capacity. Remarkably, the model achieved a "
        f"perfect accuracy of 100% in performing these tasks."
    )

    st.write(
        f"If you want to examine the visual attributes of healthy and infected "
        f"leaves, you can find the **Cherry Leaf Visualizer** tab."
    )

    st.write("### Hypotesis Two and validation")

    st.success(
        f"Based on the image data it has been trained on, the machine "
        f"learning system can confidently differentiate between cherry leaves "
        f"that are healthy and those that have been infected with powdery "
        f"mildew. Its high level of accuracy, consistently at or above 90%, "
        f"suggests that this classification task is both straightforward and "
        f"well-suited to this particular method of analysis."
    )

    st.info(
        f"According to the model developed, the hypothesis has been "
        f"validated with outstanding results in assessing the project's "
        f"business functionality and triumph. The F1 score and recall for the "
        f"powdery mildew label both reached an impressive 100%."
    )

    st.write(
        f"For those interested in reviewing the model's performance metrics, "
        f"kindly refer to the** ML Prediction Metrics** tab."
    )

    st.write("### Hypotesis Three and validation")

    st.success(
        f"Integrating image visualization into the cherry leaf inspection "
        f"process greatly minimizes the risk of misidentifying infected leaves."
    )

    st.info(
        f"While the ML model is indeed precise in its predictions, it may prove "
        f"challenging to discern the visual characteristics of the disease "
        f"during its early stages. However, to further enhance the accuracy of "
        f"the model and achieve even better results, a staff member "
        f"examines cases where the model lacks confidence during the "
        f"prediction process visually. This process involves utilizing an image "
        f"and a prediction plot in the Powdery Mildew Detection tab."
    )

    st.write(
        f"To review the performance metrics of the model, "
        f"please visit the **Mildew Detector**  section."
    )

    st.write("### Hypotesis Four and validation")

    st.success(
        f"Implementing a machine learning solution is the way to go for "
        f"improving the accuracy and speed of cherry leaf inspection. This "
        f"will lead to more efficient use of resources, enhanced productivity, "
        f"and greater worker safety. Furthermore, it will significantly cut down "
        f"on the time and exposure required for manual cherry leaf inspection."
    )

    st.info(
        f"Based on the business case, it's clear that manually inspecting and "
        f"treating 100 trees would take approximately 50 hours. However, "
        f"using an ML model to analyse pictures of the leaves takes just a "
        f"minute per tree. This means that taking pictures and uploading "
        f"them for analysis would only require an hour and 40 minutes for all "
        f"100 trees. With the ML model being 100% accurate in detecting "
        f"unhealthy trees, there's no longer a need for manual visual "
        f"inspection."
        f"The employee can focus solely on the trees identified by the model "
        f"as having powdery mildew and administer the appropriate "
        f"compound. Implementing an ML model would significantly reduce "
        f"the time needed to inspect and treat 100 trees, making the process "
        f"much more efficient."
    )

    st.write("### Hypotesis Five and validation")

    st.success(
        f"Through the implementation of ML prediction, the company can "
        f"significantly reduce its reliance on manual labour for identifying "
        f"powdery mildew on cherry leaves. This results in substantial cost "
        f"savings and improved efficiency."
    )

    st.info(
        f"To assess the impact of the ML solution, we must compare the "
        f"manual inspection process before and after implementation. "
        f"Employee feedback can also provide valuable insight into the "
        f"effectiveness of the system."
    )

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
from src.machine_learning.evaluate import load_test_evaluation

def page_performance_body():
    version = 'v1'
    output_dir = f"outputs/{version}/"

    st.write("### Train, Validation and Test set: Label Frequencies")

    labels_distribution = plt.imread(f"{output_dir}img_distribution.png")
    st.image(labels_distribution,
             caption="Label Distribution on Train, Validation and Test sets")
    st.info(f"* The original dataset has a total 2104 images labelled **healthy**"
            f" and 2104 image files labelled powder_mildew\n\n"
            f"* The dataset was split into train, validation and test set in the ratio 0.7, 0.2 and 0.1.")
    st.write('---')

    if st.checkbox("Model History"):
        st.write('### Model History')
        st.info(f"")
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f'{output_dir}training_and_validation_metrics.png')
            st.image(model_acc, caption="Model Training And Validation Accuracy", width=600)
        st.info(
            f"A model history plot is an effective visualization tool that showcases "
            f"an ML model's progress during both training and validation. It "
            f"provides valuable insights into the model's performance over time "
            f"by plotting the performance metric on the y-axis and the number of "
            f"training epochs on the x-axis. A good model history plot should "
            f"exhibit consistent and sustained improvement in performance on "
            f"both the training and validation sets, without any signs of overfitting. "
            f"This means that the validation accuracy curve should remain stable "
            f"throughout the epochs, and the loss curves should align perfectly. "
            f"Moreover, the validation accuracy should remain steady without any "
            f"sign of plateauing, while the training accuracy continues to "
            f"increase.\n\n"
            f"In case there is a significant fluctuation in loss and validation loss "
            f"curves, it may be due to random noise or data fluctuations. "
            f"However, if the model accuracy consistently stays at 100% during "
            f"training and the validation set shows minimal and consistent "
            f"fluctuation over multiple iterations, there is likely no problem. "
            f"Therefore, a well-designed model history plot is a crucial tool for "
            f"evaluating an ML model's performance and ensuring that it is "
            f"functioning optimally."
        )
        st.write('---')

    st.write('### Generalised Performance on Test Set')
    load_test_evaluation(version)
    st.info(
        f"The plot shows the evaluation metrics of the trained ML model on "
        f"the test dataset. The two metrics displayed are loss and accuracy, "
        f"which are important indicators of the model's performance. The loss "
        f"value of 0.0009 indicates how much the predicted values deviate "
        f"from the true values on average, with lower values being better. "
        f"Typically, a loss value of 0.0009 is considered a good value for "
        f"binary classification problems. The accuracy value of 1 shows the "
        f"proportion of correctly classified instances in the test dataset, with "
        f"higher values being better.\n\n"
        f"Overall, a low loss value and high accuracy value indicate that the "
        f"machine learning model is performing well on the test dataset and "
        f"has learned to generalize well to new, unseen data. This means that "
        f"the model can be considered robust and reliable, and can be used "
        f"with confidence to make predictions on new data."
    )
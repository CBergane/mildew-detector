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

    st.write('### Confusion Matrix')

    confusion_matrix = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(confusion_matrix, caption="Confusion Matrix", width=500)

    st.info(
        f"The matrix is divided into four quadrants: true positives (TP), true "
        f"negatives (TN), false positives (FP), and false negatives (FN). TP "
        f"and TN represent accurate predictions, while FP and FN indicate "
        f"inaccurate predictions. The model's accuracy metric is 100%, "
        f"meaning that all predictions are correct. However, the loss metric is "
        f"0.09%, which measures the discrepancy between the predicted and "
        f"true labels. Despite this slight discrepancy, the model's high "
        f"accuracy and low loss indicate that it is making precise predictions."
    )

    classification_report = plt.imread(
        f"outputs/{version}/classification_report.png")
    st.image(classification_report, caption='Classification Report')

    st.info(
        f"Based on the classification report, it seems that the model has "
        f"performed exceptionally well in terms of precision and recall for "
        f"both classes. Precision is calculated by dividing the number of true "
        f"positives by the sum of true and false positives, while recall is "
        f"determined by dividing the number of true positives by the sum of "
        f"true positives and false negatives. A high precision score indicates "
        f"that the model can accurately identify true positives while "
        f"minimizing false positives. Similarly, a high recall score means that "
        f"the model can effectively identify true positives while keeping false "
        f"negatives to a minimum."
    )

    st.write("### ROC Curve")

    roc_curve = plt.imread(f"outputs/{version}/roc_curve.png")
    st.image(roc_curve, caption='ROC Curve')

    st.info(
        f"The model's ROC curve reveals its impressive ability to accurately "
        f"differentiate between positive and negative samples, with a high "
        f"true positive rate (sensitivity) and low false positive rate (1 - "
        f"specificity) across various thresholds. The AUC score of 1.0 "
        f"confidently demonstrates its exceptional performance in "
        f"distinguishing between the 'Healthy' and 'Powdery Mildew' classes, "
        f"with perfect separation between the two."
    )
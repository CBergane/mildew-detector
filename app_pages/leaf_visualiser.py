
import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import itertools
import random
import glob
import itertools


def page_leaf_visualiser_body():
    version = 'v1'
    output_dir = f"outputs/{version}"

    st.write('### Cherry Leaf Visualiser')
    st.info(
        f"The objective here is to visually differentiating a **healthy**"
        f" cherry leaf from that which contains **powdery mildew**."
    )
    st.warning(
        f"Powdery mildew can cause cherry leaves to develop a white or "
        f"greyish powdery coating on their surface. The most noticeable sign "
        f"of infection is the appearance of white or greyish marks on the "
        f"leaves, which can take on the form of irregular blotches or spots.\n\n"
        f"To ensure optimal feature extraction and training when working with "
        f"image datasets, it is crucial to prepare the images beforehand. This "
        f"is especially true when analyzing powdery mildew on a leaf, where "
        f"normalizing the images in the dataset is crucial before training a "
        f"Neural Network. By calculating the mean and standard deviation of "
        f"the entire dataset and taking into account the visual properties of "
        f"the powdery mildew on the leaf, we can enable the machine "
        f"learning model to accurately and efficiently learn the relevant "
        f"features from the image data."
    )

    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"{output_dir}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"{output_dir}/avg_var_powdery_mildew.png")

        st.warning(
            f"We observed that a difference in the level of color pigmentation.\n\n"
            f"* The healthy leaves appear to have a more uniform green colour than the powdery mildew leaf.\n\n"
            f"* The veins appear more visible in the mildew leaf compared to the healthy leaf."
        )

        st.image(avg_healthy, caption="Healthy Cherry Leaf - Average and Variability")
        st.image(
            avg_mildew, caption="Powdery Mildew Cherry Leaf - Average and Variability")
        st.write('---')

    if st.checkbox('Differences between Healthy and Powdery Mildew cherry leaves'):
        avg_diff = plt.imread(f"{output_dir}/avg_diff.png")

        st.warning(
            f"* The first two images show the average which is explained in the second checkbox. "
            f" In the difference between variability, the darker area shows where both images"
            f" are similar while the lighter area shows where variability differences. "
        )

        st.image(avg_diff, caption='Difference between average images')
        st.write('---')

    if st.checkbox("Image Montage"):
        st.write(
            "- To view the montage, select a label and click on **Create Montage** button")
        st.write('- To refresh the image montage, click on **Create Montage** button')
        data_dir = 'inputs/cherryleaves_dataset/cherry-leaves/validation'
        labels = os.listdir(data_dir)
        label_to_display = st.selectbox(
            label="Select label",
            options=labels,
            index=0
        )
        if st.button("Create Montage"):
            st.warning(
                f"**Observation**\n\n"
                f"* The average dimension of the leaf images is 256px width by 256px height\n\n"
                f"* The mildew leaves have visible white streaks on them"
                f" which differentiates them from healthy leaves"
            )
            image_montage(data_dir, label_to_display,
                          nrows=3, ncols=3, figsize=(10, 12))
            st.write('---')


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10), sort_order='alphabetical'):
    """
    Displays a montage of images from a directory subset based on a given label.

    Args:
    - dir_path (str): The path to the directory containing the image files.
    - label_to_display (str): The label corresponding to the image subset to display.
    - nrows (int): The number of rows in the image montage.
    - ncols (int): The number of columns in the image montage.
    - figsize (tuple, optional): The size of the matplotlib figure. Default is (15, 10).
    - sort_order (str, optional): The sorting order of the image files. Options are 'alphabetical' or 'numerical'. Default is 'alphabetical'.

    Returns:
    - None
    """
    
    # Check if the label exists in the directory
    if label_to_display not in os.listdir(dir_path):
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {os.listdir(dir_path)}")
        return
    
    # Load the image files in the subset directory
    img_files = glob.glob(os.path.join(dir_path, label_to_display, '*'))
    
    # Sort the image files based on the specified order
    if sort_order == 'alphabetical':
        img_files.sort()
    elif sort_order == 'numerical':
        img_files = sorted(img_files, key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    else:
        print("Invalid sort order. Please specify 'alphabetical' or 'numerical'.")
        return
    
    # Check if the montage space is greater than the subset size
    if nrows * ncols > len(img_files):
        print(f"Decrease nrows or ncols to create your montage. There are {len(img_files)} in your subset.")
        return
    
    # Create a list of axes indices based on nrows and ncols
    plot_idx = list(itertools.product(range(nrows), range(ncols)))
    
    # Create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for i, ax in enumerate(axes.flat):
        img = plt.imread(img_files[i])
        img_shape = img.shape
        ax.imshow(img)
        ax.set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout()
    st.pyplot(fig=fig)
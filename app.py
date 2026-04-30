import streamlit as st
import cv2

st.title("VisionCraft")
img = cv2.imread("image1.jpeg")

import filters 
import utils 


st.set_page_config(page_title="Image Editor", page_icon="⭐")

st.title("⭐ Image Editing & Processing App")

# Sidebar controls
st.sidebar.header("Controls")

blur = st.sidebar.slider("Blur", 1, 51, 1, step=2)
sharp = st.sidebar.slider("Sharpness", 0.0, 3.0, 0.0)
brightness = st.sidebar.slider("Brightness", -100, 100, 0)
contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)

edge = st.sidebar.checkbox("Edge Detection")
gray = st.sidebar.checkbox("Grayscale")

t1 = st.sidebar.slider("Threshold1", 0, 255, 100)
t2 = st.sidebar.slider("Threshold2", 0, 255, 200)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = utils.read_image(uploaded_file)
    output = img.copy()

    # Apply filters
    output = filters.apply_blur(output, blur)
    output = filters.apply_sharpness(output, sharp)
    output = filters.apply_brightness(output, brightness)
    output = filters.apply_contrast(output, contrast)

    if gray:
        output = filters.apply_gray(output)

    if edge:
        output = filters.apply_edge(output, t1, t2)

    # Display images
    col1, col2 = st.columns(2)

    with col1:
        st.image(img, caption="Original", channels="BGR")

    with col2:
        st.image(output, caption="Processed", channels="BGR")

    # Download
    img_bytes = utils.convert_to_bytes(output)

    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="edited.png",
        mime="image/png"
    )


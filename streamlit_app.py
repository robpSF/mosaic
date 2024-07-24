import streamlit as st
import cv2
import numpy as np
from PIL import Image

def apply_mosaic(image, piece_size):
    # Get image dimensions
    h, w = image.shape[:2]
    
    # Resize image to smaller size
    temp = cv2.resize(image, (w // piece_size, h // piece_size), interpolation=cv2.INTER_LINEAR)
    
    # Scale back to original size
    mosaic = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
    
    return mosaic

st.title("Mosaic Image Transformer")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

    st.image(image, caption='Original Image', use_column_width=True)
    
    # Slider to control mosaic piece size
    piece_size = st.slider("Mosaic Piece Size", min_value=2, max_value=100, value=10)
    
    # Apply mosaic effect
    mosaic_image = apply_mosaic(image, piece_size)
    
    st.image(mosaic_image, caption='Mosaic Image', use_column_width=True)

if __name__ == "__main__":
    st.run()

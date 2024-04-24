import streamlit as st
from PIL import Image, ImageFilter
from PIL import ImageEnhance

# Title and description
st.title('Image Processing Web App')
st.write('This web app performs simple image processing tasks.')

# File upload
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Image processing options
    st.sidebar.title('Image Processing Options')

    # Convert to grayscale
    if st.sidebar.checkbox('Convert to Grayscale'):
        grayscale_image = image.convert('L')
        st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)

    # Blur the image
    if st.sidebar.checkbox('Blur'):
        blur_radius = st.sidebar.slider('Select blur radius', 0, 10, 2)
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
        st.image(blurred_image, caption='Blurred Image', use_column_width=True)

    # Rotate the image
    if st.sidebar.checkbox('Rotate'):
        rotation_angle = st.sidebar.slider('Select rotation angle', -180, 180, 0)
        rotated_image = image.rotate(rotation_angle)
        st.image(rotated_image, caption='Rotated Image', use_column_width=True)

    # Flip the image
    if st.sidebar.checkbox('Flip'):
        flip_direction = st.sidebar.radio('Select flip direction', ('Horizontal', 'Vertical'))
        if flip_direction == 'Horizontal':
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        st.image(flipped_image, caption='Flipped Image', use_column_width=True)





    # Adjust brightness and contrast
    brightness_and_contrast = st.sidebar.checkbox('Adjust Brightness & Contrast')
    if brightness_and_contrast:
        brightness_factor = st.sidebar.slider('Brightness', 0.0, 2.0, 1.0)
        contrast_factor = st.sidebar.slider('Contrast', 0.0, 2.0, 1.0)

        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(brightness_factor)

        enhancer = ImageEnhance.Contrast(brightened_image)
        contrasted_image = enhancer.enhance(contrast_factor)

        st.image(contrasted_image, caption='Adjusted Image', use_column_width=True)

     # Reset button
    if st.sidebar.button('Reset'):
        st.sidebar.clear()


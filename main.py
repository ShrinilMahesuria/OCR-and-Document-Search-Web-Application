import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Initialize the OCR reader for English and Hindi
reader = easyocr.Reader(['en', 'hi'], gpu=False)

# Streamlit app setup
st.title("OCR and Document Search Web Application")
st.write(
    "Upload an image containing text in both Hindi and English. The app will extract the text and allow you to perform a keyword search.")

# Upload the image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to a NumPy array for easyocr
    image_np = np.array(image)

    # Perform OCR on the uploaded image
    with st.spinner("Extracting text..."):
        results = reader.readtext(image_np)
        extracted_text = " ".join([res[1] for res in results])

    st.subheader("Extracted Text")
    st.text_area("Extracted Text", value=extracted_text, height=300)

    # Search functionality
    search_keyword = st.text_input("Enter a keyword to search within the extracted text")

    if st.button("Search"):
        if search_keyword:
            search_results = [result[1] for result in results if search_keyword.lower() in result[1].lower()]
            if search_results:
                st.subheader("Search Results")
                for match in search_results:
                    st.markdown(f"- {match}")
            else:
                st.warning("No matching text found.")
        else:
            st.warning("Please enter a search keyword.")

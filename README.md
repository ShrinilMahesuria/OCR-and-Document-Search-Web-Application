# OCR-and-Document-Search-Web-Application
Developed and deployed  a web-based prototype that demonstrates the ability to perform Optical Character Recognition (OCR) on an uploaded image (in picture format) containing text in both Hindi and English. The web application also implements a basic keyword search functionality based on the extracted text.

## Features
- Upload images in JPEG, JPG or PNG format.
- Extract text from images using EasyOCR.
- User-friendly interface powered by Streamlit.
- User can Search any word from extracted text.
- Display Search Results from extracted text on the same page.

## Technologies Used

- [Streamlit](https://streamlit.io/) - for creating the web app.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - for OCR functionality.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - for image processing.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2. Set up a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
    pip install -r requirements.txt

4. Run the Streamlit app:
    streamlit run app.py

## Usage
1. Open the app in your web browser.
2. Upload an image using the file uploader.
3. After Uploading the Image Text Extracting from Uploaded Image will start. 
4. And you can retrieve the text from the image,The extracted text will be displayed on the page.
5. You can Search for the word from extracted text.
6. After clicking on Search Button you can retrieve the text containing searched word.

Deployment
This app is deployed on Streamlit Sharing. You can access it via the following link: Your Deployed App URL

Troubleshooting
If you encounter any issues, please check the following:
    Ensure all dependencies are correctly listed in requirements.txt.
    Check for any errors in the logs on the Streamlit Sharing dashboard.

Contributing
    Contributions are welcome! If you have suggestions for improvements or features, 
    please create an issue or submit a pull request.

Acknowledgments
    Thanks to the developers of Streamlit and EasyOCR for their fantastic tools.

### Notes

- Replace `yourusername` and `yourrepository` with your actual GitHub username and repository name.
- Update the deployment URL with the actual link to your Streamlit app.
- Feel free to add any additional sections or information that might be relevant to your project!



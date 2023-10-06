from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from extract_data import extract_information_from_ocr_results
from save_to_mongo import save_to_mongodb
import pytesseract
from PIL import Image

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hospital_db']  # Assuming 'hospital_db' is your database name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        # Assuming you have a function process_image(file) which extracts data using OCR
        process_image(file)
        return "File uploaded and processed successfully!"
    else:
        return "No file uploaded"

def process_image(file):
    enhanced_image = enhance_image(file)
    ocr_text = pytesseract.image_to_string(enhanced_image)
    extracted_data = extract_information_from_ocr_results(ocr_text)
    save_to_mongodb(extracted_data)

# def enhance_image(file):
#     # Implement your image enhancement logic here
#     # ...

if __name__ == '__main__':
    app.run(debug=True)

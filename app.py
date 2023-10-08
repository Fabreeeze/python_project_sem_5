from flask import Flask, render_template, jsonify, request, redirect
from pymongo import MongoClient
from enhance_image import enhance_image
from extract_data import extract_information_from_ocr_results
from save_to_mongo import save_to_mongodb
from save_to_mongo import load_from_mongodb
import pytesseract
from PIL import Image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hospital_db']  # Assuming 'hospital_db' is your database name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print('\noioioi\n\noioii\nreached upload\noioioi\n\n\n')
    file = request.files['file']
    if file.filename != '':
        # Assuming you have a function process_image(file) which extracts data using OCR
        # image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        process_image(file)
        return "File uploaded and processed successfully!"
    else:
        return "No file uploaded"

def process_image(file):
    print('-----------------\n\n\n\n\n-----------oioioi\n\noioii\nreached processing\n--------\noioioi\n\n\n')
    enhanced_image = enhance_image(file)
    ocr_text = pytesseract.image_to_string(enhanced_image)
    extracted_data = extract_information_from_ocr_results(ocr_text)
    save_to_mongodb(extracted_data)

     # Assuming the data was successfully uploaded to the database, we return a success message
    return jsonify({"success": True})


@app.route('/database_data')
def database_data():
    data = load_from_mongodb()
    return render_template('database.html', data=list(enumerate(data, start=1)))

if __name__ == '__main__':
    app.run(debug=True)

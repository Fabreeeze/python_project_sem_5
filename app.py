from flask import Flask, render_template, jsonify, request, redirect, json, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
from enhance_image import enhance_image
from extract_data import extract_information_from_ocr_results
from save_to_mongo import save_to_mongodb
from save_to_mongo import load_from_mongodb
from save_to_mongo import remove_item
import pytesseract
from flask import session
from PIL import Image
import numpy as np
import cv2
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

# Accessing environment variables



app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # print('\noioioi\n\noioii\nreached upload\noioioi\n\n\n')
    # file = request.files['file']
    # if file.filename != '':
    #     # Assuming you have a function process_image(file) which extracts data using OCR
    #     # image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    #     process_image(file)
    #     return jsonify({"message": "File uploaded and processed successfully.", "success": True})
    # else:
    #     return jsonify({"message": "No file uploaded", "success": False})
    try:
        file = request.files['file']
        if file.filename != '':
            extracted_data = process_image(file)
            session['extracted_data'] = extracted_data
            return redirect('/edit_data') 
        else:
            return jsonify({"message": "No file uploaded", "success": False})
    except Exception as e:
        print(e)
        return jsonify({"message": str(e), "success": False}), 500

def process_image(file):
    print('-----------------\n\n\n\n\n-----------oioioi\n\noioii\nreached processing\n--------\noioioi\n\n\n')
    enhanced_image = enhance_image(file)
    ocr_text = pytesseract.image_to_string(enhanced_image)
    extracted_data = extract_information_from_ocr_results(ocr_text)

    # save_to_mongodb(extracted_data)
    return extracted_data
    
     # Assuming the data was successfully uploaded to the database, we return a success message
    # return jsonify({"success": True})


@app.route('/edit_data', methods=['GET'])
def edit_data():
    extracted_data = session.get('extracted_data')
    print(render_template('edit_data.html', extracted_text=extracted_data))
    return render_template('edit_data.html', extracted_text=extracted_data)


@app.route('/submit_edited_data', methods=['POST'])
def save_data():
    edited_text = request.form['edited_text']
    import re
    pattern = re.compile('(?<!\\\\)\'')
    edited_text = pattern.sub('\"', edited_text)
    final_extracted_data = json.loads(edited_text)
    save_to_mongodb(final_extracted_data)
    # return jsonify({"message": "Data successfully saved to the database.", "success": True})
    return redirect(url_for('index'))


@app.route('/database_data')
def database_data():
    data = load_from_mongodb()
    return render_template('database.html', data=list(enumerate(data, start=1)))

@app.route('/test',methods =['POST'])
def testFunction():
    return render_template('edit_data.html',extracted_text='ansh')


@app.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.json.get('itemId')

    result = remove_item(item_id)
    
    
    if result.deleted_count == 1:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 400



if __name__ == '__main__':
    app.run(debug=True)

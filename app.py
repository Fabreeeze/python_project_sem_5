from flask import Flask, render_template, request, jsonify
from enhance_image import enhance_image
from extract_information import extract_information

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    enhanced_image = enhance_image(file)
    information = extract_information(enhanced_image)

    # Store information in database
    # Insert code for MongoDB or MySQL here

    return jsonify({'message': 'Information extracted and stored successfully'})

if __name__ == '__main__':
    app.run(debug=True)

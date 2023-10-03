import pytesseract
import re
import numpy as np

def extract_information(image):
    
    def extract_information_from_ocr_results(ocr_text):
    name_pattern = r'Name:\s*(.*)'
    email_pattern = r'Email:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    blood_group_pattern = r'Blood Group:\s*([ABO]\s?[-+]?)'
    sex_pattern = r'Sex:\s*(Male|Female)'
    phone_number_pattern = r'Phone:\s*(\d{10})'
    age_pattern = r'Age:\s*(\d{1,3})'
    
    name = re.search(name_pattern, ocr_text, re.IGNORECASE)
    email = re.search(email_pattern, ocr_text, re.IGNORECASE)
    blood_group = re.search(blood_group_pattern, ocr_text, re.IGNORECASE)
    sex = re.search(sex_pattern, ocr_text, re.IGNORECASE)
    phone_number = re.search(phone_number_pattern, ocr_text)
    age = re.search(age_pattern, ocr_text)
    
    extracted_data = {
        'Name': name.group(1) if name else None,
        'Email': email.group(1) if email else None,
        'Blood Group': blood_group.group(1) if blood_group else None,
        'Sex': sex.group(1) if sex else None,
        'Phone Number': phone_number.group(1) if phone_number else None,
        'Age': age.group(1) if age else None
    }
    
    return extracted_data

def process_image(file):
    enhanced_image = enhance_image(file)
    
    # Convert enhanced image to text using pytesseract
    ocr_text = pytesseract.image_to_string(enhanced_image)
    
    # Extract information from OCR results
    extracted_data = extract_information_from_ocr_results(ocr_text)
    
    return extracted_data

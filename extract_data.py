import re

def extract_information_from_ocr_results(ocr_text):
    # Add your regular expressions here
    # For example:
    name_pattern = r"Name: (.+)"
    email_pattern = r"Email: (.+)"
    # Add more patterns as needed

    # Use regular expressions to extract information
    name_match = re.search(name_pattern, ocr_text)
    email_match = re.search(email_pattern, ocr_text)
    # Extract other information as needed


    print("raw data is => ",ocr_text)
    # Create a dictionary to store the extracted information
    extracted_data = {
        'name': name_match.group(1) if name_match else None,
        'email': email_match.group(1) if email_match else None,
        # Add more fields as needed
    }
    print("extracted data is =>",extracted_data)
    print("\nUwU ---\n\n\ndata extracted  \n\n\n\n----------\n\n\n")
    return extracted_data

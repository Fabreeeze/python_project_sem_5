import cv2
import numpy as np

def enhance_image(file):
    # Read the image from the file stream
    image_stream = file.read()
    nparr = np.frombuffer(image_stream, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Step 1: Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Apply adaptive thresholding for better text visibility
    enhanced_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Step 3: Apply morphological operations to remove noise
    kernel = np.ones((1, 1), np.uint8)
    enhanced_image = cv2.dilate(enhanced_image, kernel, iterations=1)
    enhanced_image = cv2.erode(enhanced_image, kernel, iterations=1)

    # Step 4: Convert the enhanced image back to RGB format
    enhanced_image_rgb = cv2.cvtColor(enhanced_image, cv2.COLOR_GRAY2RGB)
    print("\nUwU ---\n\n\nImage Enhanced \n\n\n\n----------\n\n\n")
    return enhanced_image_rgb

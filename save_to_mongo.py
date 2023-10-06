def save_to_mongodb(extracted_data):
    
    db.extracted_data.insert_one(extracted_data)
    print("Data saved to MongoDB successfully!")

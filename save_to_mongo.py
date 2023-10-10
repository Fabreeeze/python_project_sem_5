from pymongo import MongoClient



def save_to_mongodb(extracted_data):

     # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/') 

    # Access the database
    db = client['OCR_project']  

    # Access the collection
    collection = db['testing_data_collection'] 

    # Insert the extracted data into the collection
    collection.insert_one(extracted_data)

    print("\nUwU ---\n\n\ndata stored\n\n\n\n----------\n\n\n")
    # Close the connection when you're done
    
    db.close()


def load_from_mongodb():
        # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/') 

    # Access the database
    db = client['OCR_project']  

    # Access the collection
    collection = db['testing_data_collection'] 
    data = db.testing_data_collection.find()  # Fetch data from MongoDB
    
    db.close()
    return data

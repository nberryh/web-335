#-----------------------------------------------------
# Title: berryhill-usersp2.py
# Author: Nolan Berryhill
# Date: 24 September 2023
# Description: Exercise 7.3 
#-----------------------------------------------------

# Import the pymongo
import pymongo

# Connection to MongoDB
connection_string = "mongodb+srv://web335_user:s3cret@cluster0.wmphxtw.mongodb.net/web335DB"

# Connect to the MongoDB database
try:
    client = pymongo.MongoClient(connection_string)
    print("Connected to MongoDB")
except pymongo.errors.ConnectionFailure:
    print("Failed to connect to MongoDB")

# Create a new user document
new_user = {
    "firstName": "Sally",
    "lastName": "Daisy",
    "employeeId": "1027",
    "email": "sallydaisy@mail.com"
}

# Insert the new user document into the users collection
db = client.web335DB
user_collection = db.users
user_collection.insert_one(new_user)
print("New user document created")

# Display the newly created document
print("\nNewly created user document:")
created_user = user_collection.find_one({"employeeId": "1027"})
print(created_user)

# Update the email address of the document
updated_email = "sallydaisy_updated@mail.com"
user_collection.update_one({"employeeId": "1027"}, {"$set": {"email": updated_email}})
print("\nEmail address updated to: {updated_email}") 
      
#Display the updated document
print("\nUpdated user document:")
updated_user = user_collection.find_one({"employeeId": "1027"})
print(updated_user)

# Delete the document
user_collection.delete_one({"employeeId": "1027"})
print("\nUser document deleted")

# Prove the document was deleted
deleted_user = user_collection.find_one({"employeeId": "1027"})
if deleted_user is None:
    print("\nUser document has been successfully deleted")
else:
    print("\nUser document still exists")

# Close the mongoDB connection
client.close()
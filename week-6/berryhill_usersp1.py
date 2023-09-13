#-----------------------------------------------------
# Title: berryhill-usersp1.py
# Author: Nolan Berryhill
# Date: 17 September 2023
# Description: Exercise 6.3 
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

# Select the 'web335DB' database
db = client.web335DB

# Display all documents in the user's collection
print("All documents in the user's collection:")
user_collection = db.users
all_users = user_collection.find()
for user in all_users:
    print(user)

# Display a document where the employeeId is 1011
print("\nDocument where employId is 1011:")
user_1011 = user_collection.find_one({"employeeId": 1011})
print(user_1011)

# Display a document where lastName is Mozart
print("\nDocument where lastName is Mozart:")
user_mozart = user_collection.find_one({"lastName": "Mozart"})
print(user_mozart)

# Close the MongoDB connection
client.close()
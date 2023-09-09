/**
	Title: berryhill-projections.js
    Author: Nolan Berryhill
    Date: 10 September 2023
    Description: MongoDB queries for the users collection
 */

// Add a new user
const newUser = {
    "firstName": "Bob",
    "lastName": "Builder",
    "employeeId": "1013",
    "email": "bobbuilder@mail.com",
    "dateCreated": new Date()
}

db.users.insertOne(newUser)

// Update Mozart's email address
db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@me.com" } }
)

// Verify that Mozart's email address was updated
db.users.find({ lastName: "Mozart" })

// List all documents in the user's collection with projections
db.users.find({}, { firstName: 1, lastName: 1, email: 1 })
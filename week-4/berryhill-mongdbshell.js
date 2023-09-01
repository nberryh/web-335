/**
	Title: berryhill-mongdbshell.js
    Author: Nolan Berryhill
    Date: 01 September 2023
    Description: MongoDB queries for the users collection
 */

// Display all documents in the users collection
db.users.find({})

// Find the user with an email address of jbach@me.com
db.users.find({"email": "jbach@me.com"})

// Find a user with the last name of Mozart
db.users.find({"lastName": "Mozart"})

// Find a user with a first name of Richard
db.users.find({"firstName": "Richard"})

// Find a user with a employeeId of 1010
db.users.find({"employeeId": "1010"})
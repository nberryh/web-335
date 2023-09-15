/**
	Title: berryhill-queries.js
    Author: Nolan Berryhill
    Date: 17 September 2023
    Description: MongoDB queries for the houses collection
 */

// Display all documents in the houses collection
db.houses.find({})

// Display all students in the houses collection
db.students.find({})

// Display add documents to the houses collection
const newStudent = {
    "firstName": "New",
    "lastName": "Student",
    "studentId": "s1019",
    "houseId": "h1007"
};

db.students.insertOne(newStudent);

// Delete a documents in the houses collection
db.students.deleteOne({ "studentId": "s1019" });

// Display all students from the houses collection
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseInfo"
        }
    },
    {
        $unwind: "$houseInfo"
    },
    {
        $project: {
            _id: 0,
            firstName: 1,
            lastName: 1,
            house: "$houseInfo.mascot"
        }
    }
]);

// Display all students from Gryffindor the houses collection
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseInfo"
        }
    },
    {
        $unwind: "$houseInfo"
    },
    {
        $match: {
            "houseInfo.mascot": "Loin"
        }
    },
    {
        $project: {
            _id: 0,
            firstName: 1,
            lastName: 1,
            house: "$houseInfo.mascot"
        }
    }
]);

// Display all students from Eagle mascot house from the houses collection
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "houseInfo"
        }
    },
    {
        $unwind: "$houseInfo"
    },
    {
        $match: {
            "houseInfo.mascot": "Eagle"
        }
    },
    {
        $project: {
            _id: 0,
            firstName: 1,
            lastName: 1,
            house: "$houseInfo.mascot"
        }
    }
]);
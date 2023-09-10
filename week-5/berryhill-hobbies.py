#-----------------------------------------------------
# Title: berryhill-hobbies.py
# Author: Nolan Berryhill
# Date: 10 September 2023
# Description: Exercise 5.3 
#-----------------------------------------------------

# List of hobbies
hobbies = ["Working out", "Video Games", "Watching Movies", "Reading", "Watching Tv Shows"]

# Print hobbies
print('My Hobbies:')
for hobby in hobbies:
    print("- " + hobby)

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Print day messages
print("\nDays of the Week:")
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: It is a day off and you should enjoy your hobbies!")
    else:
        print(f"{day}: It is a workday.")
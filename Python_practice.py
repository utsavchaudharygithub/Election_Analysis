# Create a variable called 'name' that holds a string
name = "utsav chaudhary"
# Create a variable called 'country' that holds a string
country = "United States"
# Create a variable called 'age' that holds an integer
age = 35
# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 15
# Calculate the daily wage for the user
daily_wage = hourly_wage * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = True
# Print out "Hello <name>!"
print("Hello " + name + "!")
# Print out what country the user entered
print("You live in " + country)
# Print out the user's age
print("You are " + str(age) + " years old")
# With an f-string, print out the daily wage that was calculated
print(f"You make {daily_wage} per day")
# With an f-string, print out whether the users were satisfied
print(f"Are you satisfied with your current wage? {satisfied}")

#----
#pet dictionary

#dictionary full of info
my_info= {"name": "bullet","age":3,
          "hobbies":["barking","eating", "sleeping", "loving my owner"
        ],
        "wake-up": {"Mon":5, "Friday":5, "saturday":7, "sunday": 7}}
#print out results stored in dictionary using f-strings.

print(f'Hello i am {my_info["name"]} and i am {my_info["age"]} years old.')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'One of my hobbies is {my_info["hobbies"][0]}.')
print(f'off saturday i get up at {my_info["wake-up"]["saturday"]} AM.')


#___

#_____
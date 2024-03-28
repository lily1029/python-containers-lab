# Exercise 1

# your solution here
students = ['Jack', 'Tom', 'Lucy', 'Liz', 'Mia']
print(students[1])
print(students[-1])


# Exercise 2

# your solution here
foods = ('pizza', 'bread', 'steak', 'bacon', 'hamburger')

for food in foods:
    print(f"{food} is a good food. ")


# Exercise 3

# your solution here
for food in foods[-2 : ]:
    print(food)


# Exercise 4

# your solution here
home_town = {
    'city': 'Sunnyvale',
    'state': 'CA',
    'population': '100 million'
}

print(f"I was born in {home_town['city']} ,{home_town['state']} - {home_town['population']} of population")
    

# Exercise 5

# your solution here: first way to write:
for key in home_town:
    print(f"{key} = {home_town[key]}")

#your solution here: sencond way to write:
for key, val in home_town.items():
    print(f"{key} = {val}")


# Exercise 6

# your solution here
cohort = []
#here use enumerate to get each student index and each student name in students list
for idx, student in enumerate(students):
    #here use .append()method to append the result in cohort list. 
    #put the result in a dictionary so it has key-value pairs
    cohort.append({'student': student, 'fav_food': foods[idx]})

#then, print the each student from cohort list as requested format
for student in cohort:
    print(student)


# Exercise 7

# your solution here

awesome_students = [student + ' is awesome!' for student in students]

for student in awesome_students:
    print(student)


# Exercise 8

# your solution here
#print food item for loop food in foods tuple if only if food item has 'a' in the food name. 
[print(food) for food in foods if 'a' in food]




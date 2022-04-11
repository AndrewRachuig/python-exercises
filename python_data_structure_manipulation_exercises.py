students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# 1. How many students are there?
print(f"There are {len(students)} students.\n")


# 2. How many students prefer light coffee? For each type of coffee roast?
print(f"There are {len([student for student in students if student['coffee_preference'] == 'light'])} "
      "students who prefer light coffee, "
      f"{len([student for student in students if student['coffee_preference'] == 'medium'])} "
      "students who prefer medium coffee, "
      f"and {len([student for student in students if student['coffee_preference'] == 'dark'])} "
      "students who prefer dark coffee.\n")


# 3. How many types of each pet are there?
#  Make a list of all pets owned by students.
pets_list = []
for student in students:
    for pet in student['pets']:
        pets_list.append(pet['species'])

# Make a dictionary which contains key:value of species:count
pet_dictionary = {x:pets_list.count(x) for x in pets_list}

# Display the count and species
for x in pet_dictionary:
    print(f"There are {pet_dictionary[x]} {x}s owned by students.")
print('\n')


# 4. How many grades does each student have? Do they all have the same number of grades?
grade_count = 0
grade_change = 0
for x in students:
    if len(x['grades']) > grade_count:
        grade_count = len(x['grades'])
        grade_change += 1
    print(f"{x['student']} has {grade_count} grades recorded.")

if grade_change > 1:
    print("\nThe students do not all have the same number of grades recorded.")
else:
    print(f"\nThe students all have {grade_count} grades recorded.\n")


# 5. What is each student's grade average?
from statistics import mean

for x in students:
    print(f"{x['student']}'s grade average is {mean(x['grades'])}.\n")


# 6. How many pets does each student have?
for x in students:
    if len(x['pets']) > 1:
        print(f"{x['student']} has {len(x['pets'])} pets.\n ")
    elif len(x['pets']) == 1:
        print(f"{x['student']} has 1 pet.\n ")
    else:
        print(f"{x['student']} has no pets.\n ")


# 7. How many students are in web development? data science?
web_dev_count = 0
ds_count = 0
for x in students:
    if x['course'] == "web development":
        web_dev_count += 1
    elif x['course'] == "data science":
        ds_count += 1
print(f"There are {web_dev_count} students in web development and {ds_count} students in data science.\n")


# 8. What is the average number of pets for students in web development?
webdev_pet_count = 0
for x in students:
    if x['course'] == "web development":
        webdev_pet_count += len(x['pets'])
print(f"The average number of pets for students in web development is {webdev_pet_count/web_dev_count}.\n")


# 9. What is the average pet age for students in data science?
ds_pet_count = 0
ds_pet_age = 0
for x in students:
    if x['course'] == 'data science':
        ds_pet_count += len(x['pets'])
        for x in x['pets']:
            ds_pet_age += x['age']
print(f"The average pet age for students in data science is {ds_pet_age/ds_pet_count}.\n")

# 10. What is most frequent coffee preference for data science students?
light_pref = 0
medium_pref = 0
dark_pref = 0
for x in students:
    if x['course'] == 'data science':
        if x["coffee_preference"] == 'light':
            light_pref += 1
        elif x["coffee_preference"] == 'medium':
            medium_pref += 1
        elif x["coffee_preference"] == 'dark':
            dark_pref += 1

if light_pref > medium_pref:
    if light_pref > dark_pref:
        print("The most frequent coffee preference for data science students is light coffee.\n")
    else:
        print("The most frequent coffee preference for data science students is dark coffee.\n")
else:
    if medium_pref > dark_pref:
        print("The most frequent coffee preference for data science students is medium coffee.\n")
    else:
        print("The most frequent coffee preference for data science students is dark coffee.\n")

# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?
# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
    # a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
        # DONE
    # b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

from function_exercises import calculate_tip

print(calculate_tip(.15, 50))

    # c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
    #  DONE

# 2. Read about and use the itertools module from the python standard library to help you solve the following problems:
import itertools as i
    # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
print("Question 2")
print(len(list(i.product('ABC', '123'))))

    # How many different combinations are there of 2 letters from "abcd"?
print(len(list(i.permutations('abcd', 2))))

    # How many different permutations are there of 2 letters from "abcd"?
print(len(list(i.combinations('abcd', 2))))

#3. Save and import json file
import json
user_info = json.load(open('profiles.json'))


# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

    # Total number of users
print(f"There are {len(user_info)} users in the json import file list.")

    # Number of active users
active_list = 0
for x in user_info:
    if x["isActive"]:
        active_list += 1
print(f"There are {active_list} active users in the json import file list.")

    # Number of inactive users
inactive_list = 0
for x in user_info:
    if not x["isActive"]:
        inactive_list += 1
print(f"There are {inactive_list} inactive users in the json import file list.")

    # Grand total of balances for all users
total_balance = 0
for x in user_info:
   user_balance = (x['balance'])[1:].replace(',', '')
   user_balance = float(user_balance)
   total_balance += user_balance

print(f"The total balance for all the users is ${total_balance}.")

    # Average balance per user
print(f"The average balance per user is ${round(total_balance / len(user_info), 2)}")

    # User with the lowest balance
balance_sheet = {}
for x in user_info:
    balance_sheet[x['_id']] = x['balance']

lowest_balance = min(balance_sheet.values())
lowest_balance_user = str()
for x in balance_sheet:
    if balance_sheet[x] == lowest_balance:
        lowest_balance_user = x

print(f"The user with the lowest balance is user id {lowest_balance_user}")
    # User with the highest balance
highest_balance = max(balance_sheet.values())
highest_balance_user = str()
for x in balance_sheet:
    if balance_sheet[x] == highest_balance:
        highest_balance_user = x

print(f"The user with the highest balance is user id {highest_balance_user}")

    # Most common favorite fruit
fruit_list =[]
fruit_list = [x['favoriteFruit'] for x in user_info]
fruit_count = {}
fruit_count = {x: fruit_list.count(x) for x in fruit_list}

most_quantity  = max(fruit_count.values())
most_fruit_name = ()
for x in fruit_count:
    if fruit_count[x] == most_quantity:
        most_fruit_name = x

print(f"The most common favorite fruit is {most_fruit_name}.")

    # Least most common favorite fruit
least_quantity  = min(fruit_count.values())
least_fruit_name = ()
for x in fruit_count:
    if fruit_count[x] == least_quantity:
        least_fruit_name = x

print(f"The least common favorite fruit is {least_fruit_name}.")

    # Total number of unread messages for all users
import re
total_unread = 0
for x in user_info:
    total_unread += int(re.findall('[0-9]+', x['greeting'])[0])

print(f"There are {total_unread} unread messages for all users.")

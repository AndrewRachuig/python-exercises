#1.Conditional Basics
#
# a. prompt the user for a day of the week, print out whether the day is Monday or not
print("1. Conditional Basics: part a")
if input("What day is today? ").lower() == 'monday':
    print("Today is monday.")
else:
    print("Today is not monday.")


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
print("Conditional Basics: part b")
if input("What day is today? ").lower() in ['saturday', 'sunday']:
    print("Today is a weekend day.")
else:
    print("Today is a weekday.")

# c. create variables and make up values for
#   the number of hours worked in one week
print("Conditional Basics: part c")
hours_worked = 45
#   the hourly rate
hourly_rate =  20
#   how much the week's paycheck will be
paycheck = None
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
if hours_worked > 40:
    paycheck = (40 * hourly_rate) + ((hours_worked -40) * (hourly_rate * 1.5))
else:
    paycheck = (hours_worked * hourly_rate)
print("The paycheck is", paycheck)

# 2. Loop Basics
print("Loop Basics: part a, less than 15 loop")
#   a.While
#   Create an integer variable i with a value of 5.
i = 5
#   Create a while loop that runs so long as i is less than or equal to 15
#   Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

    # Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
print("Loop Basics: part a, count by 2's loop")
new_var = 0
while new_var < 100:
    new_var += 2
    print(new_var, '\n')

    # Alter your loop to count backwards by 5's from 100 to -10.
print("Loop Basics: part a, countdown by 5's loop")
while new_var >= -10:
    print(new_var, '\n')
    new_var -= 5

    # Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
print("Loop Basics: part a, square to 1 million")
square_var = 2
while square_var < 1000000:
    print(square_var)
    square_var **= 2

    # Write a loop that uses print to create the output shown below.
print("Loop Basics: part a, countdown from 100 by 5's loop again")
var_hundred = 100
while var_hundred > 0:
    print(var_hundred)
    var_hundred -= 5

    # b. For Loops
print("Loop Basics: part b, multiplication table")
        # i.Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
number_choice = input("Please input a number: ")

for n in range(1, 11):
    print(f"{n} * {number_choice} = {n * number_choice}")
    # For example, if the user enters 7, your program should output:

        # ii. Create a for loop that uses print to create the output shown below.
print("Loop Basics: part b, number * itself length loop")
for n in range(1, 10):
    print(f'{n}' * n)

    # c.break and continue
print("Loop Basics: part c")
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

odd_choice = None
while odd_choice == None:
    odd_choice = input("Please select an odd number between 1 and 50: ")
    if odd_choice.isdigit() and int(odd_choice) > 1 and int(odd_choice) < 50 and (int(odd_choice) % 2 == 1):
        break
    else:
        print("Not a valid input.")
        odd_choice = None
        continue
index = 1
while index < 50:
    if int(odd_choice) == index:
        print(f"Yikes! Skipping number: {odd_choice}")
    else:
        print(f"Here is an odd number: {index}")
    index += 2

    # d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
print("Loop Basics: part d")
while True:
    try:
        pos_choice = int(input("Please input a positive number"))
        if pos_choice > 0:
            break
        else:
            continue
    except ValueError:
        continue
count_index = 0
while count_index <= pos_choice:
    print(count_index)
    count_index += 1

    # e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
print("Loop Basics: part e")
while True:
    try:
        pos_choice = int(input("Please input a positive number"))
        if pos_choice > 0:
            break
        else:
            continue
    except ValueError:
        continue
while pos_choice > 0:
    print(pos_choice)
    pos_choice -= 1

# 3. Fizzbuzz
print("Question 3: Fizzbuzz")
    # Write a program that prints the numbers from 1 to 100.
    # For multiples of three print "Fizz" instead of the number
    # For the multiples of five print "Buzz".
    # For numbers which are multiples of both three and five print "FizzBuzz"
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 4. Display a table of powers.
print("Question 4: Table of powers")
    # Prompt the user to enter an integer.
    # Display a table of squares and cubes from 1 to the value entered.
    # Ask if the user wants to continue.
    # Assume that the user will enter valid data.
    # Only continue if the user agrees to.
user_int = int(input("What number would you like to go up to? "))
while True:
    if input("Do you want to continue?  yes or no ").lower() == 'yes':
        break
    else:
        continue
print("Here is your table!\n")
print("number | squared | cubed")
print("------ | ------- | -----")

index = 1
while index <= user_int:
    print(f'{index}      |', f'{index ** 2}', ' ' * (6 - len(str(index ** 2))), f'| {index ** 3}')
    index += 1



# 5.Convert given number grades into letter grades.
print("Question 5: Converting number grades")
    # Prompt the user for a numerical grade from 0 to 100.
    # Display the corresponding letter grade.
    # Prompt the user to continue.
    # Assume that the user will enter valid integers for the grades.
    # The application should only continue if the user agrees to.
while True:
    numerical_grade = int(input("Please enter a grade from 0 to 100: "))
    if numerical_grade >= 88:
        if numerical_grade >= 99:
            print("This is an A+")
        elif numerical_grade >= 93:
            print("This is an A")
        else:
            print('This is an A-')
    elif numerical_grade >= 80:
        if numerical_grade > 87:
            print("This is a B+")
        elif numerical_grade >83:
            print("This is a B")
        else:
            print("This is a B-")
    elif numerical_grade >= 67:
        if numerical_grade > 76:
            print("This is a C+")
        elif numerical_grade > 70:
            print("This is a C")
        else:
            print("This is a C-")
    elif numerical_grade >= 60:
        if numerical_grade > 65:
            print("This is a D+")
        elif numerical_grade > 63:
            print("This is a D")
        else:
            print("This is a D-")
    else:
        print("This is an F")

    if input("Would you like to continue? yes or no? ").lower() == 'yes':
        break


# 6. Create a list of dictionaries where each dictionary represents a book that you have read.
print("Question 6: Book dictionaries")
# Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
book_dict = dict(
    title=["Foundation", "Lord of the Rings", "Hyperion", "The Player of Games", "The Girl With the Dragon Tattoo",
           "Ender's Game"],
    author=["Isaac Asimov", "J.R.R. Tolkien", "Dan Simmons", "Iain M. Banks", "Stieg Larsson", "Orson Scott Card", ],
    genre=["Science Fiction", "Fantasy", "Science Fiction", "Science Fiction", "Mystery", "Science Fiction"])


for i in range(len(book_dict['title'])):
    print(f"\nBook #{i + 1}")
    for key in book_dict:
        print(book_dict[key][i])
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

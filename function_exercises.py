# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(a):
    if int(a) == 2:
        return True
    else:
        return False


print(is_two(2))
print(is_two('2'))
print(is_two(3))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
import re
def is_vowel(a):
    if re.search('[aeiou]', a):
        return True
    else:
        return False


print(is_vowel('a'))
print(is_vowel('e'))
print(is_vowel('d'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(a):
    if not is_vowel(a):
        return True
    else:
        return False


print(is_consonant('a'))
print(is_consonant('e'))
print(is_consonant('d'))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_string(a):
    first_letter = a[0]
    if is_consonant(first_letter):
        return a.capitalize()
    else:
        return "Word does not start with a consonant."


print(cap_string('test'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip, bill_total):
    return tip * bill_total


print(calculate_tip(.13, 25))


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount):
    return original_price * (1 - (discount/100))


print(apply_discount(100, 25))


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number_string):
    return int(number_string.replace(",", ""))


print(handle_commas('123,345,567'))
print(type(handle_commas('123,345,567')))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 65:
        return 'D'
    else:
        return 'F'


print(get_letter_grade(91))
print(get_letter_grade(76))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word_in):
   remaining_letters = [x for x in word_in if is_consonant(x)]
   return ''.join(remaining_letters)


print(remove_vowels("testing"))


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed
def normalize_name(inputstring):
    inputstring = inputstring.lower()
    while True:
        if inputstring[0].isdigit():
            inputstring = inputstring[1:]
            continue
        elif not re.search('[a-z0-9]', inputstring[0]):
            inputstring = inputstring[1:]

            continue
        else:
            break
    inputstring = inputstring.strip()
    inputstring = inputstring.replace(' ', '_')

    return inputstring


print(normalize_name('Big Cat 02'))
print(normalize_name('023 Coke lover 1'))
print(normalize_name('% Completed'))


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
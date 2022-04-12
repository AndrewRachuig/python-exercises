# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(a):
    return int(a) == 2

print("\nQuestion 1: Is it two? '2', 'str(2)', '3'")
print(is_two(2))
print(is_two('2'))
print(is_two(3))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
import re
def is_vowel(a):
    return bool(re.search('[aeiou]', a))

print("\nQuestion 2: Is a string a vowel? 'a', 'e', 'd' ")
print(is_vowel('a'))
print(is_vowel('e'))
print(is_vowel('d'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(a):
    return not is_vowel(a)

print("\nQuestion 3: Is it a consonant? 'a', 'e', 'd'")
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

print("\nQuestion 4: Capitalize the first letter: 'test'")
print(cap_string('test'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip, bill_total):
    return tip * bill_total

print("\nQuestion 5: Calculate tip: tip = .13, bill = 25")
print(calculate_tip(.13, 25))


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount):
    return original_price * (1 - (discount/100))

print("\nQuestion 6: Apply a discount: original price = 100, discount = 25%")
print(apply_discount(100, 25))


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number_string):
    return int(number_string.replace(",", ""))

print("\nQuestion 7: handle commas function; input: '123,345,567' and shows what 'type' the output is")
print(handle_commas('123,345,567'))
print(type(handle_commas('123,345,567')))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    grade = float(grade)
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

print("\nQuestion 8: Get letter grade: 91, 76")
print(get_letter_grade(91))
print(get_letter_grade(76))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word_in):
   remaining_letters = [x for x in word_in if is_consonant(x)]
   return ''.join(remaining_letters)

print("\nQuestion 9: Remove vowels function, input: 'testing'")
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
    inputstring = inputstring.strip().replace(' ', '_')
    return inputstring

print("\nQuestion 10: Normalize name function, input: 'Big Cat 02', '023 Coke lover 1', '% Completed'")
print(normalize_name('Big Cat 02'))
print(normalize_name('023 Coke lover 1'))
print(normalize_name('% Completed'))


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(some_list):
    newlist = []
    for x in some_list:
        try:
            newlist.append(x + newlist[-1])
        except IndexError:
            newlist.append(x)
    return newlist

test_list = [1, 2, 3, 4]
test_list2 = [1, 1, 1]

print("\nQuestion 11. Cumulative sum from list: [1, 2, 3, 4], [1, 1, 1]")
print(cumulative_sum(test_list))
print(cumulative_sum(test_list2))

# Bonus
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.
def twelveto24(timein):
    if 'pm' in timein:
        time_out = timein.replace('pm', '')
        time_out = float(time_out.replace(':', '.'))
        time_out += 12
        time_out = str(time_out)
        time_out = time_out.replace('.', ':')
        if len(time_out) < 5:
            time_out += '0'
        return time_out
    else:
        time_out = timein.replace('am', '')
        return time_out

print("\nBonus Question1: twelveto24 time, input: '4:30am', '4:35am', '11:30am', '11:35am', '4:30pm', '4:35pm', '11:30pm', '11:35pm'")
print(twelveto24('4:30am'))
print(twelveto24('4:35am'))
print(twelveto24('11:30am'))
print(twelveto24('11:35am'))
print(twelveto24('4:30pm'))
print(twelveto24('4:35pm'))
print(twelveto24('11:30pm'))
print(twelveto24('11:35pm'))





# Bonus write a function that does the opposite.
def twentyfourto12(timein):
    time_out = float(timein.replace(':', '.'))
    if time_out < 13:
        time_out = str(time_out).replace('.', ':')
        if re.search(':[0-9]$', time_out):
            time_out += '0'
        time_out += 'am'
        return time_out
    else:
        time_out = round(time_out - 12, 2)
        time_out = str(time_out).replace('.', ':')
        if re.search(':[0-9]$', time_out):
            time_out += '0'
        time_out += 'pm'
        return time_out

print("\nBonus Question 1 Bonus: twentyfourto12 input: '7:30', '7:35', '12:30', '12:35', '13:30', '13:35', '22:30', '22:35'")
print(twentyfourto12('7:30'))
print(twentyfourto12('7:35'))
print(twentyfourto12('12:30'))
print(twentyfourto12('12:35'))
print(twentyfourto12('13:30'))
print(twentyfourto12('13:35'))
print(twentyfourto12('22:30'))
print(twentyfourto12('22:35'))


# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27
def col_index(col_name):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    sum_total = 0
    col_name = col_name[::-1]
    for x in range(0, (len(col_name))):
        position = (alphabet.index(col_name[x]) + 1)
        if x == 0:
            sum_total += position
        else:
            sum_total += (26 ** x * (position))
    return sum_total

print("\nBonus Question 2: col_index, input: 'A', 'AB', 'ZA', 'ABC', 'XYZ', 'AKDK'")

print(col_index('A'))
print(col_index('AB'))
print(col_index('ZA'))
print(col_index('ABC'))
print(col_index('XYZ'))
print(col_index('AKDK'))

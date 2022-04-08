# 1. Movie rental price
little_mermaid = 3
brother_bear = 5
hercules = 1
total_cost = 3 * (little_mermaid + brother_bear + hercules)
print(f"Number 1\nThe total price for the movie rental is ${total_cost}.")

# 2. Company contractor payment
google_pay_rate = 400
amazon_pay_rate = 380
facebook_pay_rate = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10
total_pay = (google_hours * google_pay_rate) + (amazon_hours * amazon_pay_rate) + (facebook_hours * facebook_pay_rate)
print(f"\nNumber 2\nThe total pay earned this week is ${total_pay}.")

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_not_full = True
schedule_does_not_conflict = True

can_be_enrolled  = class_not_full and schedule_does_not_conflict
print("\nNumber 3\nEnrollment is possible?", can_be_enrolled)

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
premium_member = False
items_purchased = 11
offer_expired = False

if premium_member:
    gets_offer = True
else:
    if items_purchased > 2 and not offer_expired:
        gets_offer = True
    else:
        gets_offer = False
print("\nNumber 4\nReceives offer?", gets_offer)


# 5.
username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

password_length = (len(password) >= 5)
username_length = (len(username) <= 20)
pass_is_not_user = (password != username)
no_whitespace = ((username, password).count(' ') == 0)


print(f"\nNumber 5\nThe password is {password_length} characters.\nThe username is {username_length} characters.")
print(f"The password and username do not match? {pass_is_not_user}\nNeither the password nor the username contain with whitespace? {no_whitespace}")

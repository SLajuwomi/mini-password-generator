import random 
import string

def generate_password(min_length, numbers=True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters

  if numbers:
    characters += digits
  if special_characters:
    characters += special

  pwd = ''
  meets_criteria = False
  has_number = False
  has_special = False

  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True

    meets_criteria = True

    if numbers:
      meets_criteria = has_number
    if special_characters:
      meets_criteria = meets_criteria and has_special

  return pwd

def check_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)

    strength_score = sum([length_criteria, digit_criteria, special_criteria, uppercase_criteria, lowercase_criteria])
    
    if strength_score == 5:
        return "Strong"
    elif strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"

min_length = int(input("Enter the minimun length: "))
has_number = input("Do you want to have numbers (y/n)  ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)  ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
strength = check_password_strength(pwd)

print("The generated password is: " + pwd)
print("Password strength:", strength)


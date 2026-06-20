import re
def validate_email(email):
    pattern=r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$"
    if re.fullmatch(pattern,email):
        return True
    return False
def validate_phone(number):
    conditions=[(11,"09"),(13,"+989"),(14,"00989")]
    for length,prefix in conditions:
      if len(number)==length and number.startswith(prefix):
        return True
      return False
print("Hello! Welcome to the Paython Validator!")
user_email = input()
user_phone = input()
print(f"{validate_email(user_email)}")
print(f"{validate_phone(user_phone)}")

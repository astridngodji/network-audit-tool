import argparse

#checks the lenght of password
def checkLength(password):
    if len(password) < 8:
        return "Minimum of 8 characters"

#checks if there is an uppercase letter
def checkUppercase(password):
    if not any(char.isupper() for char in password):
        return "At least one Uppercase letter"

#check if there is a number
def checkNumber(password):
    if not any(char.isdigit() for char in password):
        return "At least one number"

#check if there is a special character
def checkSpecialChar(password):
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if not any(char in special_chars for char in password):
        return "At least one Special Character"

def main():
    parser = argparse.ArgumentParser(description="Python Password Strength Checker")
    parser.add_argument("password", help="Type a password")
    args = parser.parse_args()

    password = args.password

    errors = []
    for check in [checkLength, checkUppercase, checkNumber, checkSpecialChar]:
        result = check(password)
        if result:
            errors.append(result)
    if errors:
        print("Password is weak:")
        for err in errors:
            print(f"- {err}")
    else:
        print("Password is strong")
    

if __name__ == "__main__":
    main()

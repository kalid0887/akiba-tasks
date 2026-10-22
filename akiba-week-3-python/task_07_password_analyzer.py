password = input("enter the password: ")


def min_lenght(password):
    if len(password) < 8:
        return False
    else:
        return True

def is_include_uppercase(password):
    for char in password:
        if char.isupper():
            return True


    return False

def is_include_lowercase(password):
    for char in password:
        if char.islower():
            return True


    return False

def is_include_digits(password):
    for char in password:
        if char.isdigit():
            return True


    return False

def is_include_specialCharacters(password):
    for char in password:
        if not char.isalnum():
            return True


    return False

def analyze_password(password):
    if is_include_lowercase(password) and is_include_digits(password) and is_include_specialCharacters(password) and is_include_uppercase(password) and min_lenght(password):
        print("corrected password")
    else:
        if not is_include_uppercase(password):
            print("ur password not includes uppercase letters")
        if not is_include_specialCharacters(password):
            print("ur password not includes special characters")
        if not is_include_digits(password):
            print("ur password not includes digits")
        if not is_include_lowercase(password):
            print("ur password not includes lowercase letters")
        if not min_lenght(password):
            print("ur passwords lenght is lessthan the required length")
       


if __name__ == "__main__":
    analyze_password(password)
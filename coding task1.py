def check_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if has_lower and has_upper and has_digit:
        return True
    else:
        return False

password = input("Enter a password to check: ")
if check_password(password):
    print("Password is valid!")
else:
    print("Hence, password is invalid.")

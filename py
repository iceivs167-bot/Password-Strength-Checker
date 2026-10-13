while True:
    password = input("Create Password: ")
    length = len(password)
    uppercase = 0
    lowercase = 0
    Number = 0
    Special = 0

    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            Number += 1
        else:
            Special += 1

    if length < 6:
        print("Password too short")
    elif uppercase < 1:
        print("Need an uppercase")
    elif lowercase < 1:
        print("Need a lowercase")
    elif Number < 1:
        print("Need a number")
    elif Special < 1:
        print("Need a special character")
    else:
        print("Password is strong")
        break

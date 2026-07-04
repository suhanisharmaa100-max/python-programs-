#Write a login check using nested if statement: first check if the username matches "admin", and only if it does, check if the password matches "1234". Print "Access granted", "Wrong password", or "Unknown user" accordingly.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
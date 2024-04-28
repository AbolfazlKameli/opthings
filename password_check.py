def authenticate():
    username = "user13245"
    password = "pass13245"
    max_attempts = 3

    for i in range(max_attempts):
        i_username = input("Enter your username: ")
        i_password = input("Enter your password: ")
        if i_username == username and i_password == password:
            print(f"Welcome {i_username}")
            break
        else:
            print("Wrong username or password, try again!")
    else:
        print("you have exceeded 3 attempts!")


authenticate()

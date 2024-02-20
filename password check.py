a = 0


def login(user, password):
    if user == "username" and password == "password":
        print("wellcome")
    else:
        global a
        a += 1
        if a <= 3:
            print(f"try again, you enter the username or password {a} wrong")
            login(input("username: "), input("password: "))


login(input("username: "), input("password: "))

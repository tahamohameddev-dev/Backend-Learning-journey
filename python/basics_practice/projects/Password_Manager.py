# create Password Manager use python

password_manager = {}

def add_pass():
    user = input("Enter your user_name: ")
    password = input("Enter Your password: ")
    password_manager[user] = password
    print("Account created successfully!")

def login():
    user = input("Enter your user_name: ")
    password = input("Enter your password for login: ")
    if user in password_manager and password_manager[user] == password:
        print("login successfully!")
    else:
        print("Incorrect username or password")


def main():
    while True:
        ichoice = input("Enter the choice '1' for add pass '2' for login '0' for Exit: ")
        if ichoice == "1":
            add_pass()
        elif ichoice == "2":
            login()
        elif ichoice == "0":
            break
        else:
            print("Envallid choice")

if __name__=="__main__":
    main()
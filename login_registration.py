
def welcome():
    print("\n\tYou've Completed Your 1st TASK...!\n\n\tCongrats.............!")


def Forget_password(username=None):
    Username = str(input("Enter your username:"))

    if not len(Username ) < 1:

        # noinspection PyUnreachableCode
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))

            if Username in d:

                print("\nYour password is: ", f[d.index(Username)])
            else:
                print("\nUsername not Exist,  Plz Register\n\n")
                registration()
        else:
            pass

def login(username=None,password=None):
    Username = input("Enter your UserName:")
    Password = input("Enter your PassWord:")

    if not len(Username or Password) < 1:

        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))
            try:
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                            print("\n\nLogin success...!\n\n")
                            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
                            print("Hi ", Username,',')
                            welcome()
                        else:
                            print("Incorrect PassWord or UserName")
                            print("Plz Register")
                            print("      or")
                            print("Plz select Forgot PassWord")

                            Home_page()
                    except:
                        print("Incorrect PassWord or UserName")
                        print("Plz Register")
                        print("      or")
                        print("Plz Select Forgot PassWord")
                        Home_page()


                else:
                    print("PassWord or UserName doesn't exist")
                    print("Plz Register")
                    print("      or")
                    print("Plz Select Forgrt PassWord")
                    Home_page()
            except:
                print("PassWord or UserName doesn't Exist")
                Home_page()
    else:
        print("Plz attempt LogIn again")
        login()

    pass

def registration(username=None,password=None,password1=None):
    print('UserName Must be your E-mail, Do not make Errors')
    username=input("Create Username       : ")
    print('Password must be Minimum One Upper, Lower, Number and Spl char')
    password=input("Create Password       : ")
    password1=input("Re_enter Your Password: ")
    db=open("database.txt","r")
    v=[]
    for x in db:
        a,b= x.split(",")
        b=b.strip()
        c=a,b
        v.append(a)
    if password1 != password:
        print("PassWord was Not Match")
        registration()
    elif len(password) < 5:
        print("PassWord is too short")
    elif len(password) > 16:
        print("PassWord is too long")

    else:
        valid = 0
        user = []
        if username[0].isalpha():
            if "@." not in username:
                if "@" in username:
                    if "." in username:
                        user.append(username)
                else:
                    pass
            else:
                print("Invalid UserName")
        else:
            print("Invalid UserName")

        if len(user) > 0:
            if username not in v:
                valid = valid + 1
                pass
            else:
                print("UserName already exist")
                registration()

        u, l, d, s = 0, 0, 0, 0
        for x in password:
            if x.isdecimal():
                d = 1
            if x.upper() in password:
                u = 1

            if x.lower() in password:
                l = 1

            if x == "@" or x == "$" or x == "_":
                s = 1
        if u == 1 and l == 1 and d == 1 and s == 1:

            valid = valid + 1
        else:
            print("Invalid PassWord")

        if valid == 2:

            with open("database.txt", "a") as db:
                db.write(username + ", " + password1 + "\n")
                print('\n\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print("~~~~~~~~~ REGISTRATION SUCESSFULL ~~~~~~~~~~")
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            Home_page()
        else:
            print("Plz try again")
            registration()

def Home_page(option=None):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print("~~~~~~ LogIn / Registration Page ~~~~~~~")
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    option=input(" 1.Registration: \n 2.LogIn: \n 3.Forget_password: \n 4.Exit \n Select Any Option Above Mentioned: ")
    if option=="1":
        registration()
    elif option=="2":
        login()
    elif option=="3":
        Forget_password()
    elif option=="4":
        print("Thank You...")
        exit()
    else:
        print("Invalid Option")
        Home_page()
Home_page()





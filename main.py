# PAYMENT APP PROTO PROJECT
# back end
global currunt_bal
currunt_bal = 0


def user_sign_in():
    """Function to get user information to create account for sign in"""
    global username  # global ver for use it in all functions
    global emailid
    global D_O_B
    global user_middle_name
    global password
    global user_full_name
    # get input from user
    user_first_name = input("Entre First Your Name: ").title()
    user_middle_name = input("Entre Middle Your Name: ").title()
    user_sur_name = input("Entre Your SurName: ").title()
    emailid = input("Entre Your Email id name: ")

    while True:
        username = input("Create Your User name: ")
        if username.isalnum():
            break
        else:
            print("please entre only alphabets and numbers don't use spacial characters")
    D_O_B = input("Entre your dob dd/mm/yyyy: ")
    while True:
        password = input("Create Your Password: ")
        password_c = input("Entre Password again: ")
        if password == password_c:
            break
        else:
            print("password and entered Conform password not matching entre again")
    space = " "
    user_full_name = (user_first_name + space + user_middle_name + space + user_sur_name)
    print("Your Account is successfully created")
    main1()  # giving sign in and log in menu to user


def user_login():
    """Function to get log in userid and password from user and if its match to sign in info user will get loged in"""
    while True:  # while loop to get correct input from user
        Username_login = input("Entre Your User name: ")
        Password_login = input("Entre Your Password: ")
        # checking username and password is valid or not
        if Username_login == username and Password_login == password:
            print(F' login successful Welcome {user_full_name}')
            break  # break while loop if condition match
        else:
            print("check Userid and password again")
    main2()


def add_money():
    """Function to add money in PKPAY wallet"""
    global currunt_bal
    print(f'Your current bal of \n {currunt_bal}')  # showing balance to user
    add = int(input("Entre ammount to add in your account"))  # input from user to add ammount
    currunt_bal = currunt_bal + add
    print("1.main menu \n2.Log out")
    geti = int(input("Entre Your Choice = \n"))
    if geti == 1:
        main2()
    elif geti == 2:
        LOGOUT()


def recharge():
    """Function to Recharge sim from  PKPAY wallet"""
    global currunt_bal
    while True:  # while loop for get correct number input from user
        M_N = input("input mobile number +91-")
        if len(M_N) == 10:
            break
        else:
            print("Entre valid 10 digit mobile number")
    Am = int(input("Entre recharge plan amt = "))
    if Am < currunt_bal:  # check for recharge amount is less than wallet amount
        currunt_bal = currunt_bal - Am
        print("Recharge done")
        print(f"current balance {currunt_bal} \n")
    else:
        print("LOW BALANCE PLEASE ADD MONEY IN YOUR ACCOUNT PLEASE TO PROCEED")
    print("1.main menu \n2.Log out")
    geti = int(input("Entre Your Choice = \n"))
    if geti == 1:
        main2()
    elif geti == 2:
        LOGOUT()


def money_tr():
    """Function to money transfer from  PKPAY wallet"""
    global currunt_bal
    while True:  # while loop for get correct number input from user
        M_N = input("input mobile number of receiver  +91 ")
        if len(M_N) == 10:
            break
        else:
            print("Entre valid 10 digit mobile number \n")
    Am = int(input("Entre  amt = \n"))
    if Am < currunt_bal:  # check for recharge amount is less than wallet amount
        currunt_bal = currunt_bal - Am
        print("Transfer done")
        print(f"current balance {currunt_bal} \n ")
    else:
        print("LOW BALANCE PLEASE ADD MONEY IN YOUR ACCOUNT PLEASE TO PROCEED")
    print("1.main menu \n2.Log out")
    geti = int(input("Entre Your Choice = \n"))
    if geti == 1:
        main2()
    elif geti == 2:
        LOGOUT()


def LOGOUT():
    """ function to log out from account"""
    print(f"Thank you for using PKPAY  {user_full_name} \nplease write feedback for us")
    fed = input()  # feedback input
    main1()  # showing log in screen


def main1():
    """ function for menu to show on screen before log in"""
    print("1.Create account \n2.Login into Your Account")
    while True:
        inpM = input("entre choice = \n")
        if inpM == "1":
            user_sign_in()
        elif inpM == "2":
            user_login()
        else:
            print("please Entre Correct input")


def main2():
    """ function for menu to show on screen after log in"""
    print("1.Check current Balance \n2.Add money \n3.Recharge Sim card \n4.Money Transfer \n5.log out")
    while True:
        inpM1 = input("entre choice =\n")
        if inpM1 == "1":
            add_money()
        elif inpM1 == "2":
            add_money()
        elif inpM1 == "3":
            recharge()
        elif inpM1 == "4":
            money_tr()
        elif inpM1 == "5":
            LOGOUT()
        else:
            print("please Entre Correct input =\n")


# front end

print("_______________Welcome To PKPAY_______________")
main1()

#Retrieve user's username
print('Please put in a username of your choice:')
username = input('=> ')


#Verify password
def accept_input():
    global password
    global confirm_password
    global confirm_new_password
    global usercode
    global reconfirmed_password

    #importing function such as random and string to enable random codes 
    import random
    import string

    print('Please enter in a password of your choice: ')
    password = input("=> ")
    print('Please confirm password of your choice: ')
    confirm_password = input("=> ")
    usercode = random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)
    usercode = 'EB-' + ''.join(usercode)

    if password == "":
        print("Put in a password")
        accept_input()

    elif confirm_password == password:
        print(f"Password Verified and your usercode is '{usercode}' \n ALERT!(Save your usercode you will need it when loginning into your account)")
        
        return 
    else:   
        print("ALERT!(LAST TRIAL, Please put in a correct password)")
        reconfirmed_password = input("=> ")

        if reconfirmed_password == password:
            print(f"Password Verified and your usercode is '{usercode}' \n ALERT!(Save your usercode you will need it when loginning into your account)")
            return 
        else:
            print('Try a new password')
            new_password = input("=> ")
            global confirm_new_password
            print("Please confirm the new password: ")
            confirm_new_password = input("=> ")
            if new_password == confirm_new_password:
                print(f"Password Verified and your usercode is '{usercode}' \n ALERT!(Save your usercode you will need it when loginning into your account)")
                return 
            else:
                accept_input()



def display_userinfo():
    #Accept input from users
    print("Please put in your user name:")
    display_username = input('=> ') 
    print("Please put in your password: ")
    display_pasword = input('=> ')
    print("Please put in your usercode: ")
    display_usercode = input('=> ')

    #Checking if the diplay username is equal to username and display password is equal to password
    if display_username == username and (display_pasword == confirm_password or confirm_new_password or password or reconfirmed_password) and display_usercode == usercode:
        print(f"The account with the user name '{username}' has been validated and has the following details \nUsername: {username}\nUsercode: {usercode}")
    else: 
        print("Invalid username or password or usercode")
        display_userinfo()
 

accept_input()        
display_userinfo()




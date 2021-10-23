#!/usr/bin/env python3.6
from user import User
from credentials import Credential
from termcolor import colored
from tabulate import tabulate


def logo():
	print(colored("        ____                      _                     _   _     ","green"))
	print(colored("       |  _ \                    | |                   | | / /    ","green"))
	print(colored("       | |_) )  ____  ___   ___  | |      ___      ___ | |/ /     ","green"))
	print(colored("       |  __/  / _  |/ __  / __  | |     / __ \  /  _  |   (      ","green"))
	print(colored("       | |    / (_| |\__ \ \__ \ | |___ | (__) ||  (_  | |\ \     ","green"))
	print(colored("       |_|    \_____| ___/  ___/ |_____| \___ /  \ ___ |_| \_\    ","green"))
	print('\n')
	print(colored("*"*75,"red"))

 
logo()

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()
    
def user_verification(username,password):
    '''
    Function to verify if user details are correct
    '''
    return User.user_verification(username,password)

def create_credential(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,username,password)
    return new_credential

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    return credentials.save_credential()

def  find_credential(account):
    '''
     Function that finds a credential by account
    '''
    return Credential.find_by_account(account)

def check_credential_exist(account):
    '''
    Function that checks if a credential exists with that account 
    '''
    return Credential.credential_exist(account)

def display_credential():
    '''
    Function that displays all the saved credentials
    '''
    return Credential.display_credential()

def generate_password(password_length):
    '''
    Function that generates a random password 
    '''
    password = Credential.generate_password(password_length)

    return password  

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def main():
    print('\n')
    print("Welcome to Password Locker. Please input one of the short codes to navigate.")
    # print('\n')
    # while True:
    
        
       
    # while True:
    data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("su","yellow"), "Sign up to create your password locker account"], [colored("lg","yellow"),"Have an account already, log in to your account"],[colored("ex","yellow"),"Exit Password Locker"]]
    print(tabulate(data, headers='firstrow',tablefmt="grid"))
    short_code = input().lower()
    if short_code =="su":
            print(colored("Sign up......","green"))
            print("Enter username")
            username = input()
            print("Enter password")
            password = input()
            save_user(create_user(username,password))
            
            print('\n')
            print(colored(f"Your account has been successfully created!!","yellow"))
            print('\n')
            
            print(colored("Please log in to your account to continue......","green"))
            # print(colored("Log in......","green"))
            print("Enter username")
            username = input()
            print("Enter password")
            password = input()
            if user_verification(username,password):
                print(colored(f"Hi {username}, What would you like to do?","yellow"))
                print('\n')
                  
                data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("cc","yellow"), "Create new credential"],[colored("fd","yellow"),"Find credentials"],[colored("dc","yellow"),"Display credentials"],[colored("dl","yellow"),"Delete credentials"],[colored("ex","yellow"),"Exit Password Locker"]]
                print(tabulate(data, headers='firstrow',tablefmt="grid"))

            else: 
                print(colored("Incorrect username or password.Please try again or sign up","red"))
                print('\n') 
            
        # elif short_code =="ex":
        #     print("*"*30)
        #     print("logging out...")
        #     print('\n')
        #     print("*"*30)
        #     print("Bye .......")
        #     break
    # elif short_code =="lg": 
    #         print(colored("Log in......","green"))
    #         print("Enter username")
    #         username = input()
    #         print("Enter password")
    #         password = input()
    #         if user_verification(username,password):
    #             while True:
    #                 print(colored(f"Hi {username}, What would you like to do?","yellow"))
    #                 print('\n')
    #                 data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("cc","yellow"), "Create new credential"],[colored("fd","yellow"),"Find credentials"],[colored("dc","yellow"),"Display credentials"],[colored("dl","yellow"),"Delete credentials"],[colored("ex","yellow"),"Exit Password Locker"]]
    #                 print(tabulate(data, headers='firstrow',tablefmt="grid"))

    #         else: 
    #             print(colored("Incorrect username or password.Please try again or sign up","red"))
    #             print('\n') 
    
    elif short_code =="ex":
            print('\n')
            print("*"*30)
            print("Bye .......")
        
    else: 
        print(colored("I didn't get that. Please use one of the short codes","red"))
        print('\n')
        
        
            


if __name__ == '__main__':

    main()
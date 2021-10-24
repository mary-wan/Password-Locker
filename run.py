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
    print("Welcome to Password Locker.")
    while True:
        print('\n')
        print("Please input one of the short codes to navigate.")
        data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("su","yellow"), "Sign up to create your password locker account"], [colored("lg","yellow"),"Have an account already, log in to your account"],[colored("ex","yellow"),"Exit Password Locker"]]
        print(tabulate(data, headers='firstrow',tablefmt="grid"))
        print('\n')
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
        
        elif short_code =="lg": 
            print(colored("Log in......","green"))
            print("Enter username")
            username = input()
            print("Enter password")
            password = input()
            if user_verification(username,password):
                
                print('\n')
                print(colored(f"Hi {username}, What would you like to do?","yellow"))
                print('\n')    
                 
                while True:
                    print('\n')
                    print("Please input one of the short codes to navigate.")
                    data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("cc","yellow"), "Create new credential"],[colored("fc","yellow"),"Find credentials"],[colored("dc","yellow"),"Display credentials"],[colored("dl","yellow"),"Delete credentials"],[colored("lo","yellow"),"log out"]]
                    print(tabulate(data, headers='firstrow',tablefmt="grid"))
                    print('\n')
                    short_code = input().lower()
                    
                    if short_code == "cc":
                        print('\n')
                        print(colored("creating new credential......","green"))
                        print("Name of the Account...") 
                        account_name = input()
                        print("Enter username of the credential...") 
                        account_username = input()
                        while True:
                            print('\n')
                            print(colored("Please select to input password of generate password","green"))
                            data = [[colored('Short Code  ','green'),colored('         Action ','green')],[colored("in","yellow"), "Input password"],[colored("gp","yellow"),"Auto generate your password"]]
                            print(tabulate(data, headers='firstrow',tablefmt="grid"))
                            print('\n')
                            short_code = input().lower()
                                
                            if short_code == "in":
                                    print("Enter password of the credential...") 
                                    account_password = input()
                                    save_credentials(create_credential(account_name,account_username,account_password))
                                    print('\n')
                                    print(colored(f"Credential successfully created!!","yellow"))
                                    break
                            elif short_code == "gp":
                                    print("Enter your desired password length e.g 6")
                                    password_length = int(input())
                                    save_credentials(create_credential(account_name,account_username,generate_password(password_length)))
                                    print('\n')
                                    print(colored(f"Credential successfully created!!","yellow"))
                                    break
                            else:
                                    print(colored("I didn't get that. Please use one of the short codes","red"))
                                    print('\n')
                                    
                                
                    elif short_code == "fc":
                        print('\n')
                        print ("Enter account name for the credential you wish to find ")
                        account_find = input()
                        if check_credential_exist(account_find):
                            search_credential = find_credential(account_find)
                            data = [[colored('Description  ','green'),colored('         Credential ','green')],[colored("Account","cyan"), f"{search_credential.account}"],[colored("Username","cyan"),f"{search_credential.username}"],[colored("Password","cyan"),f"{search_credential.password}"]]
                            print(tabulate(data, headers='firstrow',tablefmt="grid"))
                            print('\n')
                        else:
                            print('\n')
                            print(colored("We could not find a credential in that account name","red"))
                            
                    elif short_code == "dc":
                        if display_credential():
                            print(colored("Here is a list of all your credentials","green"))
                            print('\n')
                            
                            for credential in display_credential():
                                data = [[colored("Account","cyan"), f"{credential.account}"],[colored("Username","cyan"),f"{credential.username}"],[colored("Password","cyan"),f"{credential.password}"]]
                                print(tabulate(data,tablefmt="grid"))
                                print('\n')
                                #   print(f"{credential.account} {credential.username} .....{credential.password}")
                        else:
                                print('\n')
                                print(colored("You dont seem to have any credentials saved yet","red"))
                                
                    elif short_code == "dl":
                        print('\n')
                        print("Enter name of the account to delete") 
                        delete_account = input() 
                        if check_credential_exist(delete_account):
                            account_to_delete = find_credential(delete_account)
                            print('\n')
                            print(f"Are You Sure You Wish to Delete {delete_account} credentials?")  
                            print("Enter y/n...")  
                            response = input().lower()
                            if response == 'y':
                                account_to_delete.delete_credential()
                                print(colored("Credential has been deleted!!","yellow"))

                            else :
                                print(colored("Account not deleted!!!","yellow"))
                        else:
                            print(colored("We could not find a credential in that account name","red"))

                    elif short_code =="lo":
                        print("*"*30)
                        print(colored("logging out...","green"))
                        print('\n')
                        print("*"*30)
                        # print("Bye .......")
                        break
                        
            else: 
                print('\n') 
                print(colored("Incorrect username or password.Please try again or sign up","red"))
                
        elif short_code =="ex":
            print("*"*30)
            print("Bye .......")
            break
        
        else: 
            print(colored("I didn't get that. Please use one of the short codes","red"))


if __name__ == '__main__':

    main()
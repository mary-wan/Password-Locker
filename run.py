#!/usr/bin/env python3.6
from user import User
from credentials import Credential
from termcolor import colored


def logo():
	print(colored("        ____                      _                     _   _     ","green"))
	print(colored("       |  _ \                    | |                   | | / /    ","green"))
	print(colored("       | |_) )  ____  ___   ___  | |      ___      ___ | |/ /     ","green"))
	print(colored("       |  __/  / _  |/ __  / __  | |     / __ \  /  _  |   (      ","green"))
	print(colored("       | |    / (_| |\__ \ \__ \ | |___ | (__) ||  (_  | |\ \     ","green"))
	print(colored("       |_|    \_____| ___/  ___/ |_____| \___ /  \ ___ |_| \_\    ","green"))
	print('\n')
	print(colored("*"*70,"red"))
 
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
    
def user_verification(usename,password):
    '''
    Function to verify if user details are correct
    '''
    return User.user_verification(usename,password)

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


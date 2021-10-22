#!/usr/bin/env python3.6
from user import User
from credentials import Credential
from termcolor import colored


def logo():
	print(colored("        ____                      _                  _         ","green"))
	print(colored("       |  _ \                    | |                | |  _     ","green"))
	print(colored("       | |_) )  ____  ___   ___  | |     ___    ___ | | / /    ","green"))
	print(colored("       |  __/  / _  |/ __  / __  | |    / _  \ /  _ | |/ /     ","green"))
	print(colored("       | |    / (_| |\__ \ \__ \ | |___| (_)  |  (_ |   \      ","green"))
	print(colored("       |_|    \_____| ___/  ___/ |_____|\ ___/ \___ |_|\_\     ","green"))
	print("\n")
 
logo()

# text = colored('Hello, World!', 'red')

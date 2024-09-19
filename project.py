import os
import json
import base64
from getpass import getpass
from cryptography.fernet import fernet

def add_new_password():
    ....
    
    
def retrive_password(site,username):
    ....
    
def generate_random_password():
    ....


def delete_password(site, username):
    ....


def change_password(site, username, new_password):
    .....


def main:
    master_pass = input("Welcome to the password manager /n enter your master password: ")
    
    if master_pass != __master__password:
        print(f"invalid master password")
        return
    else:
        try:
            option = int(input("\noptions\n1)add new password\n2)retrive password\n3)generate random password\n4)delete password\n5)change password\n6)quit\nchoose an option(1-6)"))
            if option == 1:
                add_new_password()
            elif option == 2:
                retrive_password(site,username)
            elif option == 3:
                generate_random_password()
            elif option == 4:
                delete_password()
            elif option == 5:
                change_password()
            elif option == 6:
                break
            else:
                print("invalid option")
        except ValueError:
            print("enter a fucking number next time u dimwit")
            return

if "__name__" == __main__ :
    main()
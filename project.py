import os
import json
import base64
from getpass import getpass
from cryptography.fernet import Fernet
import string
import random


def add_new_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    opt=input("enter 1 to enter own password and 2 to generate a random password for you")
    if opt == "1":
        while True:
            password = input("enter your password")
            if len(password) >= 10:
                break
            else: 
                continue
    elif opt == "2":
        password = generate_random_password()
    fernet = get_fernet()
    encrypted_pass = fernet.encrypt(password.encode())
    
    if os.path.exists("passwords.json"):
        with open("passwords.json","r") as file:
            passwords = json.load(file)
    else :
        passwords = {}
    
    
    passwords(site) = {"username":username, "password": encrypted_pass.decode()}
    
    
    with open("passwords.json","w") as file:
        json.dump(passwords, file)
    
    print("password added successfully")
            
        
def retrive_password(site, username):
    fernet = get_fernet()
    if os.path.exista("passwords.json"):
        with open("passwords.json","r") as file:
            passwords = json.load(file)

        if site in passwords:
            encrypted_pass = passwords[site]["password"]
            decrypted_pass = fernet.decrypt(encrypted_pass.encode()).decode()
            printf(f"username: {passwords[site][username]}")
            printf(f"password: {decrypted_pass}")
        else:
            print("no password found for the site")
    else:
        print("no password stored yet")
    
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(12))


def delete_password(site, username):
    ....


def change_password(site, username, new_password):
    .....


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def get_fernet():
    key = load_key()
    return Fernet(key)



def main():
    master_pass = getpass("Welcome to the password manager /n enter your master password: ")
    
    if master_pass != "1 Am TH3 dArth D0g1us @,1":
        print(f"invalid master password")
        return
    else:
        try:
            option = int(input("\noptions\n1)add new password\n2)retrive password\n3)generate random password\n4)delete password\n5)change password\n6)quit\nchoose an option(1-6)"))
            if option == 1:
                add_new_password()
            elif option == 2:
                site = input("enter name of the site: ")
                username = input("enter the username: ")
                retrive_password(site, username)
            elif option == 3:
                generate_random_password()
            elif option == 4:
                site = input("enter site name")
                username = input("enter username")
                delete_password(site, username)
            elif option == 5:
                site = input("enter site name")
                username = input("enter username")
                new_password = getpass("enter new password: ")
                change_password(site, username, new_password)
            elif option == 6:
                break
            else:
                print("invalid option")
        except ValueError:
            print("enter a fucking number next time u dimwit")
            return

if "__name__" == __main__ :
    main()
import os
import json
import base64
from getpass import getpass
from cryptography.fernet import Fernet
import string
import random


def get_fernet():
    if not os.path.exists("secret.key"):
        # If not, generate a new key and save it
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        # If the key exists, load it
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    
    # Return the Fernet instance initialized with the key
    return Fernet(key)


def add_new_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    opt=input("enter 1 to enter own password and 2 to generate a random password for you: ")
    if opt == "1":
        while True:
            password = getpass("enter your password: ")
            if len(password) >= 10:
                break
            else:
                print("password must be 10 characters long")
                continue
    elif opt == "2":
        password = generate_random_password()
        print(f"your randomly generated password is: {password}")
    fernet = get_fernet()
    encrypted_pass = fernet.encrypt(password.encode())
    
    if os.path.exists("passwords.json"):
        with open("passwords.json","r") as file:
            passwords = json.load(file)
    else :
        passwords = {}
        
    passwords[site] = {"username":username, "password": encrypted_pass.decode()}
    with open("passwords.json","w") as file:
        json.dump(passwords, file)
    print("password added successfully")
            
        
def retrive_password(site):
    fernet = get_fernet()
    if os.path.exists("passwords.json"):
        with open("passwords.json","r") as file:
            passwords = json.load(file)

        if site in passwords:
            a = passwords[site]
            encrypted_pass = a["password"]
            decrypted_pass = fernet.decrypt(encrypted_pass.encode()).decode()
            b = passwords[site]
            print(f"username: {b['username']}")
            print(f"password: {decrypted_pass}")
        else:
            print("no password found for the site")
    else:
        print("no password stored yet")
    
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(12))


def delete_password(site):
    if os.path.exists("passwords.json"):
        with open("passwords.json","r") as file:
            passwords = json.load(file)
        if site in passwords:
            del passwords[site]
        else:
            print("no such site found")
        with open("passwords.json","w") as file:
            json.dump(passwords, file)
    else:
        print("\n\n\nno passwords stored")
    

def change_password(site,username):
    while True:
        new_password = getpass("enter your new password: ")
        if len(new_password) >= 10:
            break
        else:
            print("password must be 10 characters long")
            continue
    fernet = get_fernet()
    encrypted_pass = fernet.encrypt(new_password.encode())
    
    
    with open("passwords.json","r") as file:
        passwords = json.load(file)
        
    passwords[site] = {"username":username, "password": encrypted_pass.decode()}
    with open("passwords.json","w") as file:
        json.dump(passwords, file)
    print("\n\n\npassword changed successfully")
    

def main():
    print("Welcome to the password manager")
    master_pass = input("enter your master password: ")
    
    if master_pass != "XZ1234xz":
        print(f"invalid master password")
        return
    while True:
        try:
            option = int(input("\noptions\n1)add new password\n2)retrive password\n3)generate random password\n4)delete password\n5)change password\n6)quit\nchoose an option(1-6): "))
            if option == 1:
                add_new_password()
            elif option == 2:
                site = input("enter name of the site: ")
                retrive_password(site)
            elif option == 3:
                generate_random_password()
            elif option == 4:
                site = input("enter site name: ")
                delete_password(site)
            elif option == 5:
                site = input("enter site name: ")
                username = input("enter username: ")
                change_password(site, username)
            elif option == 6:
               break
            else:
                print("invalid option")
        except ValueError:
            print("enter a fucking number u fucking dimwit")
    return

if __name__ == "__main__" :
    main()
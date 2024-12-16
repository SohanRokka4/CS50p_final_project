# Password Manager
    #### Video Demo:  https://youtu.be/pHBur-bfZBI
    
Overview
This is a simple command-line-based Password Manager program written in Python. It allows users to securely store, retrieve, update, and delete passwords for various sites. The passwords are encrypted using the Fernet encryption from the cryptography library, ensuring high security for stored credentials.

Features
Add New Password: Store a new password for a site with an encrypted format.
Retrieve Password: Decrypt and display the stored password for a specific site.
Generate Random Password: Generate a strong random password with special characters.
Delete Password: Remove a site's password entry from the storage.
Change Password: Update the password for an existing site.
Secure Storage: Uses Fernet encryption to securely store passwords in a JSON file.
Installation
Clone the Repository:
bash
Copy code
git clone [<repository_url>](https://github.com/SohanRokka4/CS50p_final_project.git)
cd password-manager
Install Dependencies: Make sure you have Python installed, then run:
Copy code
pip install cryptography pytest
Usage
Run the program:

Copy code
python project.py
Master Password: The default master password is:

Copy code
XZ1234xz
You can change it by editing the main() function in the project.py file.

Options:

sql
Copy code
1) Add new password
2) Retrieve password
3) Generate random password
4) Delete password
5) Change password
6) Quit
Security
The encryption key is stored in secret.key. If this file is deleted, you will not be able to decrypt existing passwords.
Passwords are stored in an encrypted format in a passwords.json file.
User inputs for passwords are hidden using getpass for extra privacy.
File Structure
vbnet
Copy code
├── project.py
├── README.md
├── requirements.txt
├── secret.key
├── passwords.json
├── tests/
│   └── test_project.py
Testing
The tests are written using pytest. You can run the tests using the following command:
bash
Copy code
pytest tests/test_project.py
Sample Tests in test_project.py:
test_get_fernet_key_generation: Checks if a new Fernet key is generated when it doesn't exist.
test_get_fernet_existing_key: Checks if the program can load an existing Fernet key.
test_delete_password: Ensures passwords are correctly deleted from the JSON file.
Dependencies
cryptography (for password encryption)
pytest (for testing)
To install dependencies, use:

Copy code
pip install -r requirements.txt
Known Issues
If you manually delete the secret.key file, previously stored passwords will not be retrievable.
Ensure you input a number in the options menu; otherwise, it will throw an error.
License
This project is licensed under the MIT License.

Author
Sohan Rokka - sohanrokka4@gmail.com
Feel free to contribute to this project by submitting pull requests or reporting issues.
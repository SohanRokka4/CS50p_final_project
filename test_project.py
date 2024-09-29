from project import  add_new_password, retrive_password, delete_password, change_password
import unittest
from unittest.mock import patch, mock_open



def test_add_new_password():
    with patch("project.get_fernet_key") as mock_get_fernet:
            mock_fernet = mock_get_fernet.return_value
            mock_fernet.encrypt.return_value = b'encrypted_password'
            
            # Call the add_password function
            add_new_password("gmail", "user", "password123")
            
            # Assert the file was opened correctly
            mock_file.assert_called_with("passwords.json", "r")
            
            # Check if the json.dump was called with the expected data
            expected_data = {
                "gmail": {
                    "username": "user",
                    "password": "encrypted_password"
                }
            }
            mock_json_dump.assert_called_once_with(expected_data, mock_file())



def test_retrive_password():
    ...
    
    
def test_delete_password():
    ....


def test_change_password():
    ...


def main():
    test_add_password()
    test_change_password()
    test_delete_password()
    test_retrive_password()


if __name__ == "__main__":
    main()
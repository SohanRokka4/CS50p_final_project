from project import get_fernet, retrive_password, add_new_password, delete_password, change_password, generate_random_password, add_new_password, retrive_password, change_password
import pytest
from unittest.mock import patch, mock_open
from cryptography.fernet import Fernet
import json
import os

# Test the Fernet key generation
@patch('builtins.open', new_callable=mock_open)
def test_get_fernet_key_generation(mock_file):
    # Simulate file not existing for key generation
    with patch('os.path.exists', return_value=False):
        fernet = get_fernet()
        assert isinstance(fernet, Fernet)
        mock_file().write.assert_called_once()  # Ensure key file is written

# Test loading existing Fernet key
@patch('builtins.open', new_callable=mock_open)
def test_get_fernet_existing_key(mock_file):
    # Simulate key file already exists
    mock_file().read.return_value = Fernet.generate_key()
    with patch('os.path.exists', return_value=True):
        fernet = get_fernet()
        assert isinstance(fernet, Fernet)
        mock_file().read.assert_called_once()


# Test deleting a password
@patch('builtins.input', return_value="testsite")
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps(
    {"testsite": {"username": "testuser", "password": Fernet(Fernet.generate_key()).encrypt(b"validpassword123").decode()}}
))
@patch('os.path.exists', return_value=True)
def test_delete_password(mock_exists, mock_file, mock_input):
    expected_passwords = {}
    
    delete_password("testsite")
    mock_file().write.assert_called_once_with(json.dumps(expected_passwords))


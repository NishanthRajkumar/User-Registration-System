'''
    @Author: Nishanth
    @Date: 31-03-2022 16:32:00
    @Last Modified by: Nishanth
    @Last Moddified date: 31-03-2022 16:32:00
    @Title: Validate user input for the user registration details
'''
import logging
import re
import sys

class UserRegistration:

    def __init__(self) -> None:
        self.patterns = {
            'name': r"^[A-Z][a-z]{2,}$",
            'email': r"^[A-Za-z0-9]{3,}([.][A-Za-z0-9]{3,})?[@][a-zA-Z]{2,}[.][a-zA-Z]{2,}([.][a-zA-Z]{2})?$"
        }

    def get_user_info(self) -> dict[str, str]:
        """
            Description:
                Gets the details from the user
            
            Parameter:
                None
            
            Return:
                returns the valid user info
        """
        user_info: dict[str, str] = {}
        user_info['First Name'] = input("Enter First Name: ")
        user_info['Last Name'] = input("Enter Last Name: ")
        user_info['Email'] = input("Enter Email: ")
        if self.validate_user_info(user_info['First Name'], 'name') == False:
            raise ValueError(f"Invalid First Name: {user_info['First Name']}")
        if self.validate_user_info(user_info['Last Name'], 'name') == False:
            raise ValueError(f"Invalid Last Name: {user_info['Last Name']}")
        if self.validate_user_info(user_info['Email'], 'email') == False:
            raise ValueError(f"Invalid Email: {user_info['Email']}")
        return user_info

    def validate_user_info(self, user_info: str, pattern_type: str) -> bool:
        """
            Description:
                checks if the name of the user is valid
            
            Parameter:
                name: name given by user
            
            Return:
                returns True if valid, else False
        """
        pattern_type = pattern_type.casefold()
        if pattern_type not in self.patterns.keys():
            raise ValueError("Invalid pattern type given")
        match = re.fullmatch(self.patterns[pattern_type], user_info)
        if match == None:
            return False
        return True


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"user_registration_app\user_reg.log", mode = 'a'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    user_reg = UserRegistration()
    print(f"Name pattern: {user_reg.patterns['name']}")
    try:
        user_info = user_reg.get_user_info()
        logging.info(f"Valid user info:\n{user_info}")
    except ValueError:
        logging.exception("User info is invalid")
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
        if self.validate_name(user_info['First Name']) == False:
            raise ValueError(f"Invalid First Name: {user_info['First Name']}")
        if self.validate_name(user_info['Last Name']) == False:
            raise ValueError(f"Invalid Last Name: {user_info['Last Name']}")
        return user_info

    def validate_name(self, name: str) -> bool:
        """
            Description:
                checks if the name of the user is valid
            
            Parameter:
                name: name given by user
            
            Return:
                returns True if valid, else False
        """
        name_pattern = r"^[A-Z][a-zA-Z]{2}[a-zA-Z]*$"
        match = re.fullmatch(name_pattern, name)
        if match:
            return True
        return False


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"user_registration_app\user_reg.log", mode = 'a'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    user_reg = UserRegistration()
    try:
        user_info = user_reg.get_user_info()
        logging.info(f"Valid user info:\n{user_info}")
    except ValueError:
        logging.exception("User info is invalid")
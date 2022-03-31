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

    def get_user_info(self):
        """
            Description:
                Gets the details from the user
            
            Parameter:
                None
            
            Return:
                returns the valid user info
        """
        while True:
            first_name = input("Enter First Name: ")
            if self.validate_name(first_name) == False:
                logging.warn("Invalid name. name must be min 3 charcters and starts with capital")
            else:
                break
        return first_name

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
    user_reg.get_user_info()
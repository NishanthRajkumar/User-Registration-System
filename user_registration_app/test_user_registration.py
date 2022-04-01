'''
    @Author: Nishanth
    @Date: 31-03-2022 19:48:00
    @Last Modified by: Nishanth
    @Last Moddified date: 31-03-2022 19:48:00
    @Title: testing the user registration class and it's pattern validation
'''
import unittest
from user_registration import UserRegistration

class UserRegistrationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user_reg = UserRegistration()

    def test_validate_name(self):
        self.assertTrue(self.user_reg.validate_user_info("Nishanth", 'name'))
        self.assertFalse(self.user_reg.validate_user_info("nishanth", 'name'))
        self.assertFalse(self.user_reg.validate_user_info("Ni", 'name'))
    
    def test_validate_email(self):
        self.assertTrue(self.user_reg.validate_user_info("nish@gmail.com", 'email'))
        self.assertFalse(self.user_reg.validate_user_info("n@gmail.com", 'email'))
        self.assertFalse(self.user_reg.validate_user_info("nish@g.c", 'email'))
    
    def test_validate_mobile(self):
        self.assertTrue(self.user_reg.validate_user_info("91 9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("19 9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("91 4952472949", 'mobile'))
    
    def test_validate_password(self):
        self.assertTrue(self.user_reg.validate_user_info("qweasd98@$", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("qwerty", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("pass word", 'password'))

if __name__ == '__main__':
    unittest.main()
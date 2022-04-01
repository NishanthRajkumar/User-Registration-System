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
        #Test Valid Emails
        self.assertTrue(self.user_reg.validate_user_info('abc@yahoo.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc-100@yahoo.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc.100@yahoo.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc111@abc.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc-100@abc.net', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc.100@abc.com.au', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc@1.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc@gmail.com.com', 'email'))
        self.assertTrue(self.user_reg.validate_user_info('abc+100@gmail.com', 'email'))
        
        #Test Invalid Emails
        self.assertFalse(self.user_reg.validate_user_info('abc', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc@.com.my', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc123@gmail.a', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc123@.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc123@.com.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('.abc@abc.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc()*@gmail.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc@%*.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc..2002@gmail.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc.@gmail.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc@abc@gmail.com', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc@gmail.com.1a', 'email'))
        self.assertFalse(self.user_reg.validate_user_info('abc@gmail.com.aa.au', 'email'))
    
    def test_validate_mobile(self):
        self.assertTrue(self.user_reg.validate_user_info("91 9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("19 9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("9952472949", 'mobile'))
        self.assertFalse(self.user_reg.validate_user_info("91 4952472949", 'mobile'))
    
    def test_validate_password(self):
        self.assertTrue(self.user_reg.validate_user_info("Qweasd98@", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("qwerty", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("pass word", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("password", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("Password", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("Password12", 'password'))
        self.assertFalse(self.user_reg.validate_user_info("Password12@$", 'password'))

if __name__ == '__main__':
    unittest.main()
'''
    @Author: Nishanth
    @Date: 31-03-2022 17:06:00
    @Last Modified by: Nishanth
    @Last Moddified date: 31-03-2022 17:06:00
    @Title: testing the user registration class and it's pattern validation
'''
import unittest
from user_registration import UserRegistration

class UserRegistrationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user_reg = UserRegistration()

    def test_validate_name(self):
        self.assertTrue(self.user_reg.validate_name("Nishanth"))
        self.assertFalse(self.user_reg.validate_name("nishanth"))
        self.assertFalse(self.user_reg.validate_name("Ni"))

if __name__ == '__main__':
    unittest.main()
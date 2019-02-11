import unittest 
from user import User 
class TestUser(unittest.TestCase):
   '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''# Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("virginie","mukantwari","0786679517","pasword","virgm2020@gmail.com",) # create User object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.first_name,"virginie")
        self.assertEqual(self.new_User.last_name,"mukantwari")
        self.assertEqual(self.new_User.phone_number,"0786679517")
        self.assertEqual(self.new_User.pasword,"iradukunda")
        self.assertEqual(self.new_User.email,"virgm2020@gmail.com")
        


if __name__ == '__main__':
    unittest.main()
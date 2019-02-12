import unittest # Importing the unittest module
from user import User # Importing the contact class 

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = User("virginie","mukantwari","0786679517","iradukunda","virgm2020@gmail.com") # create User object


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.first_name,"virginie")
    self.assertEqual(self.new_user.last_name,"mukantwari")
    self.assertEqual(self.new_user.number,"0786679517")
    self.assertEqual(self.new_user.password,"iradukunda")
    self.assertEqual(self.new_user.email,"virgm2020@gmail.com")

def test_save_user(self):
    '''
    test_save_contact test case to test if the user object is saved into
    the user list
    '''
    self.new_user.save_user() # saving the new user
    self.assertEqual(len(User.user_list),1)


def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

    # other test cases here
def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple user
    objects to our user_list
    '''
    self.new_user.save_user()
    test_user = User("virginie","mukantwari","0786679517","iradukunda","virgm2020@gmail.com") # new user
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)

# More tests above
def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("virginie","mukantwari","0786679517","iradukunda","virgm2020@gmail.com") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    

def test_user_exists(self):
    '''
    test to check if we can return a Boolean  if we cannot find the contact.
    '''

    self.new_user.save_user()
    test_user = User("virginie","mukantwari","0786679517","iradukunda","virgm2020@gmail.com") # new user
    test_user.save_user()

    user_exists = User.user_exist("0786679517")

    self.assertTrue(user_exists)


def test_display_all_contacts(self):
    '''
    method that returns a list of all contacts saved
    '''

    self.assertEqual(User.display_contacts(),User.user_list)

if __name__ == '__main__':
   unittest.main()
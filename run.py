from User import User
def create_user(self,first_name,last_name,number,password,email):
    '''
    Function to create a new contact
    '''
    new_user = User(self,first_name,last_name,number,password,email)
    return new_user

    def save_contacts(user):
    '''
    Function to save user
    '''
    user.save_user()


    def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

    def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)



    def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(number)
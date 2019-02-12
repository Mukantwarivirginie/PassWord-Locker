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
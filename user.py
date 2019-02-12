class User:
    """
    Class that generates new instances of users.
    """
    user_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,password,email):

        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.password = password
        self.email = email

    def save_user(self):

        '''
        save_User method saves User objects into User_list
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


    @classmethod
    def display_contacts(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False

    
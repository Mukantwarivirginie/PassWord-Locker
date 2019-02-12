class User:
    """
    Class that generates new instances of users.
    """
    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,password,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.password = passwordlaste
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
   

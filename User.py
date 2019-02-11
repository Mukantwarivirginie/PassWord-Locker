class User:
    """
    Class that generates new instances of users.
    """
    User_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,password,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.password = password
        self.email = email
   

   

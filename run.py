#!/usr/bin/env python3.6
from user import User

def create_user(first_name,last_name,number,password,email):
    '''
    Function to create a new contact
    '''
    new_user = User(first_name,last_name,number,password,email)
    return new_user
    

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


# def del_user(user):
#     '''
#     Function to delete a user
#     '''
#     user.delete_user()

# def find_user(number):
#     '''
#     Function that finds a user by number and returns the user
#     '''
#     return User.find_by_number(number)



# def check_existing_contacts(number):
#     '''
#     Function that check if a contact exists with that number and return a Boolean
#     '''
#     return User.user_exist(number)



# def display_contacts():
#     '''
#     Function that returns all the saved contacts
#     '''
#     return User.display_contacts()






def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display contacts, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print ("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Phone number ...")
            number = input()

            print("password...")
            password = input()

            print("Email address ...")
            email = input()






            save_user(create_user(first_name,last_name,number,password,email)) # create and save new user.
            print ('\n')
            print(f"New User {first_name} {last_name} {number} {password} {email} created")
            print ('\n')
        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for user in display_contacts():
                    print(f"{user.first_name} {user.last_name} .....{user.number}")

                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any contacts saved yet")
                    print('\n')

        elif short_code == 'fc':

                print("Enter the number you want to search for")

                search_number = input()
                if check_existing_contacts(search_number):
                   search_user = find_user(search_number)
                   print(f"{search_user.number} {search_user.email}")
                   print('-' * 20)

                   print(f"number.......{search_user.number}")
                   print(f"email.......{search_user.email}")
                else:
                    print("That user does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")




if __name__ == '__main__':

    main()
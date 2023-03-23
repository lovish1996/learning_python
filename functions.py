'''
This function prints the name of a person
It takes two parameters: first_name and last_name
It uses formatted string
'''


def print_name(first_name, last_name):
    print(f'Welcome, {first_name} {last_name}!')


# main function
if __name__ == '__main__':
    first_person_first_name = input('Enter first name: ')
    first_person_last_name = input('Enter last name: ')
    print_name(first_person_first_name, first_person_last_name)

    second_person_first_name = input('Enter first name: ')
    second_person_last_name = input('Enter last name: ')
    print_name(second_person_first_name, second_person_last_name)


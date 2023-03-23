# function to print name
def print_name(first, last):
    print(f'Hey, how are you doing {first} {last}?')


# main function for printing names of all family members
if __name__ == '__main__':
    your_first_name = input('Enter your first name: ')
    your_last_name = input('Enter your last name: ')
    print_name(your_first_name, your_last_name)

    brother_first_name = input('Enter your brother\'s first name: ')
    brother_last_name = input('Enter your brother\'s last name: ')
    print_name(brother_first_name, brother_last_name)

    father_first_name = input('Enter your father\'s first name: ')
    father_last_name = input('Enter your father\'s last name: ')
    print_name(father_first_name, father_last_name)

    mother_first_name = input('Enter your mother\'s first name: ')
    mother_last_name = input('Enter your mother\'s last name: ')
    print_name(mother_first_name, mother_last_name)

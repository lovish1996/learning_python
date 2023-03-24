def if_else():
    x = int(input('Enter a number:'))
    # Boolean expression True/ False
    if x > 1:
        print(f'{x} is greater than 1')
    elif x == 1:
        print(f'{x} is equal to 1')
    else:
        print(f'{x} is less than 1')
        
if __name__ == '__main__':
    if_else()

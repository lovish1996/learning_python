def get_weekdays(number):
    if number == 1:
        return 'Sunday'
    elif number == 2:
        return 'Monday'
    elif number == 3:
        return 'Tuesday'
    elif number == 4:
        return 'Wednesday'
    elif number == 5:
        return 'Thursday'
    elif number == 6:
        return 'Friday'
    elif number == 7:
        return 'Saturday'
    else:
        return 'Invalid number!'


if __name__ == '__main__':
    number = int(input('Enter a number between 1 and 7: '))
    weekday = get_weekdays(number)
    print(weekday)

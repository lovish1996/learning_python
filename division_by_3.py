def division_by_3(number):
    count = 0
    while number > 10:
        number /= 3
        count += 1
    return count


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    cnt = division_by_3(num)
    print(cnt)

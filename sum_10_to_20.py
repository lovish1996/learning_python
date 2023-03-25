def find_sum():
    sum_numbers = 0
    for i in range(10, 21, 2):
        sum_numbers += i
    return sum_numbers


if __name__ == '__main__':
    sum_10_to_20_even = find_sum()
    print(sum_10_to_20_even)

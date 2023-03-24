"""

for(int i=0; i<10; i++){
    // code statements here     0 .. 9
}
"""


def for_loop():
    for i in range(10):  # i 0..9        0 included 10 excluded
        print(i)


"""
for(int i=3; i<11; i++){
    // code statements here     3 .. 10
}
"""


def for_loop_start():
    for i in range(3, 11):  # i 3..10       3 included 11 excluded increment 1
        print(i)


"""
for(int i=3; i<11; i += 2){
    // code statements here     3 5 7 9
}
"""


def for_loop_increment():
    for i in range(3, 11, 2):  # i 3 5 7 9       3 included 11 excluded increment 2
        print(i)


"""
for(int i=11; i>3; i -= 2){
    // code statements here     11 9 7 5
}
"""


def for_loop_decrement():
    for i in range(11, 3, -2):  # i 11 9 7 5       11 included 3 excluded decrement 2
        print(i)


if __name__ == '__main__':
    for_loop()
    print()
    for_loop_start()
    print()
    for_loop_increment()
    print()
    for_loop_decrement()

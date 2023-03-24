# int i = 5;
# while(i>=0){cout << i << endl; i--;}
def while_loop():
    i = 5
    while i >= 0:
        print(i)  # 5 4 3 2 1 0
        i -= 1
        
        
if __name__ == '__main__':
    while_loop()

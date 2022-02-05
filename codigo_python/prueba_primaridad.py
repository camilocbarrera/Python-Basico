# sample cases
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
def is_prime(number):
    counter = 0 
    for i in range(1, number + 1):
            if (i == 1 or i == number) and number > 1:
                continue
            if number % i != 0 :
                return True
            else:
                return False
            
    if counter == 0:
        return True
    else: 
        False
        

def run():
    number = input("Please, enter a number: ")
    numbers = number.split(',')
    
    for n in numbers:
        # print(n)
        if is_prime(int(n)):
            print( n +  ' Is prime')
        else:
            print( n  + ' Is not a prime number')






if __name__ == '__main__':
    run()


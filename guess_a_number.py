# to get a random number from the computer
import random

# a function to take random number
def guess(a):
    random_num = random.randint(1,a)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Pick a Number between 1 and {a}:'))
        if (guess < random_num) :
            print("Please guess again, Number is Too Low.")
        elif (guess>random_num):
            print("Please guess again, Number is Too High.")
            
    print(f'You Guessed it Right!!, the Number is {random_num} correct.')
            
        
# example 
guess(10)
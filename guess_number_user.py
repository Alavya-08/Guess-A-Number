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
    
    # Here the user willl be giving the number and computer has to guess the correct number
def computer_guess(a):
    low = 1
    high = a
    feedback = ''
    while feedback !='C':
        if  low != high :
            guess= random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} Too High (H) ,  Too Low (L) or Correct(C)??').upper()
        if (feedback == 'H'):
            high = guess -1
        elif (feedback == 'L'):
            low = guess + 1
    print(f'Yes I Guessed it !!, The Number is {guess}')
            
            
        
# example 
computer_guess(10)
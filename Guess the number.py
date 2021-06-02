import random

guessesTaken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 6)
print('Hi, ' + name + ', Do you want to play a game?')

answer = input("Enter yes or no ")
if answer == 'yes':
    print('Great. Lets play! ')
    
    
    print('So, ' + name + ', I am going to roll a die, can you guess the number?  It can be any number from 1 to 6')

    for guessesTaken in range(6):
        print('Take a guess.') 
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.') 

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + name + '! You guessed my number in ' +
            guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')

else:
    print("well maybe next time!")

  

    

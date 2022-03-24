import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print(f"You guessed {guess}. That is correct! You win!")
        isGuessRight = True
    else:
        print(f"You guessed {guess}. Sorry, that isn't it. Try again.")
        if int(guess) > 10:
            i = 1
            while i<= 5:
                print('*' *i)
                i = i+1
            print("LOADING..")
            print(">>Please follow instructin by entering a number between 1 to 10!<<")
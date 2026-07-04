#Modify the number guessing game: add a maximum attempts limit of 7. if exceeded, print 'Game Over!'
secret_number = 7
max_attempts = 7
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You won!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game Over!")
import random
secret = random.randint(1, 100)
attempts = 0
print('guess the number between 1 and 100 ')
while True:
    guess = int(input('your guess: '))
    attempts += 1
    if guess < secret:
        print('too low! Try higher.')
    elif guess> guess:
        print('too high! Try lower.')
    else:
        print(f" correct ! you got it in {attempts} attempts!")
        break
    print(f" the secret number was {secret}.")
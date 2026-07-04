#Write a program that prints numbers 1-20 but skips multiples of 3(use continue).
for number in range(1, 21):
    if number % 3 == 0:
        continue

    print(number)
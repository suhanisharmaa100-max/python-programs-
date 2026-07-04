#Using a while loop, keep asking the user for a number until they enter 0. print the sum of all numbers entered.
total = 0

while True:
    number = float(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Sum of all numbers:", total)

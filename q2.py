#Print a multiplication table for any number entered by the user(using a for loop).
n = int(input(" enter number for multiplication table : "))
for i in range (1 , 11):
    print(f'{n} x {i} = {n * i}')
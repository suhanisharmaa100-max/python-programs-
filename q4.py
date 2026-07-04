#What is the difference between return and print inside a function? give an example of each.
#print() displays something on the screen. return sends a value back to the code that called the function, so you can store or use it later.

def print_sum(a, b):
    print(a + b)

result = print_sum(2, 3)
print(result)

 

#print_sum() shows 5, but it does not return a value, so result becomes None.

def return_sum(a, b):
    return a + b

result = return_sum(2, 3)
print(result)

 
#Here, return_sum() gives back 5, which is stored in result.
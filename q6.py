#Write a function totoal(numbers) that returns the sum of however many numbers are passed in. Call it with 2 numbers, then 5 numbers, then 5 numbers, then zero numbers-- what does it retuen for zero?
def totoal(*numbers):
    return sum(numbers)

print(totoal(5, 10))                    
print(totoal(1, 2, 3, 4, 5))            
print(totoal(10, 20, 30, 40, 50))       
print(totoal())                         
#Write a function is_prime(n) that returns True if n is a prime number, False otherwise.
def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(1))   # False
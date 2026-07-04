#Write a function print_profile(**details) that prints each key-value pair it receives, one per line. Call it like print_profile(name+"John", age+20, city+"Dehli").
def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_profile(name="John", age=20, city="Delhi")
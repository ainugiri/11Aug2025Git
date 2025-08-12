def random_no_generator():
    import random
    return random.randint(100000000000, 999999999999) 
def generate_random_numbers():
    numbers = []
    for _ in range(10):
        numbers.append(random_no_generator())
    return numbers
if __name__ == "__main__":
    random_numbers = generate_random_numbers()
    for number in random_numbers:
        print(number)
# newfile.py
# This file generates random numbers and prints them.
#    
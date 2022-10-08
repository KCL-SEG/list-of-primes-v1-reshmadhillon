"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 2
    if number_of_primes > 0:
        list.append(i)
    while len(list) < number_of_primes:
        prime = True
        i = i + 1
        for j in range (2,i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            list.append(i)

    return list

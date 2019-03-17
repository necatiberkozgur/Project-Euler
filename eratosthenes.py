#Here is an implementation for Sieve of Eratosthenes to generate prime numbers:


def sieve(limit):
    numbers = range(3, limit, 2)
    numbers.insert(0, 2)
    for i in numbers:
        for d in numbers:
            if d != i and d%i == 0:
                numbers.remove(d)
    print numbers
    print len(numbers)
sieve(int(input("Enter a number: ")))

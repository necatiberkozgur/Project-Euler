
#Here is some utility functions such as checking whether a number is prime or not, generating primes etc.
import math
fl = open("numbers.txt", "a+")
numlist = []


def isprimefromlist(k):
    for num in numlist:
        if(k%num==0):
            return False
    return True


def islargeprime(k):
    if k <= 1:
        return False
    elif k < 4:
        return True
    elif k % 2 == 0:
        return False
    elif k < 7:
        return True
    elif k % 3 == 0:
        return False
    else:
        for i in range(3, int(math.floor(math.sqrt(k)))+1, 2):
            if k%i==0:
                return False
    return True


for line in fl:
    numlist.append(int(line))

limit = int(input("Enter your limit: "))
count = 0
for k in range(0, limit):
    if islargeprime(k):
        count += 1
        print k
print count
fl.close()

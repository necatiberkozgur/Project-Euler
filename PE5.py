
#Problem definition:
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

fl = open("numbers.txt", "a+")
numlist = []

for line in fl:
    numlist.append(int(line))
largest = 1
for i in numlist:
    a = i
    if i>10:
        break
    while i<10:
        i = a*i
    i = i/a
    print i
    largest = i*largest

print largest

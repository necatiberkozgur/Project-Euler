
#Problem Definition:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

fl = open("numbers.txt", "a+")
numlist = []
lim = 600851475143
for line in fl:
    numlist.append(int(line))

for n in numlist:
    if(lim % n == 0):
        while lim % n == 0:
            lim = lim/n
            print n


#Problem definiton:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(i):
    strnum = str (i)
    for x in range(0, len(strnum)/2):
        if strnum[x] != strnum[len(strnum)-(1+x)]:
            return False
    return True
mul = 0
p = []
for x in range(999, 100, -2):
    for y in range(999, 100, -2):
        if(isPalindrome(x*y)):
            print x*y
            p.append(x*y)
            break

set(p)
list(p)
sorted(p)
print p[0]

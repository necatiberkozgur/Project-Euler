#Here is a palindrome checker for integer data:

def isPalindrome(i):
    strnum = str (i)
    for x in range(0, len(strnum)/2):
        if strnum[x] != strnum[len(strnum)-(1+x)]:
            return False
    return True

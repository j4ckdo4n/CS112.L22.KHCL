def checkPalindrome(str)->bool:
    if (len(str) == 0):
        return False
    for i in range(len(str) // 2):
        if (str[i] != str[len(str)-i-1]):
            return False
    return True

def Check(str, l, r, size):
    if (l >= size + (r-size)):
        print(str)
        return

    for i in range(l, r+1):
        if (checkPalindrome(str[l:i])):
            tmp = str[:i] + " " + str[i:]
            Check(tmp, i+1, r+1, size)
    
str = input()
Check(str, 0, len(str), len(str))
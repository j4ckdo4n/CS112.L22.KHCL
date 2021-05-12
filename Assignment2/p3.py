from sys import stdout

def Extend(s, left, right, index, maxLength):
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        if right - left + 1 > maxLength:
            index = left
            maxLength = right - left + 1
        left -= 1
        right += 1
    return (index, maxLength)

def LongestPalSubStr(s):
    index, maxLength = 0, 1
    for i in range(len(s)):
        index, maxLength = Extend(s, i - 1, i, index, maxLength)
        index, maxLength = Extend(s, i - 1, i + 1, index, maxLength)

    for i in range(index, index + maxLength):
        stdout.write(s[i])

s = input()
LongestPalSubStr(s)
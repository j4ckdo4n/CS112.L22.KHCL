from utils import binary_to_decimal, one_hot_encoding

def isSetSum(set, n, sum):
    global res
    if sum == 0:
        return True
    if n == 0: 
        return False
    if set[n-1] > sum:
        return isSetSum(set, n-1, sum)
    # else 
    # two case:
    #     1. include the last element
    #     2. exclude the last element
    if isSetSum(set, n-1, sum - set[n-1]):
        res.append(n-1)
        return True
    return isSetSum(set, n-1, sum)


file_inp = open('INPUT.txt','r')
file_out = open('OUTPUT.txt', 'r')
CORRECTED_CASES = 0
NUMBER_OF_CASES = int(file_inp.readline())
wrong_cases = []
for i in range(NUMBER_OF_CASES):
    global res
    res = [] # store the index of the set
    public_key = [int(x) for x in file_inp.readline().split()]
    answer = int(file_out.readline())
    C = int(file_inp.readline())
    if isSetSum(set=public_key, n=len(public_key), sum=C):
        one_hot = one_hot_encoding(res, len(public_key))
        decrypted_message = binary_to_decimal(one_hot)
        if decrypted_message == answer:
            CORRECTED_CASES += 1
        else:
            wrong_cases.append(f"answer: {answer} --- predict: {decrypted_message}")
    print(f"Done: {i+1}/100")
print(f"Corrected cases in total: {CORRECTED_CASES}/{NUMBER_OF_CASES}" )
print(f"Wrong cases: ", wrong_cases)
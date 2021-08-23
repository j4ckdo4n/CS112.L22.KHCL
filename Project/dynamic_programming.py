from utils import binary_to_decimal, one_hot_encoding

def FindSubsetSum(set, n, sum):
	subset =([[(False, []) for i in range(sum + 1)] for i in range(n + 1)])

	for i in range(n + 1): subset[i][0] = (True, [])

	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if (j < set[i - 1]) or (subset[i - 1][j][0]):
				subset[i][j] = subset[i - 1][j]

			elif subset[i - 1][j - set[i - 1]][0]:
				#traceback 
				subset[i][j] = (True, [i - 1] + subset[i - 1][j - set[i - 1]][1])

	return subset[n][sum]

file_inp = open('INPUT.txt','r')
file_out = open('OUTPUT.txt', 'r')
CORRECTED_CASES = 0
NUMBER_OF_CASES = int(file_inp.readline())
wrong_cases = []
for i in range(NUMBER_OF_CASES):
    public_key = [int(x) for x in file_inp.readline().split()]
    answer = int(file_out.readline())
    C = int(file_inp.readline())

    tmp = FindSubsetSum(set=public_key, n=len(public_key), sum=C)
    if tmp[0]:
        one_hot = one_hot_encoding(tmp[1], len(public_key))
        decrypted_message = binary_to_decimal(one_hot)
        if decrypted_message == answer:
            CORRECTED_CASES += 1
        else:
            wrong_cases.append(f"answer: {answer} --- predict: {decrypted_message}")
    print(f"Done: {i+1}/100")
print(f"Corrected cases in total: {CORRECTED_CASES}/{NUMBER_OF_CASES}" )
print(f"Wrong cases: ", wrong_cases)
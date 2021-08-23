def FindSubsetSum(set, sum):
	n = len(set)
	subset =([[(False, []) for i in range(sum + 1)] for i in range(n + 1)])

	for i in range(n+1):
		subset[i][0] = (True, [])

	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if (j < set[i - 1]) or (subset[i - 1][j][0]):
				subset[i][j] = subset[i - 1][j]

			elif subset[i - 1][j - set[i - 1]][0]:
				#traceback 
				subset[i][j] = (True, [i - 1] + subset[i - 1][j - set[i - 1]][1])

	return subset[n][sum]

def Decrypt(S, C):
	message = ""
	tmp = 1
	dec = 0
	bin = [0 for j in range(0, len(S))]
	subsetPos = FindSubsetSum(S, C)
	for i in subsetPos[1]: 
		bin[i] = 1

	for i in range(len(bin) - 1, -1, -1):
		dec += tmp * int(bin[i])
		tmp *= 2 
		
	message += str(dec)
	return message
         
# Driver code
if __name__=='__main__':
	S = [int(i) for i in input().split()]
	C = int(input())
	print(Decrypt(S, C))
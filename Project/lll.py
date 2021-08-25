def Sum(u, v):
    matrix = []
    for i in range(0, len(v)):
        matrix.append(v[i] + u[i])
    return matrix

def Multiply(k, v):
    matrix = []
    for i in range(0, len(v)):
        matrix.append(k * v[i])
    return matrix
  
def DotProduct(u, v):
    result = 0
    for i in range(0, len(v)):
        result += v[i] * u[i]
    return result

def CreateMatrix(ciphertext, public_key):
    matrix = [[1 if i == j else 0 for i in range(0, len(public_key))] for j in range(0, len(public_key))]
    for i in range(0, len(public_key)): 
        matrix[i].append(public_key[i])
    matrix.append([0 for i in range(0, len(public_key))])
    matrix[len(public_key)].append(-ciphertext)
    return matrix

def GramSchmidt(basis):
    orth_basis = [basis[0]]
    proj_coef = {}
    for j in range(1, len(basis)):
        orth_basis.append(basis[j])
        for i in range(0, j):
            proj_coef[str(j) + str(i)] = (DotProduct(orth_basis[i], basis[j])) / (DotProduct(orth_basis[i], orth_basis[i]))
            orth_basis[j] = Sum(orth_basis[j], Multiply(-1 * proj_coef[str(j) + str(i)], orth_basis[i]))
    return (orth_basis, proj_coef)

def LLL(basis):
    while True:
        GS_basis, GS_coef = GramSchmidt(basis)
        for j in range(1, len(basis)):
            for i in range(j - 1, -1, -1):
                if abs(GS_coef[str(j) + str(i)]) > 0.5:
                    basis[j] = Sum(basis[j], Multiply(-1 * round(GS_coef[str(j) + str(i)]), basis[i]))

        GS_basis, GS_coef = GramSchmidt(basis)
        try:
            for j in range(0, len(basis) - 1):
                tmp = Sum(GS_basis[j + 1], Multiply(GS_coef[str(j + 1) + str(j)], GS_basis[j]))
                if DotProduct(tmp, tmp) < 0.99*(DotProduct(GS_basis[j], GS_basis[j])):
                    basis[j], basis[j + 1] = basis[j + 1], basis[j]
                    raise Exception()
            return basis
        except: 
            continue

def Decrypt(matrix):
    short_vectors = LLL(matrix)
    binary_string = ""
    for vector in short_vectors:
        current = ""
        check = 0
        for n in vector:
            current += str(n)
            if (n != 1) and (n != 0): check = 1
        if not check: binary_string = current
    binary_string = binary_string[:-1]
    message = 0
    tmp = 1
    for i in range(len(binary_string) - 1, -1, -1):
        message += tmp * int(binary_string[i])
        tmp *= 2
    return message

file_inp = open('INPUT.txt','r')
file_out = open('OUTPUT.txt', 'r')
CORRECTED_CASES = 0
NUMBER_OF_CASES = int(file_inp.readline())
wrong_cases = []
for i in range(NUMBER_OF_CASES):
    public_key = [int(x) for x in file_inp.readline().split()]
    answer = int(file_out.readline())
    C = int(file_inp.readline())

    decrypted_message = Decrypt(CreateMatrix(C, public_key))
    if decrypted_message == answer:
        CORRECTED_CASES += 1
    else:
        wrong_cases.append(f"answer: {answer} --- predict: {decrypted_message}")
    print(f"Done: {i+1}/100")
print(f"Corrected cases in total: {CORRECTED_CASES}/{NUMBER_OF_CASES}" )
print(f"Wrong cases: ", wrong_cases)
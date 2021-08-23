from math import gcd
import random


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# the extended Euclidean algorithm
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = egcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse_euclidean(n, m):
    gcd, x, y = egcd(n, m)
    if gcd != 1:
        return -1
    return (x % m + m) % m # x could be nagative

def generate_super_increasing_set(length, margin=5):
    sumset = 0
    arr = []
    for i in range(length):
        tmp = random.randint(sumset+1, sumset + margin)
        sumset += tmp
        arr.append(tmp)
    return arr, sumset

def generate_q_r(sumset, margin=1e6):
    while True:
        q = random.randint(sumset+1, sumset+margin)
        r = random.randint(1, q-1)
        if gcd(r, q) == 1:
            return q, r

def generate_public_key(private_keys, q, r):
    result = []
    for key in private_keys:
        result.append(r * key % q)
    return result

def generate_ciphertext(m, public_keys):
    bit_arrays = []
    C = 0 # ciphertext value
    for i in range(len(public_keys)):
        bit_arrays.append(m % 2)
        m //= 2
    bit_arrays.reverse()
    for i in range(len(public_keys)):
        C += bit_arrays[i] * public_keys[i]
    return C, bit_arrays

def one_hot_encoding(array, length):
    result = [0 for _ in range(length)]
    for i in array:
        result[i] = 1
    return result

def binary_to_decimal(binary_bits):
    binary_bits.reverse()
    # print(f"On binary_to_decimal: {binary_bits}")
    decimal = 0
    temp = 0
    for bit in binary_bits:
        decimal += bit * (2 ** temp)
        temp += 1
    return decimal
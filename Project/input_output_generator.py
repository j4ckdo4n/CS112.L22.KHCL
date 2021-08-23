from typing import Iterator
from utils import *
import random


file_inp = open("INPUT.txt", 'w')
file_out = open("OUTPUT.txt", 'w')

# for turning
NUMBER_OF_INPUT = 100
MINIMUM_OF_M = 14
RANGE_OF_INPUT_LENGTH = (4, 33) # the number of bits 

file_inp.write(str(NUMBER_OF_INPUT) + "\n")

for i in range(NUMBER_OF_INPUT):
    n = random.randint(*RANGE_OF_INPUT_LENGTH)
    private_keys, sumset = generate_super_increasing_set(length=n)
    q, r = generate_q_r(sumset)
    public_keys = generate_public_key(private_keys, q, r)
    # maximum value n-bits required 2*2^(n-1)-1
    m = random.randint(MINIMUM_OF_M, 2 * (2 ** (n - 1) - 1))
    C, bits = generate_ciphertext(m, public_keys)
    
    # show history
    print(f"N = {n}")
    print("private keys: ", private_keys)
    print(f"q, r = {q} {r} \ngcd({q}, {r}) = {gcd(q, r)}")
    print("public keys: ", public_keys)
    print(f"m = {m}")
    print(f"ciphertext C = {C}")
    print("bits array: ", bits)
    print("---------------------------------------")

    # for INPUT.txt
    for key in public_keys:
        file_inp.write(f"{str(key)} ")
    file_inp.write(f"\n{C}\n")

    # for OUTPUT.txt
    file_out.write(f"{m}\n")
print("Done")

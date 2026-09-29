import math
import os
import random
import re
import sys

def getTotalX(a, b):
    cuenta = 0
    inicio = max(a)
    fin = min(b)
    
    for x in range(inicio, fin + 1):
        es_valido = True
        
        for numero_a in a:
            if x % numero_a != 0:
                es_valido = False
                
        for numero_b in b:
            if numero_b % x != 0:
                es_valido = False
                
        if es_valido:
            cuenta = cuenta + 1
            
    return cuenta

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
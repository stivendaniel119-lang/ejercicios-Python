import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    cuenta_manzanas = 0
    for manzana in apples:
        donde_cayo = a + manzana
        if donde_cayo >= s and donde_cayo <= t:
            cuenta_manzanas = cuenta_manzanas + 1
            
    cuenta_naranjas = 0
    for naranja in oranges:
        donde_cayo = b + naranja
        if donde_cayo >= s and donde_cayo <= t:
            cuenta_naranjas = cuenta_naranjas + 1
            
    print(cuenta_manzanas)
    print(cuenta_naranjas)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
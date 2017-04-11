from math import sqrt
from time import time
from sys import exit

control_val = 600851475143
val_primes = []
prime_numbers = [11]
initial = time()
val = int(sqrt(control_val))

for i in range(12, val):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        for j in range(len(prime_numbers)):
            prime = prime_numbers[j]
            if prime > sqrt(float(i)):
                prime_numbers.append(i)
                if control_val % i == 0:
                    val_primes.append(i)
                    if len(val_primes) == 1:
                        multiplication = i
                    else:
                        multiplication = multiplication * i
                        if multiplication == control_val:
                            print i
                            final = time()
                            print final - initial
                            exit()
                break
            elif int(i) % int(prime) == 0:
                break

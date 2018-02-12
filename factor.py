#!/usr/bin/env python


from primality_testing import prime

def factors(num):
    list1 = prime(num)
    factors = []
    for i in list1:
        if num % i ==0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    print("Factors of {} is {}".format(35, str(factors(35))))
    print("Factors of {} is {}".format(48, str(factors(48))))

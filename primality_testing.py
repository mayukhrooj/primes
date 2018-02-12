#!/usr/bin/env python


def prime(numb):
    prime_list = []
    for num in xrange(2, numb):
        divisible = 0
        for num2 in xrange(1,num+1):
            if num % num2 == 0:
                divisible += 1
        if divisible == 2:
            prime_list.append(num)
    return prime_list

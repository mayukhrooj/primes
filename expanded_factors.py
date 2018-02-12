#!/usr/bin/env python

from factor import factors

def epform(num):
    ep_form = []
    l1 = factors(num)
    for i in l1:
        count = 0
        be = []
        while(num % i == 0):
            count += 1
            num /= i
        be.append(i)
        be.append(count)
        ep_form.append(be)
    return ep_form


if __name__ == "__main__":
    print("Expanded form of {} is {}".format(24, str(epform(24))))
    print("Expanded form of {} is {}".format(693, str(epform(693))))
    print("Expanded form of {} is {}".format(786, str(epform(786))))
    print("Expanded form of {} is {}".format(460, str(epform(460))))

from decimal import *
import math
from math import factorial
import re
import matplotlib.pyplot as plt

def get_pi_str():
    file = open('pi.txt', 'r')
    return file.read()

def to_base(n, b):
    p = 0
    while n > b**(p+1):
        p += 1

    new_num = []
    while p > 0:
        basenum = b**p
        if n > basenum:
            times = long(math.floor(n/basenum))
            new_num.insert(0, math.floor(n/basenum))
            n -= (times*basenum)
        else:
            new_num.insert(0, 0)

        p -= 1

    new_num.insert(0, n)
    return new_num

def get_num_quan(an, base):
    quan = [0]*(base+1)
    for n in an:
        n = int(math.floor(n))
        quan[n] += 1

    return quan

def make_graph(quan, base):
    indeces = range(len(quan))
    x_choords = indeces
    if base >= 100:
        size = (100, 3)
    else:
        size = (25, 3)


    plt.rcParams['figure.figsize'] = size
    plt.bar(x_choords, quan, align='center')
    plt.xticks(x_choords, indeces, size=10)
    plt.ylabel('quan')
    plt.title('digit frequency for pi in base %d' % base)
    # plt.show()
    plt.savefig('graphs/%d.png' % base)
    plt.close()

pi_digits = long(re.sub(r'\.', '', get_pi_str()))
diffs = []

for b in xrange(256, 1, -1):
    new_pi = to_base(pi_digits, b)
    quan = get_num_quan(new_pi, b)
    make_graph(quan, b)
    print(b, quan)

#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Throw dice')
    parser.add_argument('nb', type=int)
    args = parser.parse_args()
    fails = 0
    for x in xrange(args.nb):
        dice = random.randint(1, 6)
        fail = dice <= 3
        print dice, "Fail" if fail else "Ok"
        if fail:
            fails += 1
    print "Failure(s)", fails

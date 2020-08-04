# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:59:53 2020

@author: mhous
"""

import time
max_iterations = 10000

def rev(n):
    return int(str(n)[::-1])

def palindrome(n):
    sequence = []
    sequence.append(n)
    while (n != rev(n)):
        n = n + rev(n)
        sequence.append(n)
        if len(sequence) >= max_iterations:
            break
    return sequence

def palindrome_info(n):
    test = palindrome(n)
    if len(test) >= max_iterations:
        print("Integer:" + str(n))
        print("Candidate Lychrel Number")
        print("Number of Iterations:" + str(max_iterations))
        print("Number of Digits in Last Iteration: " + str(len(str(test[-1]))))
        print("Time to run: " + str(time.time() - start_time))
        print("")
    else:
        print("Integer:" + str(n))
        print(test)
        print("Palindrome: " + str(test[-1]))
        print("Number of Digits in Palindrome: " + str(len(str(test[-1]))))
        print("Number of Iterations: " + str(len(test)-1))
        print("Time to run: " + str(time.time() - start_time))
        print("")


start_time = time.time()
palindrome_info(196)
print("Time to run: " + str(time.time() - start_time))
palindrome_info(197)
print("Time to run: " + str(time.time() - start_time))










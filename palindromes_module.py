# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:06:00 2020

@author: mhous
"""

def reverse(n):
    '''
    Reverses the digits of an integer
    '''
    return int(str(n)[::-1])

def convert_list_to_int(list): 
    '''
    Converts list of digits to integer
    '''
    s = [str(i) for i in list] 
    res = int("".join(s))
    return(res)
    
    
def palindrome_test(n, max_iterations):
    '''
    Tests whether an integer n is a candidate lychrel number
    '''
    sequence = []
    sequence.append(n)
    while (n != reverse(n)):
        n = n + reverse(n)
        sequence.append(n)
        if len(sequence) >= max_iterations:
            break
    return sequence


def count_frequency(dictionary):
    '''
    Takes a dictionary where keys are an integer and values are the number of iterations and returns the frequency of number of iterations 
    '''
    freq = {}
    for entry in dictionary.values():
        if entry in freq:
            freq[entry] +=1
        else:
            freq[entry] = 1
    return freq

def rel_frequency_dict_to_lists(frequencies):
    '''
    Takes a dictionary of relative frequencies and enables plotting by returning two lists, freq_x and freq_y
    '''
    sorted_frequencies = dict(sorted(frequencies.items(), key = lambda x: x[0]))
    rel_freq = dict(sorted(frequencies.items(), key = lambda x: x[0]))
    rel_freq.update({n: round(100*sorted_frequencies[n]/sum(frequencies.values()), 4) for n in sorted_frequencies.keys()})
    freq_lists = sorted(rel_freq.items())
    freq_x, freq_y = zip(*freq_lists)
    return freq_x, freq_y






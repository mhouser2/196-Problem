# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:11:59 2020

@author: mhous
"""

import time
import winsound
import palindromes_module as p
import matplotlib.pyplot as plt
duration = 2000  # milliseconds
freq = 440  # Hz

outer_digit_list = [(1, 0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (2,9), (3,9), (4,9), (5,9), (6,9), (7,9), (8,9), (9,9)]
inner_digit_list = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9), (1,9), (2,9), (3,9), (4,9), (5,9), (6,9), (7,9), (8,9), (9,9)]


def list_range(digits):
    min_digit = p.convert_list_to_int([1] + [0]* (digits-1))
    max_digit = p.convert_list_to_int([1] + [0] * digits)
    return list(range(min_digit, max_digit))

def master(digits, max_iterations):
    lychrel_candidates = []
    terminating_sequences = []
    all_ints = list_range(digits)
    if digits == 3:
        for i in range(len(all_ints)):
            if (int(str(all_ints[i])[0]), int(str(all_ints[i])[-1])) in outer_digit_list:
                reverse_add_sequence = p.palindrome_test(all_ints[i], max_iterations)
                if len(reverse_add_sequence) < max_iterations:
                    terminating_sequences.append(reverse_add_sequence)
                else:
                    lychrel_candidates.append(reverse_add_sequence[0])
    if digits in [4,5]:
        for i in range(len(all_ints)):
            if (int(str(all_ints[i])[0]), int(str(all_ints[i])[-1])) in outer_digit_list and (int(str(all_ints[i])[1]), int(str(all_ints[i])[-2])) in inner_digit_list:
                reverse_add_sequence = p.palindrome_test(all_ints[i], max_iterations)
                if len(reverse_add_sequence) < max_iterations:
                    terminating_sequences.append(reverse_add_sequence)
                else:
                    lychrel_candidates.append(reverse_add_sequence[0])
    if digits in [6,7]:
        for i in range(len(all_ints)):
            if (int(str(all_ints[i])[0]), int(str(all_ints[i])[-1])) in outer_digit_list and (int(str(all_ints[i])[1]), int(str(all_ints[i])[-2])) in inner_digit_list:
                if (int(str(all_ints[i])[2]), int(str(all_ints[i])[-3])) in inner_digit_list:
                    reverse_add_sequence = p.palindrome_test(all_ints[i], max_iterations)
                    if len(reverse_add_sequence) < max_iterations:
                        terminating_sequences.append(reverse_add_sequence)
                    else:
                        lychrel_candidates.append(reverse_add_sequence[0])
    if digits in [8,9]:
        for i in range(len(all_ints)):
            if (int(str(all_ints[i])[0]), int(str(all_ints[i])[-1])) in outer_digit_list and (int(str(all_ints[i])[1]), int(str(all_ints[i])[-2])) in inner_digit_list:
                if (int(str(all_ints[i])[2]), int(str(all_ints[i])[-3])) in inner_digit_list:
                    if (int(str(all_ints[i])[3]), int(str(all_ints[i])[-4])) in inner_digit_list:
                        reverse_add_sequence = p.palindrome_test(all_ints[i], max_iterations)
                        if len(reverse_add_sequence) < max_iterations:
                            terminating_sequences.append(reverse_add_sequence)
                        else:
                            lychrel_candidates.append(reverse_add_sequence[0])
    
    return terminating_sequences, lychrel_candidates


start_time = time.time()
terminating_sequences3, lychrel_candidates3 = master(3, 200)
terminating_sequences4, lychrel_candidates4 = master(4, 200)
terminating_sequences5, lychrel_candidates5 = master(5, 200)
terminating_sequences6, lychrel_candidates6 = master(6, 200)
terminating_sequences7, lychrel_candidates7 = master(7, 200)
terminating_sequences8, lychrel_candidates8 = master(8, 200)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)

terminating_sequences = []
for i in range(len(terminating_sequences3)):
    terminating_sequences.append(terminating_sequences3[i])
for i in range(len(terminating_sequences4)):
    terminating_sequences.append(terminating_sequences4[i])
for i in range(len(terminating_sequences5)):
    terminating_sequences.append(terminating_sequences5[i])    
for i in range(len(terminating_sequences6)):
    terminating_sequences.append(terminating_sequences6[i])
for i in range(len(terminating_sequences7)):
    terminating_sequences.append(terminating_sequences7[i])
for i in range(len(terminating_sequences8)):
    terminating_sequences.append(terminating_sequences8[i])


lychrel_candidates = []
for i in range(len(lychrel_candidates3)):
    lychrel_candidates.append(lychrel_candidates3[i])
for i in range(len(lychrel_candidates4)):
    lychrel_candidates.append(lychrel_candidates4[i])
for i in range(len(lychrel_candidates5)):
    lychrel_candidates.append(lychrel_candidates5[i])    
for i in range(len(lychrel_candidates6)):
    lychrel_candidates.append(lychrel_candidates6[i])
for i in range(len(lychrel_candidates7)):
    lychrel_candidates.append(lychrel_candidates7[i])
for i in range(len(lychrel_candidates8)):
    lychrel_candidates.append(lychrel_candidates8[i])

winsound.Beep(freq, duration)


lengths_dictionary = {terminating_sequences[i][0] : len(terminating_sequences[i])-1 for i in range(len(terminating_sequences))}


frequencies = p.count_frequency(lengths_dictionary)
sorted_frequencies = dict(sorted(frequencies.items(), key = lambda x: x[0]))
rel_freq = dict(sorted(frequencies.items(), key = lambda x: x[0]))
rel_freq.update({n: round(100*sorted_frequencies[n]/sum(frequencies.values()), 6) for n in sorted_frequencies.keys()})

lychrel_dictionary = {}
for j in range(len(lychrel_candidates)):
    lychrel_dictionary[lychrel_candidates[j]] = -1


xticks = []
for i in range(98):
    if i % 5 == 0:
        xticks.append(i)


yticks = []
for i in range(20):
    if i % 5 == 0:
        yticks.append(i)
        

f, ax = plt.subplots(figsize=(10, 6))
freq_lists = sorted(rel_freq.items())
freq_x, freq_y = zip(*freq_lists)
plt.bar(freq_x,freq_y)
plt.title("Figure 6: Relative Frequency of Number of Iterations", loc = "left")
plt.ylabel("Percent")
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlabel("Number of Iterations")


plt.figure()
f, ax = plt.subplots(figsize=(12, 8))
lists = sorted(lengths_dictionary.items())
x, y = zip(*lists)
lists2 = sorted(lychrel_dictionary.items())
x2, y2 = zip(*lists2)
plt.scatter(x,y, s = .05)
plt.scatter(x2,y2, s = .05, color = 'red')
plt.title("Figure 7: Number of Iterations to Reach a Palindrome, Possible Seeds only", loc = 'left')
plt.xlabel("Number")
plt.ylabel("Number of Iterations")








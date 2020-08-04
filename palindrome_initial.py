# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:22:12 2020

@author: mhous
"""

import time
import matplotlib.pyplot as plt
import palindromes_module as p

#Creates a list of lists of eventual palindromic numbers
def palindromes(max_number, max_iterations = 100):
    lychrel = []
    #creates list of natural numbers from 10 to max_number 
    numbers_list = list(range(max_number + 1))
    #Creates a list of max_number lists in order to see the sequence for each number until it reaches palindrome
    main_list = [[] for i in range(len(numbers_list))]
    for i in list(range(max_number+1)):
        #When i in range of max numbers, when i != the reverse of i
        while (numbers_list[i] != p.reverse(numbers_list[i])):
            #add initial number to beginning of list
            main_list[i].append(numbers_list[i])
            #add rev(i) to i
            numbers_list[i] = numbers_list[i] + p.reverse(numbers_list[i])
            #if max number of iterations occurs, stop
            if len(main_list[i]) >= max_iterations:
                lychrel.append(main_list[i][0])
                break
            #if palindrome is found, stop
        else:
            main_list[i].append(numbers_list[i])
    for i in range(max_number +1):
        if main_list[i][0] in lychrel:
            del main_list[i][:]
    main_list = [x for x in main_list if x!=[]]
    return main_list, lychrel



start_time = time.time()
sequences, lychrels = palindromes(1000, 100)
print("Time to run: " + str(time.time() - start_time))


lengths_dictionary = {sequences[i][0] : len(sequences[i])-1 for i in range(len(sequences))}

frequencies = p.count_frequency(lengths_dictionary)
print(lychrels)
sorted_frequencies = dict(sorted(frequencies.items(), key = lambda x: x[0]))
rel_freq = dict(sorted(frequencies.items(), key = lambda x: x[0]))
rel_freq.update({n: round(100*sorted_frequencies[n]/sum(frequencies.values()), 2) for n in sorted_frequencies.keys()})
print(sorted_frequencies)
print(rel_freq)

test = {i[0] : i[-1] for i in sequences}



freq_lists = sorted(sorted_frequencies.items())
freq_x, freq_y = zip(*freq_lists)
plt.bar(freq_x,freq_y)
plt.title("Frequency of Number of Iterations")
plt.ylabel("Count")
plt.xlabel("Number of Iterations")

plt.show()

plt.figure()
rel_freq_lists = sorted(rel_freq.items())
rf_x, rf_y = zip(*rel_freq_lists)
plt.bar(rf_x,rf_y)
plt.title("Relative Frequency of Number of Iterations")
plt.ylabel("Percent")
plt.xlabel("Number of Iterations")
plt.show

plt.figure()
lists = sorted(lengths_dictionary.items())
x, y = zip(*lists)
plt.scatter(x,y, s = .2)
plt.title("Number of Iterations to Reach a Palindrome")
plt.xlabel("Number")
plt.ylabel("Number of Iterations")

plt.show
print("Time to run: " + str(time.time() - start_time))


plt.figure()
lists2 = sorted(test.items())
x2, y2 = zip(*lists2)
plt.scatter(x2,y2, s = .1)
plt.title("Number and its Associated Palindrome")
plt.show



# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:52:35 2020

@author: mhous
"""
duration = 200  # milliseconds
freq = 440  # Hz
import time
import palindromes_module as p
import winsound
import random
import matplotlib.pyplot as plt

max_iterations = 200

def mc_lychrels(digits, number_tests, max_iterations):
    min_digit = p.convert_list_to_int([1] + [0]* (digits-1))
    max_digit = p.convert_list_to_int([1] + [0] * (digits))
    b = 0
    for i in range(number_tests):
        a = p.palindrome_test(random.randint(min_digit,max_digit), max_iterations)
        if len(a) >= max_iterations:
            b += 1
    return (b/number_tests) * 100

def mc_lychrels_dictionary(min_digits, max_digits, number_tests, max_iterations):
    a = {}
    for i in range(min_digits, (max_digits+1)):
        a[i] = round(mc_lychrels(i, number_tests, max_iterations), 2)
    return a

start_time = time.time()
mc_lychrel_dictionary = mc_lychrels_dictionary(3, 30, 100000, max_iterations)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)

plt.figure()
f, ax = plt.subplots(figsize=(12, 8))
lists = sorted(mc_lychrel_dictionary.items())
x, y = zip(*lists)
plt.scatter(x,y)
plt.title('Figure 4: Candidate Lychrel Numbers as a Share of all Integers for a Specified Number of Digits', loc = 'left')
plt.xlabel("Number of Digits")
plt.ylabel("Percent")



def mc_palindrome(digits, palindromics, max_iterations):
    min_digit = p.convert_list_to_int([1] + [0]* (digits-1))
    max_digit = p.convert_list_to_int([1] + [0] * (digits))
    palindromes = []
    while len(palindromes) < palindromics:
        a = p.palindrome_test(random.randint(min_digit,max_digit), 100)
        if len(a) < max_iterations:
            palindromes.append(a)
    return palindromes


start_time = time.time()
palindromes5 = mc_palindrome(5, 100000, 200)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)

start_time = time.time()
palindromes10 = mc_palindrome(10, 100000, 200)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)

start_time = time.time()
palindromes15 = mc_palindrome(15, 100000, 200)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)

start_time = time.time()
palindromes20 = mc_palindrome(20, 100000, 200)
print("Time to run: " + str(time.time() - start_time))
winsound.Beep(freq, duration)



def lengths_function(somelist):
    lengths_dictionary = {somelist[i][0] : len(somelist[i])-1 for i in range(len(somelist))}
    frequencies = p.count_frequency(lengths_dictionary)
    return frequencies


lengths5 = lengths_function(palindromes5)
lengths10 = lengths_function(palindromes10)
lengths15 = lengths_function(palindromes15)
lengths20 = lengths_function(palindromes20)




freq_x5, freq_y5 = p.rel_frequency_dict_to_lists(lengths5)
freq_x10, freq_y10 = p.rel_frequency_dict_to_lists(lengths10)
freq_x15, freq_y15 = p.rel_frequency_dict_to_lists(lengths15)
freq_x20, freq_y20 = p.rel_frequency_dict_to_lists(lengths20)

fig = plt.figure()
fig, ax = plt.subplots(2, 2, figsize=(16, 8))
ax[0,0].bar(freq_x5, freq_y5)
ax[0,1].bar(freq_x10, freq_y10)
ax[1,0].bar(freq_x15, freq_y15)
ax[1,1].bar(freq_x20, freq_y20)
ax[0,0].set_ylim([0, 27.5])
ax[0,1].set_ylim([0, 27.5])
ax[1,0].set_ylim([0, 27.5])
ax[1,1].set_ylim([0, 27.5])
ax[0,0].set_xlim([-1, 80])
ax[0,1].set_xlim([-1, 80])
ax[1,0].set_xlim([-1, 80])
ax[1,1].set_xlim([-1, 80])
ax[0,0].set_title("Figure 5: Relative Frequency for 5 digit integers", loc = 'left')
ax[0,1].set_title("10 digits", loc = 'left')
ax[1,0].set_title("15 digits", loc = 'left')
ax[1,1].set_title("20 digits", loc = 'left')
for ax in ax.flat:
    ax.set(xlabel='Number of Iterations', ylabel='Percent')
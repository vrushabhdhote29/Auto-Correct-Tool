#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = np.zeros((m+1, n+1), dtype=int)

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]

def auto_correct(word, dictionary):
    distances = []
    for dict_word in dictionary:
        distance = levenshtein_distance(word, dict_word)
        distances.append((dict_word, distance))
    
    distances.sort(key=lambda x: x[1])
    return distances[0][0]

# Example usage
dictionary = ['apple', 'banana', 'cherry', 'date', 'elderberry']

input_word = input("Enter a word: ")
suggested_word = auto_correct(input_word, dictionary)

print(f"Suggested word: {suggested_word}")


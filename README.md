# Auto-Correct-Tool
Python project that utilizes AI to create an Auto Correct tool. This project uses the Levenshtein distance algorithm to find the nearest words to the input word and suggests corrections based on those distances. You can run this code in a Jupyter notebook.

Here's a breakdown of the project:

The levenshtein_distance function calculates the Levenshtein distance between two strings. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another.

The auto_correct function takes an input word and a dictionary of valid words. It calculates the Levenshtein distance between the input word and each word in the dictionary and stores the distances along with the corresponding words in a list.

The list of distances and words is sorted in ascending order based on the distances, so the word with the smallest distance (i.e., the nearest word) appears first in the list.

The suggested word is extracted from the sorted list and returned as the output.

In the example usage section, the code prompts the user to enter a word. It then calls the auto_correct function with the input word and the dictionary of words. The suggested word is printed as the output.

The Levenshtein distance algorithm is a simple yet effective method for finding the nearest words based

![image](https://github.com/vrushabhdhote29/Auto-Correct-Tool/assets/92002956/19e50da9-257d-4f6d-b765-3edc2a1b0588)

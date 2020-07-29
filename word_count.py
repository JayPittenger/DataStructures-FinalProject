# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

# Jay Pittenger
# CS 261 - Spring 2020
# Assignment 5 pt.2

import re
from hash_map import HashMap
"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")


def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500, hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    # build hash table
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # convert to lowercase so words are counted properly
                lowercase_w = w.lower()
                keys.add(lowercase_w)
                word_count = ht.get(lowercase_w)
                # have value of node track number of times word has appeared
                if word_count is None:
                    ht.put(lowercase_w, 1)
                else:
                    ht.put(lowercase_w, word_count + 1)
    # for the amount of top words requested, find the word with maximum count
    max_list = []
    for count in range(number):
        max_w = ""
        max_value = 0
        # iterate over all words to find max key, value
        for w in keys:
            value = ht.get(w)
            if value > max_value:
                max_key = w
                max_value = value
        max_list.append((max_key, max_value))
        # remove max word from set for next iteration to get next top word
        keys.remove(max_key)
    return max_list

print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE


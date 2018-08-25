from collections import Counter

def palindrome_permutation(string):
    lowerString = string.lower()
    #Creates a dictionary with the count of each character
    dict_counter = Counter(lowerString)
    even_counter = 0
    for keys in dict_counter.keys():
        if dict_counter[keys] % 2 != 0:
            even_counter += 1
    if even_counter > 1:
        print(False)
        return False
    else:
        print(True)
        return True

palindrome_permutation("tactcoa")
palindrome_permutation("Hello")

##This function has a O(n) runtime.
##The idea is that a palindrome would have at most, one character with an odd count.
##If there is more than one character with an odd count, the string cannot be a palindrome.
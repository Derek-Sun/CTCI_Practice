
def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        print(False)
        return False
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)
    for position in range(len(sorted1)):
        if sorted1[position] != sorted2[position]:
            print(False)
            return False
    print(True)
    return True

checkPermutation("Apple", "ppleA")

checkPermutation("Bobcat", "catBob")

checkPermutation("Hello", "There")

##Check Permutation has O(n Log(n)) Runtime.
##In the best case scenario, when the length is given, the runtime can be O(1).
##The sorting takes up the time in this function.
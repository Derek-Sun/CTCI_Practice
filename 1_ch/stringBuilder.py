import random
import time

#Create Random List of String
def stringRNG(length):
    stringList = []
    for listLength in range(length):
        stringLength = random.randint(1,25)
        word = ''
        for letter in range(stringLength):
            randomLetter = random.randint(97,123)
            word += chr(randomLetter)
        stringList.append(word)
    return stringList

#Conventional Builder
def conventionalBuilder(stringList):
    newString = ''
    time_start = time.time()
    for strings in stringList:
        newString += strings
    time_end = time.time()
    elapsed_time = time_end - time_start
    print ("Conventional Builder {}".format(elapsed_time))

#String Builder
#Takes a List of String as Argument
def stringBuilder(stringList):
    newString = []
    time_start = time.time()
    for strings in stringList:
        newString.append(strings[:])
    time_end = time.time()
    elapsed_time = time_end - time_start
    print ("String Builder {}".format(elapsed_time))

list = stringRNG(200000)

conventionalBuilder(list)
stringBuilder(list)


##The Conventional String Builder is more efficient in Python due to how the compiler works.
##In other languages, String Builder is necessary to create a more efficient string concatenation.
##The Conventional String Builder would take O(n^2) time because the immutable strings are copied over again.
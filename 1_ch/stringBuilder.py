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
    print (time_end - time_start)

#String Builder
#Takes a List of String as Argument
def stringBuilder(stringList):
    newString = []
    time_start = time.time()
    for strings in stringList:
        newString.append(strings[:])
    time_end = time.time()
    print (time_end - time_start)

list = stringRNG(2000000)

conventionalBuilder(list)
stringBuilder(list)
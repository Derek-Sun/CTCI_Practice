#Sort Method
def sortMethod(string):
    sorted_string = sorted(string)
    print(sorted_string)
    for character in range(len(sorted_string) - 1):
        if sorted_string[character] == sorted_string[character + 1]:
            print(False)
            return
    print(True)

#This method results in O(n Log(n)) runtime. The sorting takes roughly O(n Log(n)).
#The character looping through array takes O(n) runtime.

sortMethod("Hello")

sortMethod("Hogwarts")
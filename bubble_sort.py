
a = [6,2, 9, 10, 1]

def bubblesort(myList):
    for i in range(0, len(myList)):
        for j in range(0, len(myList) - 1):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp

    return myList

print(bubblesort(a))

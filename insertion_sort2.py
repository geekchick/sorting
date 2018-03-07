a = [6,2, 9, 10, 1]

def insertionsort(mylist):
    for i in range(1, len(mylist)):
        print("This is i {}".format(i))
        #print("This is i len(mylist) {}".format(str(len(mylist)+ 1)))
        j = i - 1
        print("This is j {}".format(j))
        print("mylist[i] = {} and mylist[j] = {}".format(mylist[i], mylist[j]))
        while j >= 0 and mylist[i] < mylist[j]:
            temp = mylist[i]
            #print("This is temp {}".format(temp))
            mylist[j + 1] = mylist[j]
            j = j - 1
            mylist[j + 1] = temp
            i = i - 1
        print(mylist)

    #return mylist

print(insertionsort(a))
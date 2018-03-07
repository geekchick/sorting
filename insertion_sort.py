a = [6,2, 9, 10, 1]

def insertionsort(mylist):
    for i in range(1, len(mylist)):
        print("This is i {}".format(i))
        print("This is i len(mylist) {}".format(str(len(mylist)+ 1)))
        for j in range(0, len(mylist)):
            print("This is j {}".format(j))
            print("This is j len(mylist) {}".format(str(len(mylist))))
            if mylist[i] < mylist[j]:
                #swap
                temp = mylist[i]
                print("This is temp {}".format(temp))
                mylist[i] = mylist[j]
                print("This is mylist[i + 1]".format(mylist[i]))
                mylist[j] = temp
                print("This is mylist[j]".format(mylist[j]))
                print("This is my new list {}".format(mylist))

    #return mylist

print(insertionsort(a))
#SORT LIST CHALLENGE (i worked on an app instead)
unsortedList = [5,4,2,9,8,6,7,1,3]


def sortASC(list):
    sorted = False
    counter = 0
    while sorted == False:

        for i in list:
            print(counter)
            if counter == len(list):
                print("sorted")
                print(list)

            elif list[i] > list[i+1]:

                buffer = list[i]
                list[i] = list[i+1]
                list[i+1] = buffer

            else:
                pass


def sortDESC(list):
    sorted = False
    while sorted == False:
        print("hello")

sortASC(unsortedList)
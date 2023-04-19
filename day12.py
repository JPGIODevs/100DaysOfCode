#SORT LIST CHALLENGE (i worked on an app instead)
unsortedList = [5,4,2,9,8,6,7,1,3]


def sort(list, sortType: str):
    sorted = False
    counter = 0
    
    if sortType == "asc":
        while(sorted == False):

            counter+=1
            errors = 0
            
            for i in range(len(list)-1):
                
                if (list[i] > list[i+1]):
                    errors+=1
                    buffer = list[i]
                    list[i] = list[i+1]
                    list[i+1] = buffer

                else:
                    pass


            if errors == 0:
                print("list is sorted :)")
                sorted = True
                return list

            else:
                pass

    elif sortType == "desc":
        while(sorted == False):

            counter+=1
            errors = 0
            
            for i in range(len(list)-1):
                
                if (list[i] < list[i+1]):
                    errors+=1
                    buffer = list[i]
                    list[i] = list[i+1]
                    list[i+1] = buffer

                else:
                    pass


            if errors == 0:
                print("list is sorted :)")
                sorted = True
                return list

            else:
                pass    
   



def main():

    running = True

    while(running):

        try:
            choice = input("asc, desc or none?")
            
            if(choice.lower() == "asc"):
                print("You have chosen to ascending sort...")
                sortedList = sort(unsortedList, choice)
                print(f"the final list is {sortedList}")
                running = False

            elif(choice.lower() == "desc"):
                print("You have chosen to descending sort...")
                sortedList = sort(unsortedList, choice)
                print(f"the final list is {sortedList}")
                running = False

            elif(choice.lower() == "none"):
                print(f"{unsortedList} is not sorted :)")
            

        except:
            print("Incorrect input, try again :)\n")

main()


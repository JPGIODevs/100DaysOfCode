
import os

#central function and initiator
def __init__():

    with open ("counter.txt") as f:
        count = int(f.read())
        print(f"first open is {count}")
        f.close()

    cleanUp(count)

    newCount = writeFile(count)
    print (f"new count written is {newCount}")

#function used to take arguement of count, add 1 and rewrite to file
#used for the function of indexing and aiding in cleaning up past automatic posts
def writeFile(count):
    with open ("counter.txt", "w") as f:
        newCount=str(count+1)
        f.write(newCount)

        return newCount

def cleanUp(count: int):
    try:
        
        currentPic = "picture"+str(count)+".png"
        print(currentPic)

        location = "/Users/jxck/Desktop/computer shit/ongoing/ainsta/topost"

        path = os.path.join(location, currentPic)
        os.remove(path)

    except:

        print("error in cleanUp function was handled, proceed with caution")
        pass



#POST FILE (GENERIC) ////////////////////////////
__init__()
import os

textPath = "100daysofcode/test/test.txt"


with open (textPath) as f:
    print(f.read())
    f.close()

# it was this easy? ^^^


if(os.path.exists("100daysofcode/appResources") == False):

    os.mkdir("100daysofcode/appResources")
    os.mkdir("100daysofcode/appResources/items")
    os.mkdir("100daysofcode/appResources/photos")

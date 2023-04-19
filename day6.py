import pandas as pd

data = {
    'cars': ["BMW", "volvo", "ford"],
    'passings': [3,7,2]
}

a = [1,7,2]

calories = {"day1":420, "day2":565, "day3":982}



myvar = pd.DataFrame(data, index = ["index1","index2" ,"index3"])
#myvar = pd.Series(a) <- series of a, labeled 0-100 or whatevs
#myvar = pd.Series(a, index = ["x", "y", "z"]) <-same labeled xyz
#myvar = pd.Series(calories, index=["day1","day2"])

print(myvar.loc["index2"])
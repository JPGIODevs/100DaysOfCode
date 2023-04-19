import pandas as pd
import numpy as np
import matplotlib as plt
import sklearn
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle



# import csv file via pandas, seperated by ";" as in file to get values + read
data = pd.read_csv("/Users/jxck/Desktop/computer shit/ongoing/100daysofcode/student-mat.csv", sep=";")
print (data.head())

# strip data down to wanted attributes (not all 33) + read
data = data[["G1","G2","G3", "studytime", "famrel","failures"]]
print (data.head())
# out "want to predict" variable, known widely as label
predict = "G3"

x = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])

# creating 4 arrays from our label and features
# trimming selection of test to 10%
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size = 0.1)

# creating and implementing linear-regression algorithm
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

# measuring R / accuracy of linear-regression model 
# with out chosen label&features
accuracy = linear.score(x_test, y_test)
print(accuracy)

print ('Coefficient: \n', linear.coef_)
print ('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
#for x in range(len(predictions)):
    #print(predictions[x], x_test[x], y_test[x])

with open("/Users/jxck/Desktop/computer shit/ongoing/100daysofcode/studentgrades.pickle", "wb") as f:
    pickle.dump(linear, f)


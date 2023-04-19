import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


#import csv file via pandas, seperated by ";" as in file to get values
data = pd.read_csv("/Users/jxck/Desktop/computer shit/ongoing/100daysofcode/student-mat.csv", sep=";")

print (data.head())

#strip data down to wanted attributes (not all 33)
data = data[["G1","G2","G3", "studytime", "famrel","failures"]]

#out "want to predict" variable, known widely as label
predict = "G3"

print (data.head())
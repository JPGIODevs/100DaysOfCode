import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#arrays for scatter plot
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21 ,21]

#classes 2D array for colours, used by C modifier of the pyplot scatter function
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

#make a list from the zipped function of the two tuples, x and y
data = list(zip(x,y))

#create KNN classifier and fit DATA and classes
knn = KNeighborsClassifier(n_neighbors=5) 
#^^changing neighbors to 5 will change classification of new point
#^^ more neighbors help increase size of scope, increased scope results in higher accuracy of classification
knn.fit(data, classes)

new_x = 8
new_y = 21
#create list from tuple of 8 and 21, which are the new x and y coords respectively
new_point = [(new_x, new_y)]

#create prediction for our new point above
prediction = knn.predict(new_point)


#map and apply text to all data above :)
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()
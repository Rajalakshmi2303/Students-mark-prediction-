from sklearn.linear_model import linear regression
import numpy as np
#study hours(input)
hours=np.array([[1],[2],[3],[4],[5]])
#marks(output)
marks=np.array([30,40,50,60,70])
#create model
model=linear regression( )
#train model
model.fits(hours,marks)
#user input
h=float(input("enter study hours; "))
#predict
prediction=model.predict([[h]])
print("predicted marks;",int(prediction[0]))
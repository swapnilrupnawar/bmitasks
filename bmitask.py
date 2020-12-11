
import numpy as np
import pandas as pd


data={"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },  { "Gender": "Male", "HeightCm": 161,
"WeightKg": 85 },  { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},  {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},  {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}


data=pd.DataFrame(data)


print(data)




BMI = data['WeightKg']/((data['HeightCm']/100)**2)


type(BMI)
print(BMI)


for i in BMI:
    if i< 18.4:
        print('underweight')
    elif i<24.9:
        print('Normal weight')
    elif i<29.9:
        print('overweight')
    elif i<34.9:
        print('Moderately obese')
    elif i<29.9:
        print('Severely obese')
    else:
        print('very severely obese')


print(data)



data['BMI'] = BMI



print(data)



data['Gender']



data['BMI']


def category(x):

    for i in BMI:
        if i< 18.4:
            print('underweight')
        elif i<24.9:
            print('Normal weight')
        elif i<29.9:
            print('overweight')
        elif i<34.9:
            print('Moderately obese')
        elif i<39.9:
            print('Severely obese')
        else:
            print('very severely obese')



category(BMI)



data['overweight']= data['BMI']<29.9



data['underweight']=data['BMI']<18.9
data['Normalweight']=data['BMI']<24.9
data['Moderetaly obese']=data['BMI']<34.9
data['Severely obese']=data['BMI']<39.9

#pd.concat(data['overweight'],data['underweight'],data['Normalweight'],data['Moderetaly obese'],data['Severely obese'])


print(data[data['overweight']>0])






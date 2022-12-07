import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# This program calculates entropy of classes in mushroom dataset


def H(distribution):

    # computes Shannon's entropy of a distribution: a numpy array/list
    entropy=0.0
    for dist in distribution:
        if dist==0.0:
            entropy+=0
        else:
            entropy+=dist*math.log(dist,2)
    return -entropy


def calculate_class_entropy(data):
    # create a frequency dictionary of classes
    classes={}
    data_len=len(data)
    print("Data Length: ", data_len)
    for index, datapoint in data.iterrows():
        # print(index,datapoint['class'])
        if datapoint['class'] in classes:
            classes[datapoint['class']]+=1
        else:
            classes[datapoint['class']]=1
    print(classes)
    # calculate probablity distribution for classes
    classes_prob=[]
    for c in classes:
        prob=classes[c]/data_len
        classes_prob.append(prob)
    print("Entropy of classes in Mushroom: ", H(classes_prob))


df=pd.read_csv("mushrooms.csv")
labelencoder=LabelEncoder()
for column in df.columns:
    # print(df[column])
    df[column]=labelencoder.fit_transform(df[column])
# After replacing categories of features by ordinal values
print("After replacing categories of features by ordinal values")
print(df.head)
# Calculating entropy for classes
calculate_class_entropy(df)

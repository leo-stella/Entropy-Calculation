import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def H(distribution):
    # computes Shannon's entropy of a distribution: a numpy array/list
    entropy=0.0
    for dist in distribution:
        if dist==0.0:
            entropy+=0
        else:
            entropy+=dist*math.log(dist,2)
    return -entropy


def calculate_feature_entropy(data, feature):
    feature_values = {}
    # Here we will store frequencies of feature values
    # Iterate the dataset to get each data point
    for index,data_point in data.iterrows():
        # Get data row of this feature and the row class
        ft=data_point[feature]
        cls=data_point['class']
        # Calculate frequency for each feature values
        if ft in feature_values:
            # feature_values[data_point[feature]]+=1
            feature_values[ft]['count']+=1
            if cls in feature_values[ft]['classes']:
                feature_values[ft]['classes'][cls]+=1
            else:
                feature_values[ft]['classes'][cls] = 1
        else:
            feature_values[ft]={}
            feature_values[ft]['count']=1
            feature_values[ft]['classes']={}
            feature_values[ft]['classes'][cls]=1

    print("******************Feature Name*******", feature)
    for feature_value, feature_stats in feature_values.items():
        print("****Feature value is*****:", feature_value)
        prob=[]
        total=feature_stats['count']
        for feature_class, feature_count in feature_stats['classes'].items():
            prob.append(feature_count/total)
        print("******Probability distribution*****")
        print(prob)
        print("****Entropy:*****")
        print(H(prob))


# Load dataset using pandas
df=pd.read_csv("mushrooms.csv")
# print(df.head)
labelencoder=LabelEncoder()
for column in df.columns:
    # print(df[column])
    df[column]=labelencoder.fit_transform(df[column])
# After replacing categories of features by ordinal values
# print("After replacing categories of features by ordinal values")
# print(df.head)
feature='cap-shape'
calculate_feature_entropy(df, feature)

# Entropy-Calculation

Basic building blocks for constructing a decision tree using ID3 algorithm as oppose to CART. 

ID3 takes discrete features and calculates Information Gain differently than CART.

## Question 1

Write a program to calculate entropy of London weather.


## Question 2

Write a program to calculate entropy of classes in UCI mushroom dataset

## Question 3

Write a program to calculate entropy of features for mushroom dataset.

### Steps

1- Load the dataset using pandas.read_csv(filename) .

2- Convert labels to numbers using LabelEncoder.fit_transform() object.

3- Count frequency for each class and construct a probablity distribution shown in calculate_class_entropy function in entropy_of_class.py file.



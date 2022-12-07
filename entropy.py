import math


def H(distribution):
    # computes Shannon's entropy of a distribution: a numpy array/list
    entropy=0.0
    for dist in distribution:
        if dist==0.0:
            entropy+=0
        else:
            entropy+=dist*math.log(dist,2)
    return -entropy

# Demonstration of entropy using weather values of london
snow=1/16
showers=1/8
light_rain=1/8
wet=1/8
misty=1/8
cloudy=1/8
breezy=1/8
bright=1/8
sunny=1/16
# Probability distribution of London weather must sum to 1
X_LDN=[snow, showers, light_rain, wet, misty, cloudy, breezy, bright,sunny]

print("Entropy of London is:", H(X_LDN))
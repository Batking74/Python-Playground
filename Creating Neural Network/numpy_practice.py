import numpy as np

w1 = np.random.rand()
w2 = np.random.rand()
b = np.random.rand()

def sigmoid(x): return(1 / (1 + np.exp(-x)))

def Neural_Network(data1, data2, weight1, weight2, bias):
    z = (data1 * weight1) + (data2 * weight2) + bias
    return sigmoid(z)

Neural_Network(3, 1.5, w1, w2, b)


print(sigmoid(-2))

def cost(b):
    return (b - 4) ** 2

def num_slope(b):
    stepSize = 0.0001
    return (cost(b+stepSize) - cost(b)) / stepSize

def slope(b):
    return 2 * (b - 4)

b = 8

# for i in range(1):
#     b = b - .1 * slope(b)
#     print(b)




# singmoid algorithm: The purpose of sigmoid function is to get a number between 0 and 1
# Cost functions: Math.pow(prediction - target, 2)
    # cost function note: (Bias - target) rasied to the power of 2
# num_slope function note: We can subtract the slope of the cost function to determine how we should change 'b' aka bias (increase it or decrease it)
    # num_slope function note: The closer "b" is to target the lower the cost
# num_slope return statement note: if "b" is below the target value then the output will be negative and if its higher than the target value it will be positive
# Test: print(num_slope(1))
# Test: slope(19)
# for loop note: Training loop (Minimizing the cost) Trains the Neural Network
# numpy list/arrays are faster than using regular lists because first numpy#
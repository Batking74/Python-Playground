import numpy as np

# Modeling 1 neuron with 3 inputs

# Each input represents a unique output from a neuron from the previous layer
inputs = [1, 2, 3]

# Every input has its own unique weight to it (To know how many neurons there are count the num of arrays in weights variable.)
weights = [0.2, 0.8, -0.5]

# Every unique neuron has its own unique bias only 1 bias per neuron
bias = 2

# This is how the calculation is done under the hood
output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)




# Modeling 3 neuron with 4 inputs
inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
biases = [2, 3, 0.5]
layer_outputs = []

# Algorithm for calaculating dot product
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)




# Modeling 1 neuron with 4 inputs
inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

# Dot product of 1 neuron using two vectors/1D Arrays
output = np.dot(weights, inputs) + bias
print(output)




# Modeling 3 neuron with 4 inputs
inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
biases = [2, 3, 0.5]

# The number of columns in the first array must be equal to the number of rows in the another array for the dot() method to work.
# if you have a maxtrix and a vector array the matrix array will always come first
# Dot product of 3 neurons using a maxtrix/2D Array and vector/1D Array
output = np.dot(weights, inputs) + biases
print(output)








inputs = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]
# Layer 1
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]
# End of Layer 1

# Layer 2
weights2 = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13]]

biases2 = [1, 2, -0.5]
# End of Layer 2

layer1_output = np.dot(inputs, np.array(weights).T) + biases


layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

print(layer2_output)
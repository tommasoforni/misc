import numpy as np
from numpy import tanh,random,sin,outer,tan,cos
import matplotlib.pyplot as plt

class neuralLayer:
    def __init__(self,neurons, connections_per_neuron):
        self.neurons = neurons
        self.connections_per_neuron = connections_per_neuron
        self.weights = random.random((connections_per_neuron,neurons))-1
        self.oldw = np.zeros((connections_per_neuron,neurons))
        self.output = np.empty(neurons)
        self.delta = np.empty(neurons)

class neuralNetwork:
    def __init__(self,hidden1,outputLayer):
        self.layer1 = hidden1
        self.layer2 = outputLayer
        self.layer0 = np.array(self.layer1.connections_per_neuron)
        self.expected = 0. #np.zeros(self.layer2.neurons)
        self.learning_rate = 0.1
        self.momentum = 0.02
        self.errors = []

    def derivative(self,x):
        return 1-x*x

    def propagate(self):
        self.layer1.output = tanh(self.layer0.dot(self.layer1.weights))
        self.layer2.output = tanh(self.layer1.output.dot(self.layer2.weights))
        
    def changeInput(self):
        self.layer0 = 2*random.random(self.layer1.connections_per_neuron)-1
        self.expected = sin(self.layer0[0]+self.layer0[1])
            
    def train(self,iterations):
        for i in range(iterations):
            self.changeInput()
            self.propagate()

            error = self.expected-self.layer2.output
            print(error)
            self.errors.append(error)
            self.layer2.delta = self.derivative(self.layer2.output)*error
            self.layer1.delta = self.derivative(self.layer1.output)*(self.layer2.weights.dot(self.layer2.delta))


            change = self.learning_rate*outer(self.layer1.output, self.layer2.delta) +self.momentum*self.layer2.oldw
            self.layer2.weights += change
            self.layer2.oldw = change
            change = self.learning_rate*outer(self.layer0, self.layer1.delta) +self.momentum*self.layer1.oldw
            self.layer1.weights += change
            self.layer1.oldw = change
            
        plt.plot(self.errors)
        plt.show()


hidden1 = neuralLayer(100,2)
out = neuralLayer(1,100)

perceptron = neuralNetwork(hidden1,out)
perceptron.train(100000)

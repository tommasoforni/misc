import numpy as np
from numpy import tanh,random,sin,outer
import matplotlib.pyplot as plt

class neuralLayer:
    def __init__(self,neurons, connections_per_neuron):
        self.neurons = neurons
        self.connections_per_neuron = connections_per_neuron
        self.weights = random.random((connections_per_neuron,neurons))-1
        self.output = np.empty(neurons)
        self.delta = np.empty(neurons)

class neuralNetwork:
    def __init__(self,hidden1,hidden2,outputLayer):
        self.layer1 = hidden1
        self.layer2 = hidden2
        self.layer3 = outputLayer
        self.layer0 = np.array(self.layer1.connections_per_neuron)
        self.expected = 0. #np.zeros(self.layer2.neurons)
        self.learning_rate = 0.01
        self.momentum = 0
        self.errors = []

    def derivative(self,x):
        return 1-x*x

    def propagate(self):
        self.layer1.output = tanh(self.layer0.dot(self.layer1.weights))
        self.layer2.output = tanh(self.layer1.output.dot(self.layer2.weights))
        self.layer3.output = tanh(self.layer2.output.dot(self.layer3.weights))

        
    def changeInput(self):
        self.layer0 = 2*random.random(self.layer1.connections_per_neuron)-1
        self.expected = sin(self.layer0[0]-self.layer0[1]+self.layer0[2])
            
    def train(self,iterations):
        for i in range(iterations):
            self.changeInput()
            self.propagate()

            error = self.expected-self.layer3.output
            print(error)
            self.errors.append(error)
            self.layer3.delta = self.derivative(self.layer3.output)*error
            
            self.layer2.delta = self.derivative(self.layer2.output)*(self.layer3.weights.dot(self.layer3.delta))
    
            self.layer1.delta = self.derivative(self.layer1.output)*(self.layer2.weights.dot(self.layer2.delta))
            
            self.layer3.weights += self.learning_rate*outer(self.layer2.output, self.layer3.delta) +self.momentum*self.layer3.weights
            
            self.layer2.weights += self.learning_rate*outer(self.layer1.output, self.layer2.delta) +self.momentum*self.layer2.weights
            
            self.layer1.weights += self.learning_rate*outer(self.layer0, self.layer1.delta) +self.momentum*self.layer1.weights
            
        plt.plot(self.errors)
        plt.show()


hidden1 = neuralLayer(10,3)
hidden2 = neuralLayer(10,10)
out = neuralLayer(1,10)

perceptron = neuralNetwork(hidden1,hidden2,out)
perceptron.train(100000)

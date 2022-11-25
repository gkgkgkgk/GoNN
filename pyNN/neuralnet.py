import math 

class NeuralNetwork:
    def __init__(self, inputNodeCount, hiddenNodeCount, outputNodeCount):
        self.inputNodeCount = inputNodeCount
        self.hiddenNodeCount = hiddenNodeCount
        self.outputNodeCount = outputNodeCount
        self.hiddenNodes = []
        self.outputNodes = []
        self.activations_hidden = []
        self.outs = []

    def populateWeights(self, hiddenNodes, outputNodes):
        for _, weights in enumerate(hiddenNodes):
            self.hiddenNodes.append(Neuron(weights))
        for _, weights in enumerate(outputNodes):
            self.outputNodes.append(Neuron(weights))
    
    def sigmoid(self, x):
        return (1/(1+math.exp(-x)))
    
    def sigmoid_prime(self, x):
        return self.sigmoid(x) * (1-self.sigmoid(x))

    def train(self, features, labels, epochs, learningRate):
        for epoch in range(epochs):
            print("Starting epoch " + str(epoch))
            for feature, label in tuple(zip(features, labels)):
                a_hidden = [0] * self.hiddenNodeCount
                a_output = [0] * self.outputNodeCount

                # Forward prop- since there is only one hidden layer, activations can be calculated manually- once for the output layer and once for the output layer
                for j in range(self.hiddenNodeCount):
                    a_hidden[j] = self.sigmoid(self.hiddenNodes[j].summation(feature))

                for j in range(self.outputNodeCount):
                    a_output[j] = self.sigmoid(self.outputNodes[j].summation(a_hidden))
                
                # Backward prop
                for j in range(self.outputNodeCount):
                    self.outputNodes[j].delta = self.sigmoid_prime(self.outputNodes[j].summation(a_hidden)) * (label[j] - a_output[j])

                for i in range(self.hiddenNodeCount):
                    sum = 0
                    for j in range(self.outputNodeCount):
                        sum += self.outputNodes[j].weights[i] * self.outputNodes[j].delta
                    
                    self.hiddenNodes[i].delta = self.sigmoid_prime(self.hiddenNodes[i].summation(feature)) * sum
                
                # Update weights
                for j in range(self.hiddenNodeCount):
                    self.hiddenNodes[j].bias = self.hiddenNodes[j].bias + (learningRate * (-1) * (self.hiddenNodes[j].delta))
                    for w in range(len(self.hiddenNodes[j].weights)):
                        self.hiddenNodes[j].weights[w] = self.hiddenNodes[j].weights[w] + (learningRate * feature[w] * self.hiddenNodes[j].delta)  
                
                for j in range(self.outputNodeCount):
                    self.outputNodes[j].bias = self.outputNodes[j].bias + (learningRate * (-1) * ( self.outputNodes[j].delta))
                    for w in range(len(self.outputNodes[j].weights)):
                        self.outputNodes[j].weights[w] = self.outputNodes[j].weights[w] + (learningRate * a_hidden[w] * self.outputNodes[j].delta)

        print(self.outputNodes[0])

class Neuron:
    def __init__(self, weights):
        self.weights = weights[1:len(weights)]
        self.bias = weights[0]
        self.delta = 0

    def __repr__(self):
        return str(round(self.bias, 3)) +' '+ ' '.join(str(round(weight, 3)) for weight in self.weights)
    
    def summation(self, weights):
        result = 0
        for i in range(len(weights)):
            result += weights[i] * self.weights[i]
        
        result -= self.bias

        return result

class Parser:
    def __init__(self, default=False):
        if default:
            self.initFile = "wdbc/sample.NNWDBC.init.txt"
            self.trainingFile = "wdbc/wdbc.train.txt"
            self.epochs = 100
            self.learningRate = 0.1
        else:
            self.initFile = input("Please enter an initialization file:")
            self.trainingFile = input("Please enter a file to train on:")
            self.epochs = int(input("Please enter an amount of epochs to train for:"))
            self.learningRate = float(input("Please enter the desired learning rate:"))

        self.parseInitFile()

    def parseInitFile(self):
        f = open(self.initFile, "r")
        lines = f.read().splitlines()
        hiddenWeights = []
        outputWeights = []
        inputNodeCount = 0
        hiddenNodeCount = 0
        outputNodeCount = 0

        for i, line in enumerate(lines):
            if i == 0:
                numbers = [int(x) for x in line.split(" ")]
                inputNodeCount = numbers[0]
                hiddenNodeCount = numbers[1]
                outputNodeCount = numbers[2]
            elif i < 1 + hiddenNodeCount:
                weights = [float(x) for x in line.split(" ")]
                hiddenWeights.append(weights)
            elif i < 1 + hiddenNodeCount + outputNodeCount:
                weights = [float(x) for x in line.split(" ")]
                outputWeights.append(weights)
        
        return inputNodeCount, hiddenNodeCount, outputNodeCount, hiddenWeights, outputWeights

    def parseTrainingFile(self):
        f = open(self.trainingFile)
        lines = f.read().splitlines()
        featureCount = 0
        labelCount = 0
        sampleCount = 0

        numbers = [int(x) for x in lines[0].split(" ")]
        sampleCount = numbers[0]
        featureCount = numbers[1]
        labelCount = numbers[2]

        features = []
        labels = []
        for i, line in enumerate(lines[1:sampleCount+1]):
            weights = [float(x) for x in line.split(" ")]
            features.append(weights[0:featureCount])
            # features[i].insert(0, -1)
            labels.append([int(y) for y in weights[featureCount:featureCount + labelCount]])

        return features, labels

# wdbc/sample.NNWDBC.init.txt, wdbc/wdbc.train.txt
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
        self.testing_metrics = [[0,0,0,0,0,0,0,0] for i in range(self.outputNodeCount)]

    def populateWeights(self, hiddenNodes, outputNodes):
        for _, weights in enumerate(hiddenNodes):
            self.hiddenNodes.append(Neuron(weights))
        for _, weights in enumerate(outputNodes):
            self.outputNodes.append(Neuron(weights))
    
    def sigmoid(self, x):
        return (1/(1+math.exp(-x)))
    
    def sigmoid_prime(self, x):
        return self.sigmoid(x) * (1-self.sigmoid(x))

    def train(self, features, labels, epochs, learningRate, outputFile="trained.txt"):
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
    
        f = open(outputFile, "w")
        f.write(str(self.inputNodeCount) + " " + str(self.hiddenNodeCount) + " " + str(self.outputNodeCount)+"\n")
        for node in self.hiddenNodes:
            f.write(str(node) + "\n")
        for node in self.outputNodes:
            f.write(str(node) + "\n")

    def test(self, features, labels, outputFile="results.txt"):
        for feature, label in tuple(zip(features, labels)):
            a_hidden = [0] * self.hiddenNodeCount
            classes_output = [0] * self.outputNodeCount

            for i in range(self.hiddenNodeCount):
                a_hidden[i] = self.sigmoid(self.hiddenNodes[i].summation(feature))

            for i in range(self.outputNodeCount):
                c = 1 if self.sigmoid(self.outputNodes[i].summation(a_hidden)) > 0.5 else 0

                if c == 1 and label[i] == 1:
                    self.testing_metrics[i][0] += 1
                elif c == 1 and label[i] == 0:
                    self.testing_metrics[i][1] += 1
                elif c == 0 and label[i] == 1:
                    self.testing_metrics[i][2] += 1
                elif c == 0 and label[i] == 0:
                    self.testing_metrics[i][3] += 1
        
        for i in range(self.outputNodeCount):
            self.testing_metrics[i][4] = 0 if (self.testing_metrics[i][0] + self.testing_metrics[i][1] + self.testing_metrics[i][2] + self.testing_metrics[i][3]) == 0 else (self.testing_metrics[i][0] + self.testing_metrics[i][3]) / (self.testing_metrics[i][0] + self.testing_metrics[i][1] + self.testing_metrics[i][2] + self.testing_metrics[i][3])
            self.testing_metrics[i][5] = 0 if (self.testing_metrics[i][0] + self.testing_metrics[i][1]) == 0 else (self.testing_metrics[i][0]) / (self.testing_metrics[i][0] + self.testing_metrics[i][1])
            self.testing_metrics[i][6] = 0 if (self.testing_metrics[i][0] + self.testing_metrics[i][2]) == 0 else (self.testing_metrics[i][0]) / (self.testing_metrics[i][0] + self.testing_metrics[i][2])
            self.testing_metrics[i][7] = 0 if (self.testing_metrics[i][5] + self.testing_metrics[i][6]) == 0 else (2 * self.testing_metrics[i][5] * self.testing_metrics[i][6]) / (self.testing_metrics[i][5] + self.testing_metrics[i][6])

        f = open(outputFile, "w")
        for i in range(self.outputNodeCount):
            f.write(" ".join(str(metric) for metric in self.testing_metrics[i][0:4]) + " ")
            f.write(" ".join(str("%.3f" % round(metric, 3)) for metric in self.testing_metrics[i][4:8]) + "\n")

        a = 0
        b = 0
        c = 0
        d = 0

        accuracy = 0
        precision = 0
        recall = 0


        for i in range(self.outputNodeCount):
            a += self.testing_metrics[i][0]
            b += self.testing_metrics[i][1]
            c += self.testing_metrics[i][2]
            d += self.testing_metrics[i][3]

            accuracy += self.testing_metrics[i][4]
            precision += self.testing_metrics[i][5]
            recall += self.testing_metrics[i][6]

        accuracy_micro = (a + d) / (a + b + c + d)
        precision_micro = a / (a + b)
        recall_micro = a / (a + c)
        f1_micro = (2 * precision_micro * recall_micro) / (precision_micro + recall_micro)

        f.write(str("%.3f" % round(accuracy_micro, 3)) + " " + str("%.3f" % round(precision_micro, 3)) + " " + str("%.3f" % round(recall_micro, 3)) + " " + str("%.3f" % round(f1_micro, 3)) + "\n")

        accuracy_macro = accuracy / self.outputNodeCount
        precision_macro = precision / self.outputNodeCount
        recall_macro = recall / self.outputNodeCount
        f1_macro = (2 * precision_macro * recall_macro) / (precision_macro + recall_macro)

        f.write(str("%.3f" % round(accuracy_macro, 3)) + " " + str("%.3f" % round(precision_macro, 3)) + " " + str("%.3f" % round(recall_macro, 3)) + " " + str("%.3f" % round(f1_macro, 3)) + "\n")

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
    def __init__(self, testing=False, default=False):
        if default:
            self.initFile = "data/grades/sample.NNGrades.init.txt" if not testing else "trained.txt"
            self.trainingFile = "data/grades/grades.train.txt" if not testing else "data/grades/grades.test.txt"
            if not testing:
                self.epochs = 100
                self.learningRate = 0.05
            self.outputFile = "output.txt"
        else:
            self.initFile = input("Please enter an initialization file:")
            self.trainingFile = input("Please enter a file to train on:" if not testing else "Please enter a file to test on:")
            if not testing:
                self.epochs = int(input("Please enter an amount of epochs to train for:"))
                self.learningRate = float(input("Please enter the desired learning rate:"))
            self.outputFile = input("Please enter an output file:")

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
            labels.append([int(y) for y in weights[featureCount:featureCount + labelCount]])

        return features, labels
from neuralnet import NeuralNetwork
from neuralnet import Parser

parser = Parser(default=True)
inputNodeCount, hiddenNodeCount, outputNodeCount, hiddenWeights, outputWeights = parser.parseInitFile()

nn = NeuralNetwork(inputNodeCount, hiddenNodeCount, outputNodeCount)
nn.populateWeights(hiddenWeights, outputWeights)

features, labels = parser.parseTrainingFile()
nn.train(features, labels, parser.epochs, parser.learningRate)
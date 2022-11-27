from neuralnet import NeuralNetwork
from neuralnet import Parser

parser = Parser(testing=True, default=False)
inputNodeCount, hiddenNodeCount, outputNodeCount, hiddenWeights, outputWeights = parser.parseInitFile()

nn = NeuralNetwork(inputNodeCount, hiddenNodeCount, outputNodeCount)
nn.populateWeights(hiddenWeights, outputWeights)

features, labels = parser.parseTrainingFile()

nn.test(features, labels, outputFile=parser.outputFile)
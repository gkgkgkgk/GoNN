package main 

func main(){
	inputNodesCount, hiddenNodesCount, outputNodesCount, _, _ := initializeNeuralNetwork()
	trainingData := getTrainingSet()
	epochs := getEpochs()
	learningRate := getLearningRate()

	train(trainingData, epochs, inputNodesCount, hiddenNodesCount, outputNodesCount, learningRate)
}
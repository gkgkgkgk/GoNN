package main 

func main(){
	inputNodes, hiddenNodes, outputNodes := initializeNeuralNetwork()
	trainingData := getTrainingSet()
	epochs := getEpochs()
	learningRate := getLearningRate()

	train(trainingData, epochs, inputNodes, outputNodes, hiddenNodes, learningRate)
}
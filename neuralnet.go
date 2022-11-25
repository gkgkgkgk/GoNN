package main

import (
	"fmt"
	"bufio"
	"strings"
	"strconv"
	"os"
	"log"
	"math"
)

type neuron struct {
	weights []float64
	bias float64
}

func newNeuron(weights []float64, bias float64) *neuron {
	n := neuron{weights: weights, bias:bias}
	return &n
}

func sigmoid(x float64) float64{
	return 1/(1 + math.Exp(-x))
}

func learn(xs []float64, y []int, hiddenNodes int, learningRate float64){
	var weights []float64

	for j := 0; j < hiddenNodes; j++ {
		weights = append(weights, )
	} 
}

func train(trainingData []string, epochs int, inputNodes int, outputNodes int, hiddenNodes int, learningRate float64){
	for i := 0; i < epochs; i++ {
		fmt.Printf("Training Epoch: %d\n", i)

		for _, sample := range trainingData {			
			xs, ys := parseLine(sample, inputNodes, outputNodes)
			learn(xs, ys, hiddenNodes, learningRate)
		}
	}
}

func initializeNeuralNetwork() (inputNodesCount int, hiddenNodesCount int, outputNodesCount int, hiddenNodes neuron, outputNodes neuron){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter the path to the initial neural network:")
	path, _ := reader.ReadString('\n')
	path = path[:len(path)-2]
	path = "files\\wdbc\\sample.NNWDBC.init.txt"
	
	initialFile, err := os.ReadFile(path)

	if err != nil {
        log.Fatalf("%v", err)
    }

	initialData := strings.Split(string(initialFile), "\n")
	nodeCounts := strings.Split(initialData[0], " ")
	for i, node := range nodeCounts {
		nodeInt, err := strconv.Atoi(node)
		if err != nil {
			panic(err)
		}
		
		switch i {
		case 0:
			inputNodesCount = nodeInt
		case 1:
			hiddenNodesCount = nodeInt
		case 2:
			outputNodesCount = nodeInt
		}
	}

	hiddenInitialNodes := initialData[1:1+hiddenNodesCount]

	for i, node := range nodes {
		weights := strings.Split(node, " ")
		for _, weight := range weights {

		}
		hiddenNodes = append(hiddenNodes, )
	}

	outputInitialNodes := initialData[1+hiddenNodesCount:1+hiddenNodesCount + outputNodesCount]

	// xs, _ := parseLine(line, inputNodesCount, outputNodesCount)
	// nodes = append(nodes, xs)
		
	fmt.Printf("Initialized Neural Network with %d input node(s), %d hidden node(s), and %d output node(s).\n", inputNodesCount, hiddenNodesCount, outputNodesCount)

	return
}

func getTrainingSet() (trainingData []string){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter the path to the training set:")
	path, _ := reader.ReadString('\n')
	path = path[:len(path)-2]
	path = "files\\wdbc\\wdbc.train.txt"
	
	trainingFile, err := os.ReadFile(path)

	if err != nil {
        log.Fatalf("%v", err)
    }

	trainingData = strings.Split(string(trainingFile), "\n")[1:]

	return
}

func getEpochs() (epochs int){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter amount of epochs to train for:")
	epochsStr, err := reader.ReadString('\n')	
	epochs, err = convertStringToInt(epochsStr)

	if err != nil {
		panic(err)
	}

	return
}

func getLearningRate() (learningRate float64){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter the desired learning rate:")
	learningRateStr, err := reader.ReadString('\n')	
	learningRate, err = convertStringToFloat(learningRateStr)

	if err != nil {
		panic(err)
	}

	return
}
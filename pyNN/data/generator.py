import random

dataFile = input("Where is the data file? ")
f = open(dataFile, 'r')
data = f.read().splitlines()
numbers = [int(x) for x in data[0].split(" ")]
data = data[1:len(data)]
random.shuffle(data)
inputNodes = numbers[1]
outputNodes = numbers[2]

hiddenNodes = int(input("How many hidden nodes? "))
split = float(input("What should the data split be (please input a number between 0 and 1)? "))
name = input("What is your data set called? ")
print("Generating " + name + " data set with " + str(inputNodes) + " input nodes, " + str(hiddenNodes) + " hidden nodes, and " + str(outputNodes) + " output nodes.")

f.close()

totalCount = len(data)
trainCount = int((1-split) * totalCount)
testCount = totalCount - trainCount

f = open(name + ".train.txt", 'w')
f.write(str(trainCount) + " " + str(inputNodes) + " " + str(outputNodes) + "\n")
for i in range(trainCount):
    f.write(data[i] + "\n")

f.close()

f = open(name + ".test.txt", 'w')
f.write(str(testCount) + " " + str(inputNodes) + " " + str(outputNodes) + "\n")
for i in range(trainCount, trainCount + testCount):
    f.write(data[i] + "\n")

f.close()

f = open(name + ".init.txt", 'w')
f.write(str(inputNodes) + " " + str(hiddenNodes) + " " + str(outputNodes) + "\n")
for i in range(hiddenNodes):
    weights = []
    for j in range(inputNodes + 1):
        weights.append(random.uniform(0, 1))
    
    f.write(" ".join(str("%.3f" % round(weight, 3)) for weight in weights) + "\n")

for i in range(outputNodes):
    weights = []
    for j in range(hiddenNodes + 1):
        weights.append(random.uniform(0, 1))
    
    f.write(" ".join(str("%.3f" % round(weight, 3)) for weight in weights) + "\n")

f.close()
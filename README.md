# PyNN
A simple neural network implemented in Python.

## How to Run
Run ```python3 train.txt```. Enter the initialization file for the neural network, the training file, and the desired hyperparameters.


Then, run ```python3 test.txt``` and follow the instructions in order to train the model. The initialization file should be the trained neural network.

## How to Generate a Custom Dataset
A script called ```generator.py``` can be used to create new datasets. A data set with the first line being the amount of examples, the amount of input nodes, and the amount of output nodes can be used with this script. The iris dataset (as specified below) is used as an example. The generator script creates three new text files: an initialization file, a training file, and a testing file. The initialization file specifies a neural network with uniformly random weights. 

## Testing with the Iris Dataset
This neural network was trained on the classic iris dataset, which can be found [here](https://archive.ics.uci.edu/ml/datasets/iris). I edited the original dataset to have independent binary classifiers, instead of a string as the name. A table of examples is below.
|Sepal length in cm | sepal width in cm | petal length in cm | petal width in cm | Iris Setosa | Iris Versicolour | Iris Virginica|
|---|---|---|---|---|---|---|
|5.1|3.5|1.4|0.2|1|0|0|
|5.1 |2.5| 3.0| 1.1| 0| 1| 0|
|6.5 |3.0 |5.2 |2.0| 0| 0| 1|


## Results of the Iris Dataset
Three trials are documented below. 

### Trial #1
The network had 4 hidden nodes and was trained with a learning rate of 0.1 for 100 epochs.

Micro Averages: 0.867 0.950 0.633 0.760

Macro Averages: 0.867 0.633 0.667 0.650

### Trial #2
The network had 12 hidden nodes and was trained with a learning rate of 0.1 for 100 epochs.

Micro Averages: 0.978 0.967 0.967 0.967

Macro Averages: 0.978 0.963 0.976 0.970


### Trial #3
The network had 12 hidden nodes and was trained with a learning rate of 0.1 for 500 epochs.

Micro Averages: 0.978 0.967 0.967 0.967

Macro Averages: 0.978 0.970 0.967 0.968

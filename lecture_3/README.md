# Janelia ML Course - lecture 3

## Exercises and milestones for lab 3

### Using TensorFlow with Keras for deep learning
1. Make sure you're in your conda environment from last week: `source activate <env-name>`.
1. Make sure numpy is installed:
	`pip install numpy`
   as well as matplotlib:
   	`pip install matplotlib`
3. Install tensorflow:
	`pip install tensorflow`
   and Keras:
    `pip install keras`
4. Open and run the lab\_3.ipynb notebook

### Exercises
1. Use numpy only to construct a multilayer perceptron (MLP) for XOR
2. Use keras to construct an MLP for another 2D dataset and visualize decision boundaries
3. Use keras to construct a convolutional neural network (CNN) for MNIST digit classification

### Notes

**Warning**: For Exercise 3, make sure to rerun the cell that loads the data before running the cell in which you implement your network. This is because in the implementation cell we change the shape of the data, so you need to reset the data to its original shape before running the implementation cell.

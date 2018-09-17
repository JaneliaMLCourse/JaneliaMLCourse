# Janelia ML Course - lecture 1

## Exercises and milestones for lab 1

### Intro Python and programming
1. Have Anaconda (conda) installed
2. git-clone this repository
3. Open and run the Lecture_1.ipynb notebook
4. [Learn numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html)

### Linear regression 1
1. Read [this website about the diabetes dataset](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)
2. and [this website sklearn's Linear Regression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression)
3. Add one or more new features from the dataset, and solve using sklearn's LinearRegression
4. Set up the matrix equation for linear regression with two features
5. Solve the linear system and make sure the results are the same as those you got with sklearn

### Bayes / Naive bayes
1. Run the document classification Naive Bayes example.
2. Play around with it - try with more than the two classes used in the lecture.
3. Make up a simple classification problem, write code to generate synthetic data, and train a naive bayes classifier on your data with sklearn.
4. Make up a different classification problem, and design it so that naive bayes classifier performs poorly. (Hint: make data that violates the assumption that naive bayes makes).

### Probability / statistics
1. Derive Bayes rule. (Hint: start with the equation relating joint distribution to a conditional distribution)
2. Spot and understand the "mistake" on the **Intuition -> math -> stats** slide

### Linear algebra
1. Work through a few examples of 2x2 matrix - vector multiplications by hand.  Compare to results you get in code.
2. if AB=I, then is it the case that BA=I?
3. What is the solution to the 2x2 matrix equation in the slides?

### Linear regression 2
1. Go to the end of Lecture_1.ipynb and find the slides / cells that we didn't go over in the lecture.
2. Run the sklearn code that uses Linear regression to fit a polynomial of degree-3. 
3. Write down the matrix equation (linear system) for 
4. Write code to generate the matrices and vectors for the equation you wrote down in (3).
5. Solve it yourself in code with `np.linalg.lstsq` and make sure you get the same answer as sklearn.

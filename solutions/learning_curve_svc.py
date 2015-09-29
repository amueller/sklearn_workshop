import matplotlib.pyplot as plt

from sklearn.svm import LinearSVC
from sklearn.learning_curve import validation_curve

Cs = [0.00001, 0.0001, 0.001, 0.01, 0.1 , 1, 10]
training_scores, test_scores = validation_curve(LinearSVC(), X, y,
                                                param_name="C", param_range=Cs)
plt.figure()
plot_validation_curve(range(7), training_scores, test_scores)
plt.xticks(range(7), Cs);

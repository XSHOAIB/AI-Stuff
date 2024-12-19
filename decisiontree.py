import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# 1. Load the Iris dataset
data = load_iris()
X = data.data  # Features
y = data.target  # Labels

# 2. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize the Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# 4. Train the model on the training data
clf.fit(X_train, y_train)

# 5. Make predictions on the test data
y_pred = clf.predict(X_test)

# 6. Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Decision Tree: {accuracy * 100:.2f}%")

# 7. Visualize the decision tree
plt.figure(figsize=(12,8))
tree.plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.show()

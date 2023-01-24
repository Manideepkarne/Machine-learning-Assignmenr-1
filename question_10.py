X = [[1],[2],[3],[6],[6],[7],[10],[11]]
y = [0,0,1,1,1,0,0,0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

from sklearn.neighbors import KNeighborsClassifier
N = 3
neigh = KNeighborsClassifier(n_neighbors=N)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)

print("predicted values : ",y_pred)

from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

"""
Sensitivity/recall – how good a test is at detecting the positives. A test can cheat and maximize this by always returning “positive”.
Specificity – how good a test is at avoiding false alarms. A test can cheat and maximize this by always returning “negative”.
"""
# Accuracy
Accuracy = (tp+tn)/len(y_test)
### sensitivity or recall
Sensitivity = tp/(tp+fn)
Specificity = tn/(fp+tn)

print("Accuracy : ", Accuracy)
print("Sensitivity : ", Sensitivity)
print("Specificity : ", Specificity)
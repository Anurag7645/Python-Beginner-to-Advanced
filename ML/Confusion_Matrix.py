
Y_test=[1,0,1,1,1,0,0,0,1,0,1]
Y_pred=[1,0,0,1,0,1,0,1,1,1,1]

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test, Y_pred)

from sklearn.metrics import classification_report
print(classification_report(Y_test, Y_pred))

from sklearn.metrics import accuracy_score
accuracy_score(Y_test, Y_pred)
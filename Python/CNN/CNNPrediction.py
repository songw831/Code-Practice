import tensorflow as tf
import CNNTrain

model=tf.keras.models.load_model('./myCNNModel.h5')
x_test=CNNTrain.testData
y_true=CNNTrain.testLabel
y_predict=model.predict(x_test)

# evaluation
TP = 0
FN = 0
FP = 0
TN = 0

for i in range(len(y_true)):
    if y_predict[i][1] >= .5 and y_true[i][1] == 1:
        TP += 1
    elif y_predict[i][1] >= .5 and y_true[i][0] == 1:
        FP += 1
    elif y_predict[i][1] < .5 and y_true[i][1] == 1:
        FN += 1
    elif y_predict[i][1] < .5 and y_true[i][0] == 1:
        TN += 1
accuracy = (TP + TN) / (TP + FP + FN + TN)
sensitivity = TP / (TP + FN)
specificity = TN / (FP + TN)
print(accuracy, sensitivity, specificity)

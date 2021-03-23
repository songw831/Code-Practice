import tensorflow as tf
import numpy as np


def loadData():
    trainData=np.loadtxt("./trainData.txt")
    testData=np.loadtxt("./testData.txt")
    trainLabel=np.loadtxt("./trainLabel.txt")
    testLabel=np.loadtxt("./testLabel.txt")
    totalTrain=int(np.size(trainData,0)/length)
    totalTest=int(np.size(testData,0)/length)
    train3Data=np.ndarray(shape=(totalTrain,length,width))
    train3Label=np.ndarray(shape=(totalTrain,2))
    test3Data=np.ndarray(shape=(totalTest,length,width))
    test3Label=np.ndarray(shape=(totalTest,2))
    for i in range(totalTrain):
        train3Data[i]=trainData[i*length:(i+1)*length]
        tmp=trainLabel[i*length:(i+1)*length]
        if sum(tmp)<length/2 :
            train3Label[i][0] = 1
            train3Label[i][1] = 0
        else:
            train3Label[i][0] = 0
            train3Label[i][1] = 1
    for i in range(totalTest):
        test3Data[i]=testData[i*length:(i+1)*length]
        tmp=testLabel[i*length:(i+1)*length]
        if sum(tmp) < length / 2 :
            test3Label[i][0]=1
            test3Label[i][1] = 0
        else:
            test3Label[i][0]=0
            test3Label[i][1] = 1
    return train3Data,test3Data,train3Label,test3Label


class MyRNN(object):
    def __init__(self):
        self.model=tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.LSTM(100,input_shape=(length,width),return_sequences=True))
        self.model.add(tf.keras.layers.LSTM(50, input_shape=(length, width), return_sequences=False))
        self.model.add(tf.keras.layers.Dense(2,activation='softmax'))

#define Multivariate Time Series dimension
length=20
width=14
trainData, testData, trainLabel, testLabel=loadData()

if __name__=="__main__":
    myModel=MyRNN()
    model=myModel.model
    model.summary()  #show model summary
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(trainData, trainLabel, epochs=50, batch_size=32)
    model.save("./myRNNModel.h5")
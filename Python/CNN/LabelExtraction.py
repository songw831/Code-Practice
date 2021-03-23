#!/usr/bin/env python3

import numpy as np
import pandas as pd

partition=0.8

data=pd.read_csv("./RawData.txt")
#data.drop(columns="date",inplace=True,axis=1)
data=data.values
length=10*int(data.shape[0]*partition/10)
trainData=data[:length]
testData=data[length:]

trainInput=trainData[:,:-1]
trainInput=pd.DataFrame(trainInput)
trainInput=(trainInput-trainInput.mean())/trainInput.std()
trainInput=trainInput.values
trainLabel=trainData[:,-1]

testInput=testData[:,:-1]
testLabel=testData[:,-1]
testInput=pd.DataFrame(testInput)
testInput=(testInput-testInput.mean())/testInput.std()
testInput=testInput.values

np.savetxt("trainData.txt",trainInput)
np.savetxt("testData.txt",testInput)
np.savetxt("trainLabel.txt",trainLabel)
np.savetxt("testLabel.txt",testLabel)

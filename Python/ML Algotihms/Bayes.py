import numpy as np


def loaddataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],['maybe','not','take','him','to','dog','park','stupid'],
    ['my','dalmation','is','so','cute','I','love','him'],['stop','posting','stupid','worthless','garbage'],
     ['mr','licks','ate','my','steak','how', 'to','stop','him'],['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec

def createVocalList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

def setWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList: returnVec[vocabList.index(word)]=1
        else: print('This word %s is not in my Vocabulary!'% word)
    return  returnVec


def train(trainMatrix, trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAb=sum(trainCategory)/float(numTrainDocs)
    p0Num=np.ones(numWords)
    p1Num=np.ones(numWords)
    p0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
    p1Vec=np.log(p1Num/p1Denom)
    p0Vec=np.log(p0Num/p0Denom)
    return p0Vec,p1Vec,pAb


def  classify(vecClassify,p0Vec,p1Vec,pClass1):
    p1=sum(vecClassify*p1Vec)+np.log(pClass1)
    p0=sum(vecClassify*p0Vec)+np.log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0



if __name__ == '__main__':
    listPosts,listClasses=loaddataSet()
    myVocabList=createVocalList(listPosts)
    trainMat=[]
    for postdoc in listPosts:
        trainMat.append(setWords2Vec(myVocabList,postdoc))
    p0V,p1V,pAb=train(np.array(trainMat),np.array(listClasses))
    testEntry=['love','my','dalmation']
    thisDoc=setWords2Vec(myVocabList,testEntry)
    print(testEntry,'classified as',classify(thisDoc,p0V,p1V,pAb))

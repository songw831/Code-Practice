from math import  log
import operator
import matplotlib.pyplot as plt


#创建数据集
def creatdataSet():
   dataSet=[[1,1,'yes'],
            [1,0,'no'],
            [1,1,'yes'],
            [0,1,'no'],
            [0,0,'no']]
   labels=['no surfacing','flippers']
   return dataSet,labels



# 计算香农熵
def calcShannoEnt(dataSet):
    num=len(dataSet)
    labelcounts={}
    for featVec in dataSet:
        currentlable=featVec[-1]
        if currentlable not in labelcounts.keys():
            labelcounts[currentlable]=0
        labelcounts[currentlable]+=1
    shannonEnt=0.0
    for key in labelcounts:
        prob=float(labelcounts[key])/num
        shannonEnt-=prob*log(prob,2)
    return shannonEnt



# 划分数据集
def splitdataSet(dataSet, axis,value):
    retdataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedfeatVec=featVec[:axis]
            reducedfeatVec.extend(featVec[axis+1:])
            retdataSet.append(reducedfeatVec)
    return retdataSet



# 选择最佳划分方式
def chooseBestFeature(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannoEnt(dataSet)
    bestInfoGain=0.0; bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subdataSet=splitdataSet(dataSet,i,value)
            prob=len(subdataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannoEnt(subdataSet)
        infoGain=baseEntropy-newEntropy
        if infoGain>bestInfoGain:
           bestInfoGain=infoGain
           bestFeature=i
    return bestFeature


def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote]=0
        classCount[vote]+=1
    sortedclassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclassCount[0][0]



def creatTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return  majorityCnt(classList)
    bestFeat=chooseBestFeature(dataSet)
    bestFeatLabel=labels[bestFeat]
    mytree={bestFeatLabel:{}}
    del labels[bestFeat]
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLables=labels[:]
        mytree[bestFeatLabel][value]=creatTree(splitdataSet(dataSet,bestFeat,value),subLables)
    return mytree



if __name__ == '__main__':

   myData,labels=creatdataSet()
   Mytree=creatTree(myData,labels)
   print(Mytree)


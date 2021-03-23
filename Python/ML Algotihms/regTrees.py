from numpy import *

def loaddataSet(filename):
    fr=open(filename)
    dataMat=[]
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=[]
        for i in curLine:
          fltLine.append(float(i))
        dataMat.append(fltLine)
    return dataMat


def SplitdataSet(dataSet,feature,value):
    mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:]
    mat1=dataSet[nonzero(dataSet[:,feature]<=value)[0],:]
    return mat0,mat1



def regLeaf(dataSet):
    return mean(dataSet[:,-1])

def regErr(dataSet):
    return var(dataSet[:,-1])*shape(dataSet)[0]

def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0];tolN=ops[1]
    if len(set(dataSet[:-1].T.tolist()[0]))==1:
        return None,leafType(dataSet)
    m,n=shape(dataSet)
    S=errType(dataSet)
    bestS=inf;bestIndex=0;bestValue=0
    for featIndex in range(n-1):
        for splitVal in set(dataSet[:,featIndex].T.tolist()[0]):
            mat0,mat1=SplitdataSet(dataSet,featIndex,splitVal)
            if (shape(mat0)[0]<tolN)or (shape(mat1)[0]<tolN):continue
            newS=errType(mat0)+errType(mat1)
            if newS<bestS:
                bestIndex=featIndex
                bestValue=splitVal
                bestS=newS
    if (S-bestS)<tolS:
        return None,leafType(dataSet)
    mat0,mat1=SplitdataSet(dataSet,bestIndex,bestValue)
    if(shape(mat0)[0]<tolN) or (shape(mat1)[0]<tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue



def creatTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val=chooseBestSplit(dataSet,leafType,errType,ops)
    if feat==None:return val
    retTree={}
    retTree['spInd']=feat
    retTree['spVal']=val
    lSet,rSet=SplitdataSet(dataSet,feat,val)
    retTree['left']=creatTree(lSet,leafType,errType,ops)
    retTree['right']=creatTree(rSet,leafType,errType,ops)
    return retTree

def isTree(obj):
    return (type(obj).__name__=='dict')

def getMean(tree):
    if isTree(tree['right']):tree['right']=getMean(tree['right'])
    if isTree(tree['left']):tree['left']=getMean(tree['left'])
    return (tree['left']+tree['right'])/2.0

def prune(tree,testData):
    if shape(testData)[0]==0: return getMean(tree)
    if(isTree(tree['right']))or(isTree(tree['left'])):
        lSet,rSet=SplitdataSet(testData,tree['spInd'],tree['spVal'])
    if isTree(tree['left']):tree['left']=prune(tree['left'],lSet)
    if isTree(tree['right']):tree['right']=prune(tree['right'],rSet)
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet,rSet=SplitdataSet(testData,tree['spInd'],tree['spVal'])
        errorNoMerge=sum(power(lSet[:-1]-tree['left'],2))+sum(power(rSet[:,-1]-tree['right'],2))
        treeMean=(tree['left']+tree['right'])/2.0
        errorMerge=sum(power(testData[:,-1]-treeMean,2))
        if errorMerge<errorNoMerge:
            print('merging')
            return treeMean
        else: return tree
    else:return tree


if __name__ == '__main__':
    file='D:\Pycharm\代码\数据\ch09\ex00.txt'
    dataMat=mat(loaddataSet(file))
    myTree=creatTree(dataMat,ops=(0,1))
    file1='D:\Pycharm\代码\数据\ch09\ex2test.txt'
    testMat=mat(loaddataSet(file))
    print(prune(myTree,testMat))

import numpy as np
import operator
from matplotlib import pyplot as plt

def creatDataSet():
   fr=open('D:\PyCharm\代码\数据\Ch02\datingTestSet.txt')
   arraylines=fr.readlines()
   linesnum=len(arraylines)
   Mat=np.zeros((linesnum,3))
   index=0
   lables=[]
   lableX1,lableY1,lableX2,lableY2=[],[],[],[]
   for line in arraylines:
       line=line.strip()
       ListLine=line.split('\t')
       Mat[index,:]=ListLine[0:3]
       lables.append(ListLine[-1])
       index+=1
   fr.close()
   return Mat,lables



def autoNorm(dataSet):
    Maxvals=dataSet.max(0)
    Minvals=dataSet.min(0)
    ranges=Maxvals-Minvals
    m=dataSet.shape[0]
    normdataSet=np.zeros(dataSet.shape)
    normdataSet=dataSet-np.tile(Minvals,(m,1))
    normdataSet=normdataSet/np.tile(ranges,(m,1))
    return normdataSet




def classify(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqdiff=diffMat**2
    sqdistance=sqdiff.sum(axis=1)
    distances=sqdistance**0.5
    SortedIndex=distances.argsort()
    ClassCount={}
    for i in range(k):
        votelable=lables[SortedIndex[i]]
        ClassCount[votelable]=ClassCount.get(votelable,0)+1
        sortedClassCount=sorted(ClassCount.items(),key=operator.itemgetter(1),reverse=True)

    return sortedClassCount[0][0]


if __name__ == '__main__':

    dataSet,lables=creatDataSet()
    ratio=0.1
    normMat=autoNorm(dataSet)
    m=normMat.shape[0]
    numTest=int(m*ratio)
    errornum=0.0
    for i in range(numTest):
        Result=classify(normMat[i,:],normMat[numTest:m,:],lables[numTest:m],3)
        print('the classifier comes back: %s, the real answer is : %s' % (Result, lables[i]))
        if(Result!=lables[i]):
            errornum+=1.0

    print('the error ratio is %f' %(errornum/float(numTest)))




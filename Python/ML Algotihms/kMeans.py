from numpy import *

def loaddataSet(filename):
    dataMat=[]
    fr=open(filename)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat


def disEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
    n=shape(dataSet)[1]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids

def kMeans(dataSet,k,distMeas=disEclud,creatCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=creatCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=inf;minIndex=-1
            for j in range(k):
                distJI=distMeas(centroids[j,:],dataSet[i,:])
                if distJI<minDist:minDist=distJI;minIndex=j
            if (clusterAssment[i,0]!=minIndex): clusterChanged=True
            clusterAssment[i:]=minIndex,minDist**2
        for cent in range(k):
            ptsInclust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInclust,axis=0)
    return centroids,clusterAssment

def biKmeans(dataSet,k,distMeas=disEclud):
    m=shape(dataSet)[0]
    clustAssment=mat(zeros((m,2)))
    centroid0=mean(dataSet,axis=0).tolist()[0]
    cenList=[centroid0]
    for j in range(m):
        clustAssment[j,1]=distMeas(mat(centroid0),dataSet[j,:])**2
    while (len(cenList)<k):
        lowestSSE=inf
        for i in range(len(cenList)):
            ptsInCurrCluster=dataSet[nonzero(clustAssment[:,0].A==i)[0],:]
            centoidMat,splitClustAss=kMeans(ptsInCurrCluster,2,distMeas)
            seeSplit=sum(splitClustAss[:,1])
            seeNotSplit=sum(clustAssment[nonzero(clustAssment[:,0],A!=i)[0],1])
            print('seeSplit,and notSplit',seeSplit,seeNotSplit)
            if(seeSplit+seeNotSplit)<lowestSSE:
                bestCentToSplit=i
                bestNewCents=centoidMat
                bestClustAss=splitClustAss.copy()
                lowestSSE=seeNotSplit+seeSplit
        bestClustAss[nonzero(bestClustAss[:,0].A==1)[0],0]=len(cenList)
        bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0]=bestCentToSplit
        print('the bestCentToSplit is: ',bestCentToSplit)
        print('the len of bestClustAss is:', len(bestCentToSplit))
        cenList[bestCentToSplit]=bestNewCents[0,:]
        cenList.append(bestNewCents[1,:])
        clustAssment[nonzero(clustAssment[:,0].A==bestCentToSplit)[0],:]=bestClustAss
    return mat(cenList),clustAssment
if __name__ == '__main__':
    file=r'D:\Pycharm\代码\数据\ch10\testSet2.txt'
    dataMat=mat(loaddataSet(file))
    centList,myNewAssments=biKmeans(dataMat,3)
    print(centList,myNewAssments)
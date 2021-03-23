from numpy import *


def loadData():
    dataMat=matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    classLabels=[1.0,1.0,-1.0,-1.0,1.0]
    return dataMat,classLabels


def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray=ones((shape(dataMatrix)[0],1))
    if threshIneq=='lt':
        retArray[dataMatrix[:,dimen]<=threshVal]=-1.0
    else:
        retArray[dataMatrix[:,dimen]>threshVal]=1.0
    return retArray


def buildStump(dataArr,classLabels,D):
    dataMatrix=mat(dataArr);labelMat=mat(classLabels).T
    m,n=shape(dataMatrix)
    numsteps=10.0;bestStump={};bestClasEst=mat(zeros((m,1)))
    minEorr=inf
    for i in range(n):
        rangeMin=dataMatrix[:,i].min();rangeMax=dataMatrix[:,i].max()
        stepSize=(rangeMax-rangeMin)/numsteps
        for j in range(-1,int(numsteps)+1):
            for inequal in ['lt','gt']:
                threshVal=(rangeMin+float(j)*stepSize)
                predVals=stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr=mat(ones((m,1)))
                errArr[predVals==labelMat]=0
                weightedError = D.T * errArr
                print('split:dim %d,thresh %.2f,thresh inequal:%s,the weighted error is %.3f'%(i,threshVal,inequal,weightedError))
                if weightedError<minEorr:
                    minEorr=weightedError
                    bestClasEst=predVals.copy()
                    bestStump['dim']=i
                    bestStump['thresh']=threshVal
                    bestStump['ineq']=inequal
    return bestStump,minEorr,bestClasEst


def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr=[]
    m=shape(dataArr)[0]
    D=mat(ones((m,1))/m)
    aggClass=mat(zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst=buildStump(dataArr,classLabels,D)
        print('D:',D.T)
        alpha=float(0.5*log((1.0-error)/max(error,1e-16)))
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        print('classEst:',classEst.T)
        expon=multiply(-1*alpha*mat(classLabels).T,classEst)
        D=multiply(D,exp(expon))
        D=D/D.sum()
        aggClass+=alpha*classEst
        print('aggClass:',aggClass.T)
        aggErrors=multiply(sign(aggClass)!=mat(classLabels).T,ones((m,1)))
        errorRate=aggErrors.sum()/m
        print('total error:',errorRate,'\n')
        if errorRate==0:
            break
    return weakClassArr

def adaClassify(dataClass,classifier):
    dataMatrix=mat(dataClass)
    m=shape(dataMatrix)[0]
    aggClassEst=mat(zeros((m,1)))
    for i in range(len(classifier)):
        classEst=stumpClassify(dataMatrix,classifier[i]['dim'],classifier[i]['thresh'],classifier[i]['ineq'])
        aggClassEst+=classifier[i]['alpha']*classEst
        print(aggClassEst)
    return sign(aggClassEst)


if __name__ == '__main__':
   dataMat,classlabels=loadData()
   classifier=adaBoostTrainDS(dataMat,classlabels,30)
   adaClassify([0,0],classifier)

import random
import numpy as np

def loaddataSet(filename):
    dataMat=[];labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    j=i
    while(j==i):
        j=int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj

def smSimple(dataMat,labels,C,toler,maxIter):
    dataMatrix=np.mat(dataMat);labelMat=np.mat(labels).transpose()
    b=0;m,n=np.shape(dataMatrix)
    alphas=np.mat(np.zeros(m,1))
    iter=0
    while(iter<maxIter):
        alphaChanged=0
        for i in range(m):
            fi=float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b
            Ei=fi-float(labelMat[i])
            if((labelMat[i]*Ei<-toler)and(alphas[i]<C) or (labelMat[i]*Ei>toler)and(alphas[i]>0)):
                 j=selectJrand(i,m)
                 fj=float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                 Ej=fj-float(labelMat[j])
                 alphaI=alphas[i].copy()
                 alphaJ=alphas[j].copy()
                 if(labelMat[i]!=labelMat[j]):
                     L=max(0,alphas[j]-alphas[i])
                     H=min(C,C+alphas[j]-alphas[j])
                 else:
                     L=max(0,alphas[j]+alphas[i]-C)
                     H=min(C,alphas[j]+alphas[i])
                 if L==H: print('L==h');continue
                 eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-dataMatrix[i,:]*dataMatrix[i,:]-dataMatrix[j:]*dataMatrix[j:].T
                 if eta>=0:print('eta>=0');continue
                 alphas[j]-=labelMat[j]*(Ei-Ej)/eta
                 alphas[j]=clipAlpha(alphas[j],H,L)
                 if(abs(alphas[j]-alphaJ)<0.01):
                     print('j is not moving enoough');continue
                 alphas[i]+=labelMat[j]*labelMat[i]*(alphaJ-alphas[j])
                 b1=b-Ei-labelMat[i]*(alphas[i]-alphaI)*dataMatrix[i,:]*dataMatrix[i,:].T-labelMat[j]*(alphas[j]-alphaJ)*\
                 dataMatrix[i,:]*dataMatrix[j,:].T
                 b2=b-Ej-labelMat[i]*(alphas[i]-alphaI)*dataMatrix[i,:]*dataMatrix[j,:].T-labelMat[j]*(alphas[j]-alphaJ)*\
                 dataMatrix[j,:]*dataMatrix[j,:].T
                 if(0<alphas[i])and(C>alphas[i]):b=b1
                 elif(0<alphas[j])and(C>alphas[j]):b=b2
                 else:b=(b1+b2)/2.0
                 alphaChanged+=1
                 print('iter:%d i:%d,pairs changed %d'% (iter,i,alphaChanged))
        if(alphaChanged==0):iter+=1
        else:iter=0
        print('iteration number:%d'% iter)
    return b, alphas

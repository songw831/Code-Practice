from numpy import  *
import matplotlib.pyplot as plt


def loaddataSet(filename):
    fr=open(filename)
    dataMat=[];labelMat=[]
    numFeat=len(fr.readline().split('\t'))-1
    for line in fr.readlines():
        lineArr=[]
        curline=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curline[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curline[-1]))
    return  dataMat,labelMat


def standRegress(xArr,yArr):
    xMat=mat(xArr); yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print('This matrix is singular, cannot do inverse')
        return
    w=xTx.I*(xMat.T*yMat)
    return w


def lwlr(testPoint,xArr,yArr,k=0.01):
    xMat=mat(xArr);yMat=mat(yArr).T
    m=shape(xMat)[0]
    weights=mat(eye((m)))
    for j in range(m):
        diffMat=testPoint-xMat[j,:]
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xMat.T*(weights*xMat)
    if linalg.det(xTx)==0.0:
        print('This matrix is singular,cannot do inverse')
        return
    w=xTx.I*(xMat.T*(weights*yMat))
    return testPoint*w


def lwlrTest(TestArr,xArr,yArr,k=0.01):
    m=shape(TestArr)[0]
    yHat=zeros(m)
    for i in range(m):
        yHat[i]=lwlr(TestArr[i],xArr,yArr,k)
    return yHat


if __name__ == '__main__':
    xArr,yArr=loaddataSet('D:\Pycharm\代码\数据\ch08\ex0.txt')
    w=lwlrTest(xArr,xArr,yArr)
    xMat=mat(xArr); yMat=mat(yArr)
    srtInd=xMat[:,1].argsort(0)
    xSort=xMat[srtInd][:,0,:]
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(xSort[:,1],w[srtInd])
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    plt.show()
class treeNode:
    def __init__(self,nameValue,numOccur,parentNode):
        self.name=nameValue
        self.count=numOccur
        self.nodeLink=None
        self.parent=parentNode
        self.children={}

    def inc(self,numOccur):
        self.count+=numOccur


    def disp(self,ind=1):
        print(''*ind,self.name,'',self.count)
        for child in self.children.values():
            child.disp(ind+1)

def createTree(dataSet,minSup=1):
    headerTable={}
    for trans in dataSet:
        for item in trans:
            headerTable[item]=headerTable.get(item,0)+dataSet[trans]
    for k in list(headerTable.keys()):
        if headerTable[k]<minSup:
            del(headerTable[k])
    freqItemset=set(headerTable.keys())
    if len(freqItemset)==0:return  None,None
    for k in headerTable:
        headerTable[k]=[headerTable[k],None]
    retTree=treeNode('Null Set',1,None)
    for tranSet,count in dataSet.items():
        localD={}
        for item in tranSet:
            if item in freqItemset:
                localD[item]=headerTable[item][0]
        if len(localD)>0:
            orderedItems=[v[0] for v in sorted(localD.items(),key=lambda p:p[1],reverse=True)]
            updateTree(orderedItems,retTree,headerTable,count)
    return retTree,headerTable

def updateTree(items,inTree,headerTable,count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]]=treeNode(items[0],count,inTree)
        if headerTable[items[0]][1]==None:
            headerTable[items[0]][1]=inTree.children[items[0]]
        else:
            updateHeader((headerTable[items[0]][1],inTree.children[items[0]]))
    if len(items)>1:
        updateTree(items[1:],inTree.children[items[0]],headerTable,count)

def updateHeader(nodeToTest,targetNode):
    while(nodeToTest.nodeLink!=None):
        nodeToTest=nodeToTest.Link
    nodeToTest.nodeLink=targetNode

def loadSimDat():
    simDat=[['r','z','h','j','p'],['z','y','x','w','v','u','t','s'],['z'],['r','x','n','o','s'],]
    return simDat

def createInitSet(dataSet):
    retDict={}
    for trans in dataSet:
        retDict[frozenset(trans)]=1
    return retDict

simDat=loadSimDat()
InitSet=createInitSet(simDat)
MyFptree,myHeaderTab=createTree(InitSet,3)
MyFptree.disp()
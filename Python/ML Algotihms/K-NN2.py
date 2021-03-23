
from matplotlib import pyplot as plt

fr = open(r'D:/PyCharm/代码/数据/Ch02/datingTestSet.txt')
arraylines = fr.readlines()
linesnum = len(arraylines)
lableX1, lableY1, lableX2, lableY2 = [], [], [], []
for line in arraylines:
    line = line.strip()
    ListLine = line.split('\t')
    if ListLine[-1]=='didntLike':
        lableX1.append(ListLine[0])
        lableY1.append(ListLine[1])
    elif ListLine[-1]=='smallDoses':
        lableX2.append(ListLine[0])
        lableY2.append(ListLine[1])
plt.figure(figsize=(8,5),dpi=80)
axes = plt.subplot(111)
lable1 = axes.scatter(lableX1, lableY1, s=20,c='r')
lable2 = axes.scatter(lableX2, lableY2, s=40,c='g')

plt.xlabel('every year fly distance')
plt.ylabel('play video game time')


plt.legend((lable1, lable2), ('didntlike', 'smallDoses'))
plt.show()




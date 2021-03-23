#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<process.h>
using namespace std;
const int maxsize=20;
typedef struct{
int elem[maxsize+1];  //将elem[0]闲置
int length;
}SqList;
void showList(SqList L)
  {  for(int i=1;i<L.length;i++)
      printf("%d",L.elem[i]);
      printf("%d\n",L.elem[L.length]);
  }
void SelectPass(SqList &L)
{int w;
for(int i=1;i<L.length;++i)
{
    int j=i;
    for(int k=i+1;k<=L.length;k++)
        if(L.elem[k]<L.elem[j])  j=k;
        if(i!=j)
            {w=L.elem[i];
            L.elem[i]=L.elem[j];
            L.elem[j]=w;}
}
}
void InsertSort(SqList &L)
{
    for(int i=2;i<=L.length;i++)
    {
        if(L.elem[i]<L.elem[i-1])
            { L.elem[0]=L.elem[i];
            int j;
            for( j=i-1;L.elem[0]<L.elem[j];--j)
            L.elem[j+1]=L.elem[j];
            L.elem[j+1]=L.elem[0];
            }
    }
}
void BubbleSort(SqList &L)
{
    int w;
    int i=L.length;
    while(i>1)
    {
       int lastExchange=1;
        for(int j=1;j<=i-1;j++){
            if(L.elem[j]>L.elem[j+1]){
                w=L.elem[j];L.elem[j]=L.elem[j+1];L.elem[j+1]=w;
                lastExchange=j;
            }
        }
            i=lastExchange;
    }
}
int Partition(int R[], int low, int high)
{
    R[0]=R[low];
    int pivotkey=R[low];
    while(low<high){
        while(low<high&&R[high]>=pivotkey)
            --high;
        if(low<high)
            R[low++]=R[high];
        while(low<high&&R[low]<=pivotkey)
            ++low;
        if(low<high)
            R[high--]=R[low];}
        R[low]=R[0];
        return low;
    }
void QSort( int R[], int s, int t)
    {
        if(s<t){
            int pivotloc=Partition(R,s,t);
            QSort(R,s,pivotloc-1);
            QSort(R,pivotloc+1,t);
    }
}
void QuickSort(SqList &L)
{
    QSort(L.elem,1,L.length);
}
void Merge(int SR[], int TR[],int i, int m, int n)
{   int j, k;
    for(j=m+1, k=i;i<=m&&j<=n;++k){
        if(SR[i]<=SR[j])TR[k]=SR[i++];
        else TR[k]=SR[j++];
    }
    while (i<=m) TR[k++]=SR[i++];
    while (j<=n) TR[k++]=SR[j++];
}
void Msort(int SR[], int TR1[],int s, int t)
{
    int TR2[t-s+1];
    if(s==t) TR1[s]=SR[s];
    else{
       int m=(s+t)/2;
        Msort(SR,TR2,s,m);
        Msort(SR,TR2,m+1,t);
        Merge(TR2,TR1,s,m,t);
    }
}
void MergeSort(SqList &L)
{
    Msort(L.elem,L.elem,1,L.length);
}
int main ()
{   int N;
    SqList L;
    SqList l1;
    SqList l2;
    SqList l3;
    SqList l4;
    printf("请输入线性表元素个数:\n");
    scanf("%d",&N);
    L.length=N;
    printf("请输入线性表的元素:\n");
    for(int s=1;s<=N;s++)
    scanf("%d",&L.elem[s]);
    printf("你创建的线性表为:\n");
    showList(L);
    l1=L;l2=L;l3=L;l4=L;
    SelectPass(L);
    printf("选择排序之后的线性表为：\n");
    showList(L);
    printf("插入排序之后的线性表为：\n");
    InsertSort(l1);
    showList(l1);
    BubbleSort(l2);
    printf("冒泡排序后之的线性表为：\n");
    showList(l2);
    QuickSort(l3);
    printf("快速排序之后的线性表为：\n");
    showList(l3);
    MergeSort(l4);
    printf("归并排序之后的线性表为：\n");
    showList(l4);
}

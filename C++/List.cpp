
#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<process.h>
using namespace std;
const  int LISTINCREMENT=10;
const  int  LISTSIZE=100;
typedef char ElemType;
typedef  struct{
    char *elem;
    int  length;
    int listsize;
    int incrementsize;
}SqList;
void InitiaList_Sq(SqList &L,int maxsize=LISTSIZE,int incresize=LISTINCREMENT)
{
    L.elem=new char[maxsize];
    L.length=0;
    L.listsize=maxsize;
    L.incrementsize=incresize;
}
void increment(SqList &L,int k)
{char *a;
a=new char[L.listsize+k];
for (int i=0;i<L.length;i++)
    a[i]=L.elem[i];
delete []L.elem;
L.elem=a;
L.listsize+=k;
    delete [] a;
    }
void ClearList(SqList &L)
{
    L.length=0;
}
void showList(SqList L)
  {  for(int i=0;i<(L.length-1);i++)
      printf("%c",L.elem[i]);
      printf("%c\n",L.elem[L.length-1]);
  }
void InsertList(SqList &L, int i, char e)
{

    char *q;
    q=&(L.elem[i-1]);
    for(char *p=&(L.elem[L.length-1]);p>=q;--p)
    *(p+1)=*p;
    *q=e;
    ++L.length;
}
void ErrorMessage(char*s)
{
    cout<<s<<endl;
    exit(1);
}
void DeleteList(SqList &L,int i, char &e)
 {char *p=&(L.elem[i-1]);
 e=*p;
 char *q=L.elem+L.length-1;
 for(++p;p<=q;p++)
    *(p-1)=*p;
 L.length--;}
int LocateList(SqList L, char e)
{
   int i=1;
    char *p=L.elem;
    while (i<=L.length&&*p++!=e)
        ++i;
    if(i<=L.length)return i;
    else return 0;
}
  int main()
 {
    SqList La;
    InitiaList_Sq(La,100,10);
    printf("请输入线性表元素：\n");
    for (int i=1;i<=5;i++)
    {
        scanf("%s",&La.elem[i-1]);
    }
    La.length=5;
    printf("你创建的线性表为：\n");
    showList(La);
    InsertList(La,2,'a');
    printf("插入之后的线性表为：\n");
    showList(La);
    char e;
    DeleteList(La,3,e);
    printf("删除之后的线性表为\n");
    showList(La);
    int k=LocateList(La,'c');
    printf("该数据的位置是%d\n",k);

    return 0;

}

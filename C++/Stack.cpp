#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
const int STACK_INIT_SIZE=100;
const int STACKINCREMENT=10;
typedef struct {
int *elem;
int top;
int stacksize;
int incrementsize;
 } SqStack;
 void InitStack_Sq(SqStack &S, int maxsize, int incresize)
 {
     S.elem= new int[maxsize];
     S.top=-1;
     S.stacksize=maxsize;
     S.incrementsize=incresize;
 }
 bool GetTOP_Sq(SqStack S)
 {
     if(S.top==-1)
        return false;
     else
        return true;
 }
 void incrementStacksize( SqStack &S)
 {
     int *a;
      a=new int[S.stacksize+S.incrementsize];
      for(int i=0;i<S.stacksize;i++)
          a[i]=S.elem[i];
          delete [] S.elem;
          S.elem=a;
          S.stacksize+=S.incrementsize;
 }
 void Push_Sq(SqStack &S, int e)
 {
     if(S.top=S.stacksize-1) incrementStacksize(S);
     S.elem[++S.top]=e;
 }
 bool Pop_Sq(SqStack &S, int &e)
 {
     if(S.top==-1) return false;
     e=S.elem[S.top--];
     return true;
 }
 int Gettop(SqStack &S)
 {
     if(S.top==-1) return false;
     else return S.elem[S.top];
 }
 void ShowStack(SqStack S)
 {
     for (int i=0;i<S.top;++i)
        printf("%d",S.elem[i]);
        printf("%d\n",S.elem[S.top]);
 }
 typedef struct LNode{
int data;
struct LNode *next;
}LNode, *LinkStack;
void InitStack_L(LinkStack &s,int k,int A[])
{
    s=NULL;
    for (int i=k-1;i>=0;i--)
    {
        LNode *p=new LNode;
        p->data=A[i];
        p->next=s;
        s=p;
}
}
void showStack_L(LinkStack s)
{
    LNode *q=s;
    while (q)
    {
        cout<<q->data;
        q=q->next;
    }
}
void Push_L(LinkStack &s, int e)
{
    LNode *p=new LNode;
    p->data=e;
    p->next=s;
    s=p;
}
int main()
{
    SqStack S;
    InitStack_Sq(S,STACK_INIT_SIZE,STACKINCREMENT);
    printf("请输入线性栈元素：\n");
    for (int i=1;i<=5;i++)
    {
        scanf("%d",&S.elem[i-1]);
    }
    S.stacksize=5;
    S.top=4;
    printf("你创建的线性栈为：\n");
    ShowStack(S);
    Push_Sq(S,2);
    printf("插入之后的线性栈为：\n");
    ShowStack(S);
    int e;
    Pop_Sq(S,e);
    printf("删除之后的线性栈为\n");
    ShowStack(S);
    printf("删除的元素为：%d\n",e);
    LinkStack s;
    int k=5; int A[5];
    printf("请输入链栈元素：\n");
    for (int i=0;i<k;++i)
        scanf("%d",&A[i]);
    InitStack_L(s,k,A);
    printf("你创建的链栈为：\n");
    showStack_L(s);
    printf("\n");
    int m=6;
    Push_L(s,m);
    printf("插入元素后的链栈为：\n");
    showStack_L(s);
}

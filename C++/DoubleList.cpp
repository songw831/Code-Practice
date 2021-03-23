#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<process.h>
using namespace std;
typedef struct LNode{
int data;
struct LNode *next，*prior;
}LNode, *LinkList;
void CreatList_L(LinkList &L,int A[],int n)
{
    L=NULL;
    for(int i=n-1;i>=0;i--)
    {
        LNode *s=new LNode;
        s->data=A[i];
        s->next=L;
        L=s;
    }
}
void ListInsert_L(LinkList &L,int k,LNode *p)
// 在第k个节点前插入p节点
{
    LNode *s=L;
    if(k==0)
      {
          p->next=L;
          L=p;
}
 else {
    for (int i=0;i<k-1;i++)
        s=s->next;
        LNode *q=s->next;
        s->next=p;
        p->next=q;

 }
}
 void showList(LinkList L)
 {
     LNode *p;p=L;
     while(p){
        cout<<p->data<<" ";
        p=p->next;
     }
 }
 void DeleteList_L(LinkList &L,int k)
 {
     LNode *p=L;
  if(k==0)
  {L=p->next;}
  else {
    LNode *s=L;
    for( int i=0;i<k-1;i++)
    {
        s=s->next;
    }
    p=s->next;
    s->next=p->next;
 }
 }
 int main()
 {
     LNode *L;
     int n;
     int A[10];
     printf("请输入链表的长度：\n");
     scanf("%d",&n);
     printf("请输入链表的元素：\n");
     for (int i=0;i<n;i++)
     scanf("%d",&A[i]);
     CreatList_L(L,A,n);
     printf("你创建的链表为：\n");
     showList(L);
     LNode *p=new LNode;
     p->data=2;
     ListInsert_L(L,3,p);
     printf("插入元素后的链表为：\n");
     showList(L);
     DeleteList_L(L,2);
     printf("删除元素后的链表为：\n");
     showList(L);
     return 0;
 }

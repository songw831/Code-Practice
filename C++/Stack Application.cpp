#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include"Zhan.h"
#include"z.h"
using namespace std;
void convertion(int N)
{
    SqStack S;
    InitStack_Sq(S, 100, 10);
    while (N)
    {
        Push_Sq(S,N%8);
        N=N/8;
    }
    while(GetTOP_Sq(S))
    {
        int e;
        Pop_Sq(S,e);
        cout<<e;
}
}
bool matching(int exp[])
{   SqStack S;
    InitStack_Sq(S, 100, 10);
    int e;
    int state=1;
    int ch=*exp++;
    while(ch!=0&&state){
    switch (ch) {
    case 1:{Push_Sq(S,ch);break;}
    case 2:{Push_Sq(S,ch);break;}
    case 4:{ if(GetTOP_Sq(S)&&Gettop(S)==1)
               Pop_Sq(S,e);
               else state=0;
               break;}
    case 3:{if(GetTOP_Sq(S)&&Gettop(S)==2)
                   Pop_Sq(S,e);
                   else state=0;
                   break;}
}
 ch=*exp++;
    }
    if(state&&!(GetTOP_Sq(S))) return true;
    else return false;
}
void knapsack(int w[],int T, int n)
{
    SqStack S;
    InitStack_Sq(S, 100, 10);
    int k=0;
    int e;
    do
    {
        while (T>0&&k<n){
            if(T-w[k]>=0){
                Push_Sq(S,k);
                T-=w[k];}
        k++;}
           if(T==0) ShowStack(S);
           Pop_Sq(S,k);T+=w[k];
           k++;   }while (!StackEmpty(S)||k<n);
}
int value(int n,int x, int y)
{
    if(n==0) return(x+1);
    else switch(n){
        case 1:return x;
        case 2: return 0;
        case 3: return 1;
        default :return 2;
    }
}
int Ackerman(int n, int x, int y)
{
    sqStack S;
   InitStack_sq(S,100,10);
   Acker e;
   int u;
   e.nval=n; e.xval=x; e.yval=y; Push_sq(S,e);
   do {
        gettop(S ,e);
        while(e.nval!=0&&e.yval!=0)
            {
                e.yval--;
                Push_sq(S,e);
            }
            Pop_sq(S,e);
            u=value(e.nval,e.xval,e.yval);
            if(!Stackempty(S))
            {
                Pop_sq(S,e);
                e.nval--;
                e.yval=e.xval;
                e.xval=u;
                Push_sq(S,e);
            }
        }while (!Stackempty(S));
        return u;
}
int main()
{
    int N;
    int exp[7];
    printf("请输入你要转变的十进制数:\n");
    scanf("%d",&N);
    printf("转变后的八进制数为：\n");
    convertion(N);
    printf("\n");
    printf("你要验证的括号序列：\n");
    for(int i=0;i<7;++i)
        scanf("%d",&exp[i]);
    if(matching(exp))
        printf("输入的括号序列使用正确\n");
        else
        printf("输入的括号序列使用错误\n");
        int n=6, T=10;
        int w[6]={1,8,4,3,5,2};
        printf("满足条件的解对应的编号为为：\n");
        knapsack(w,T,n);
        printf("函数值为:\n");
        cout<<Ackerman(3,1,1)<<endl;
        return 0;
}

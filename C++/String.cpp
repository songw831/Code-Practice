 #include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
using namespace std;
const int MAXSIZE=1000;
const int MAXMN=100;
typedef struct{
int i,j;
int e;}Triple;
typedef struct{
Triple data[MAXSIZE+1];
int mu,nu,tu;}TSMatrix;
int num[100],rpos[100];
void creatRpos(TSMatrix M)
{ int col;
  for (col=1;col<=M.nu;col++)num[col]=0;
  for(int t=1;t<M.tu;t++)++num[M.data[t].j];
  rpos[1]=1;
  for(col=2;col<=M.nu;col++)
  rpos[col]=rpos[col-1]+num[col-1];
  }
void FastTransposeSMatrix(TSMatrix M, TSMatrix &T)
  {
      T.mu=M.nu;T.nu=M.mu;T.tu=M.tu;
      if(T.tu){
        creatRpos(M);
        int p,q,col;
        for(p=1;p<=M.tu;++p)
        {
            col=M.data[p].j;
            q=rpos[col];
            T.data[q].i=M.data[p].j;T.data[q].j=M.data[p].i;
            T.data[q].e=M.data[p].e;
            ++rpos[col];
        }
      }
  }
void Concat_Sq(char S1[],char S2[],char T[])
{
    int j,k=0;
    while(S1[j]!='0') T[k++]=S1[j++];
    j=0;
    while(S2[j]!='0') T[k++]=S2[j++];
    T[k]='\0';
}
void SubString_Sq(char Sub[],char *&S, int pos,int len)
{
    int slen=strlen(S);
    if(pos<0||pos>slen-1||len<0||len>slen-pos)
        {  exit(1);}
        for(int j=0;j<len;j++)Sub[j]=Sub[pos+j];
    Sub[len]='\0';
}
void StrInsert_HSq(char *&S, int pos, char *T)
{
    int slen=strlen(S);
    int tlen=strlen(T);
    char S1[slen+1];
    if(pos<1||pos>slen+1) {
        printf("输入参数不合法\n");
         exit(1);}
    if(tlen>0){
        int i=0;
        while(S[i]!='\0'){S1[i]=S[i];i++;}
        S=new char [slen+tlen+1];
        int k=0;
        for(i=0;i<pos-1;++i)S[k++]=S1[i];
        int j=0;
        while(T[j]!='\0')S[k++]=T[j++];
        while(S1[i]!='\0')S[k++]=S1[i++];
        S[k]='\0';
    }
}
int Index_BF(char S[],char T[],int pos )
{
    int i=pos;int j=0;
    while(S[i+j]!='\0'&&T[j]!='\0')
    {if(S[i+j]==T[j])j++;
    else{i++;j=0;}}
    if(T[j]=='\0')return i;
    else return -1;
}
void get_next(char *T, int *next)
{
    int i=0; int j=-1; next[0]=-1;
    while(T[i]!='\0')
    {if(j==-1||T[i]==T[j])
    {
        i++;j++;next[i]=j;}
        else j=next[j];
    }
    }
int Index_KMP(char *S, char *T, int pos)
{
    int next[50];
    int i=pos; int j=0;
    get_next(T,next);
    while(i<strlen(S))
    {
        if(j==-1||S[i]==T[j])
        {i++;j++;}
        else j=next[j];
        if(j==strlen(T))
            return i-strlen(T);
    }
    return -1;
    }
int Index_FL(char *S, char*T , int pos)
{
    int slen=strlen(S);
    int tlen=strlen(T);
    int i=pos;
    char PatStartChar=T[0];
    char PatEndChar=T[tlen-1];
    while(i<slen-tlen+1)
    {
        if(S[i]!=PatStartChar)i++;
        else if(S[i+tlen-1]!=PatEndChar)i++;
        else {int k=1,j=1;
        while (j<tlen&&S[i+k]==T[j])
        {
            k++;j++;
        }
        if(j==tlen) return i;
        else i++;
    }
    }
    return -1;
}

int main()
{
    char *S0="abcdef";
    char *S2="abcdef";
    char T[]="def";
    int next[20];
    int pos=0;
    int k=2;
    StrInsert_HSq(S0,k,T);
    printf("插入T后的S0为：%s\n",S0);
    int m1=Index_BF(S2,T,pos);
    printf("BF算法匹配后得到的值为：%d\n",m1);
    get_next(T, next);
    int m2=Index_KMP(S2,T, pos);
    printf("KMP算法匹配后得到的值为：%d\n",m2);
    int m3=Index_FL(S2,T,pos);
    printf("FL算法匹配后得到的值为：%d\n",m3);
    TSMatrix M;
    TSMatrix T1;
    for (int k=1;k<=5;++k)
    {
        M.data[k].i=k;
        M.data[k].j=k+1;
        M.data[k].e=k+2;
    }
    M.mu=6;M.nu=6;M.tu=5;
    printf("M的三元组为：\n");
    for(int k=1;k<=5;k++)
    printf("(%d,%d,%d) ",M.data[k].i,M.data[k].j,M.data[k].e);
    printf("\n");
    FastTransposeSMatrix(M,T1);
    printf("T1的三元组为：\n");
    for(int k=1;k<=5;k++)
    printf("(%d,%d,%d) ",T1.data[k].i,T1.data[k].j,T1.data[k].e);
}

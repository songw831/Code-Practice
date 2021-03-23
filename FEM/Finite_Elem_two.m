function U=Finite_Elem_two(f,N)
%用Ritz法解二维均匀矩形网椭圆型方程
%默认矩形区域为（0，1）*（0，1）
%N为每个剖分单元格数
%f为方程右端函数
if nargin<2
    error('f,u must be defined'); %必须给出右端函数和边值条件
else if nargin==2;
    N=5;       %默认单元格数为5
    end
end
    Ne=N*N;   %总单元格数
    Np=(N+1)*(N+1); %总结点个数
    h=1/N;         %计算步长
    A=zeros(Np); %总刚矩阵
    b=zeros(Np,1);   %右端向量
    P=zeros(2,Np); %表示节点坐标
    T=zeros(4,Ne);%表示每个单元节点序号矩阵
    for i=N+1:N+1:Np
        P(1,i-N:i)=h*[0:N];
        r=h*(i/(N+1)-1);
        P(2,i-N:i)=ones(1,N+1)*r;
    end
     for i=1:Ne
      k=fix(i/(N+1));  %相除取整 
      T(1:4,i)=[i+k i+k+1 i+k+N+2 i+k+N+1];
     end
    for i=1:Ne    %计算每个单位刚矩阵，进而组合成A ；计算每个单位刚矩阵对应右端向量，进而合成b
        K=zeros(Np);
        r=zeros(Np,1);
        x1=P(1,T(1,i));
        y1=P(2,T(1,i));
        f1=@(x,y)(1-abs((x-x1)/h))*(1-abs((y-y1)*h));
        x2=P(1,T(2,i));
        y2=P(2,T(2,i));
        f2=@(x,y)(1-abs((x-x2)/h))*(1-abs((y-y2)*h));
        x3=P(1,T(3,i));
        y3=P(2,T(3,i));
        f3=@(x,y)(1-abs((x-x3)/h))*(1-abs((y-y3)*h));
        x4=P(1,T(4,i));
        y4=P(1,T(4,i));
        f4=@(x,y)(1-abs((x-x4)/h))*(1-abs((y-y4)*h));
        fu={f1,f2,f3,f4};
     for k=1:4
       for j=1:4
           syms x y;
           Sdf1x=fu{k}(x,y);
           Pdf1x=diff(Sdf1x,x);
           df1x=eval(['@(x,y)',vectorize(Pdf1x)]);
           Sdf1y=fu{k}(x,y);
           Pdf1y=diff(Sdf1y,y);
           df1y=eval(['@(x,y)',vectorize(Pdf1y)]);
           Sdf2x=fu{j}(x,y);
           Pdf2x=diff(Sdf2x,x);
           df2x=eval(['@(x,y)',vectorize(Pdf2x)]);
           Sdf2y=fu{j}(x,y);
           Pdf2y=diff(Sdf2y,y);
           df2y=eval(['@(x,y)',vectorize(Pdf2y)]);
           F1=@(x,y)df1x(x,y).*df2x(x,y)+df1y(x,y).*df2y(x,y);
      K(T(j,i),T(k,i))=dblquad(F1,x1,x2,y1,y4);
      K(T(k,i),T(j,i))=K(T(j,i),T(k,i));
       end
     end
     A=A+K;
      for m=1:4
          syms x y;
          Pdf3x=diff(fu{m}(x,y),x);
          Pdf3y=diff(fu{m}(x,y),y);
          Pdf4x=diff(f(x,y),x);
          Pdf4y=diff(f(x,y),y);
          df3x=eval(['@(x,y)',vectorize(Pdf3x)]);
          df3y=eval(['@(x,y)',vectorize(Pdf3y)]);
          df4x=eval(['@(x,y)',vectorize(Pdf4x)]);
          df4y=eval(['@(x,y)',vectorize(Pdf4y)]);
          F2=@(x,y)df3x(x,y).*df4x(x,y)+df3y(x,y).*df4y(x,y);
          r(T(m,i))=dblquad(F2,x1,x2,y1,y4);
      end
          b=b+r;
          i
    end
    A
    b
    U=A\b
end
       
   
        
        
        
        
        
        
        
function U=Finite_Elem_two(f,N)
%��Ritz�����ά���Ⱦ�������Բ�ͷ���
%Ĭ�Ͼ�������Ϊ��0��1��*��0��1��
%NΪÿ���ʷֵ�Ԫ����
%fΪ�����Ҷ˺���
if nargin<2
    error('f,u must be defined'); %��������Ҷ˺����ͱ�ֵ����
else if nargin==2;
    N=5;       %Ĭ�ϵ�Ԫ����Ϊ5
    end
end
    Ne=N*N;   %�ܵ�Ԫ����
    Np=(N+1)*(N+1); %�ܽ�����
    h=1/N;         %���㲽��
    A=zeros(Np); %�ܸվ���
    b=zeros(Np,1);   %�Ҷ�����
    P=zeros(2,Np); %��ʾ�ڵ�����
    T=zeros(4,Ne);%��ʾÿ����Ԫ�ڵ���ž���
    for i=N+1:N+1:Np
        P(1,i-N:i)=h*[0:N];
        r=h*(i/(N+1)-1);
        P(2,i-N:i)=ones(1,N+1)*r;
    end
     for i=1:Ne
      k=fix(i/(N+1));  %���ȡ�� 
      T(1:4,i)=[i+k i+k+1 i+k+N+2 i+k+N+1];
     end
    for i=1:Ne    %����ÿ����λ�վ��󣬽�����ϳ�A ������ÿ����λ�վ����Ӧ�Ҷ������������ϳ�b
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
       
   
        
        
        
        
        
        
        
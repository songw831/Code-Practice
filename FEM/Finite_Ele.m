function u=Finite_Ele(fun,p,q,a,b,N)
% 从Ritz法出发计算u
% fun 为等式右端函数
% p，q为左端函数
% a,b为区间上下限
% N为节点个数
if nargin<5
    error('fun,p,q,a,b must be defined');  %输入参数少于5个提示出错
elseif nargin==5
    N=10;                                  %默认N的值
end
h=(b-a)/N;                                 %计算步长
x=a+h*[0:N]                               %计算节点
K=zeros(N);
for i=1:(N-1)  %计算总刚矩阵上次对角线元素
    f1=@(t)((-p(x(i+1)+h*t)./h)+h*q(x(i+1)+h*t)*t*(1-t));
    K(i,i+1)=int_lineGussian(f1,0,1,3);
end
for i=2:N                                       %计算总刚矩阵下次对角线元素
    f2=@(t)((-p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*(1-t));
    K(i,i-1)=int_lineGussian(f2,0,1,3);
end
for i=1:N-1                                     %计算总刚矩阵对角线元素
    f3=@(t)((p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*t);
    f4=@(t)((p(x(i+1)+h*t)./h)+h*q(x(i+1)+h*t)*(1-t)*(1-t));
    f5=@(t)((p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*t);
    K(i,i)=int_lineGussian(f3,0,1,3)+int_lineGussian(f4,0,1,3);
end
    K(N,N)=int_lineGussian(f5,0,1,3);
K
b=zeros(N,1);
for i=1:N-1                                        %求右端向量b
    f6=@(t)(fun(x(i)+h*t)*t);
    f7=@(t)(fun(x(i+1)+h*t)*(1-t));
    f8=@(t)(fun(x(N)+h*t)*t);
    b(i)=h*int_lineGussian(f6,0,1,3)+h*int_lineGussian(f7,0,1,3);
    b(N)=h*int_lineGussian(f8,0,1,3);
    
end
b
U=K\b;                                             %求u
u=[0;U];                                         
plot(x,u,'o',x(i),u(i)) 
end

    
    
    
    


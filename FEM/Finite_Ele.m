function u=Finite_Ele(fun,p,q,a,b,N)
% ��Ritz����������u
% fun Ϊ��ʽ�Ҷ˺���
% p��qΪ��˺���
% a,bΪ����������
% NΪ�ڵ����
if nargin<5
    error('fun,p,q,a,b must be defined');  %�����������5����ʾ����
elseif nargin==5
    N=10;                                  %Ĭ��N��ֵ
end
h=(b-a)/N;                                 %���㲽��
x=a+h*[0:N]                               %����ڵ�
K=zeros(N);
for i=1:(N-1)  %�����ܸվ����ϴζԽ���Ԫ��
    f1=@(t)((-p(x(i+1)+h*t)./h)+h*q(x(i+1)+h*t)*t*(1-t));
    K(i,i+1)=int_lineGussian(f1,0,1,3);
end
for i=2:N                                       %�����ܸվ����´ζԽ���Ԫ��
    f2=@(t)((-p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*(1-t));
    K(i,i-1)=int_lineGussian(f2,0,1,3);
end
for i=1:N-1                                     %�����ܸվ���Խ���Ԫ��
    f3=@(t)((p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*t);
    f4=@(t)((p(x(i+1)+h*t)./h)+h*q(x(i+1)+h*t)*(1-t)*(1-t));
    f5=@(t)((p(x(i)+h*t)./h)+h*q(x(i)+h*t)*t*t);
    K(i,i)=int_lineGussian(f3,0,1,3)+int_lineGussian(f4,0,1,3);
end
    K(N,N)=int_lineGussian(f5,0,1,3);
K
b=zeros(N,1);
for i=1:N-1                                        %���Ҷ�����b
    f6=@(t)(fun(x(i)+h*t)*t);
    f7=@(t)(fun(x(i+1)+h*t)*(1-t));
    f8=@(t)(fun(x(N)+h*t)*t);
    b(i)=h*int_lineGussian(f6,0,1,3)+h*int_lineGussian(f7,0,1,3);
    b(N)=h*int_lineGussian(f8,0,1,3);
    
end
b
U=K\b;                                             %��u
u=[0;U];                                         
plot(x,u,'o',x(i),u(i)) 
end

    
    
    
    


function [ I ] = int_lineGussian(  f, a,  b,  k)
% 高斯求积公式
%a,b为积分上下限，k为求积节点
    
    if k==1
        
        x0_gaussian = 0;
        weight_gaussian = 2;
         x_gaussian = ((1-x0_gaussian)/2 ) * a + ((x0_gaussian+1)/2 )* b;
         fun_values = f(x_gaussian);
          I =  ((b-a)/2) * (fun_values * weight_gaussian');
    elseif k==2

        x0_gaussian=[-sqrt(1/3),   sqrt(1/3)];
        weight_gaussian=[1, 1];
        x_gaussian = ((1-x0_gaussian)/2 ) * a + ((x0_gaussian+1)/2 )* b;
        fun_values =[f(x_gaussian(1)), f(x_gaussian(2))];
        I =  ((b-a)/2) * (fun_values * weight_gaussian');
        
    elseif k==3

        x0_gaussian=[-sqrt(3/5),  0,    sqrt(3/5)];
        weight_gaussian=[ 5/9, 8/9, 5/9];
        x_gaussian = ((1-x0_gaussian)/2 ) * a + ((x0_gaussian+1)/2 )* b;
        fun_values =[f(x_gaussian(1)), f(x_gaussian(2)),f(x_gaussian(3))];
        I =  ((b-a)/2) * (fun_values * weight_gaussian');
    end
    
    
    
    

   


end


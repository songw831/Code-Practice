aa=1; bb=2; fun_name = @(x)sin(x);
k_points_gaussian = 1;

I_f = cos(aa)-cos(bb);

I_f_gaussian_h0 = 0;

n0=4; 
h0=(bb-aa)/n0;
for ii=1:n0

    I_f_gaussian_h0 = I_f_gaussian_h0 + int_lineGussian( aa+(ii-1)*h0,  aa+ii*h0,  k_points_gaussian,  fun_name );
    
end
error0 = abs(I_f_gaussian_h0-I_f);




n1 = 2*n0;
h1 = h0/2;
I_f_gaussian_h1 =0;
for ii=1:n1

    I_f_gaussian_h1 = I_f_gaussian_h1 + int_lineGussian( aa+(ii-1)*h1,  aa+ii*h1,  k_points_gaussian,  fun_name );
    
end
error1 = abs(I_f_gaussian_h1-I_f);

order_gaussian = log(error0/error1) / log(2);
%func = func;
min_val=0; max_val=10; epsilon = 1e-5;
[yp,p,iteration] = golden_search(@func,min_val,max_val,epsilon);
disp("max x value is :")
disp(p)
disp("function output :")
disp(yp)
disp("iteration count :")
disp(iteration)
%%
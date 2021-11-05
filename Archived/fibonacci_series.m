% Fibonacci Series
clc
clear
write = sprintf('Write how many numbers you want and press enter? ex. 10 ');
n = input(write);
if isempty(n)
	sprintf('You did not give any input so printing 10 fibonacci values');
	n=10;
end

values = [0 1];
i = 3;
if n ==1
    values = values(1);
    values
elseif n==2
    values
else
    while i<=n
        [values,i]=fibonacci(values,i);
    end
    values
end

function [values,i] = fibonacci(values,i)
    next = values(i-1)+values(i-2);
    values = [values next];
    i=i+1;
end

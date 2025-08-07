clear all; close all; clc;

upto = input("No. of terms: ");

a = 0;
b = 1;

fprintf("%d ", a);
fprintf("%d ", b);

for i = 1:upto
    c = a + b;
    fprintf("%d ", c);
    a = b;
    b = c;
end

printf("\n");

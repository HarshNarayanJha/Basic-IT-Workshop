clc;
clear all;
close all;

a = 3.2;
b = 4.6;

theta = 60 * pi/180;

c = b * sin(theta);

printf("Third Side: %.2f\n", c);

s = (a+b+c)/2;

area = sqrt(s*(s-a)*(s-b)*(s-c));

printf("Third Side: %.2f\n", area);

clc;
clear all;
close all;

function [y] = func(X)
  y = 1 - X^2 / factorial(2) + X^4/factorial(4) - X^6/factorial(6) + X^8/factorial(8);
end

S = func(1.5);
disp(S);

clc; clear; close all;

X = linspace(-10, 10);
Y = sin(X);

plot(X, Y, 'r-', 'LineWidth', 2);

xlim([-10 10]);
ylim([-2 2]);

grid on;

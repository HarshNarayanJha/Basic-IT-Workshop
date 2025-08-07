clear all; close all; clc;

X = linspace(-1, 1);
Y = 5 * X .^ 3 + 3 * X .^ 2 + 2;

plot(X, Y, 'r-', 'LineWidth', 2);

grid on;

xTangent = 0.5;

slope = 15 * xTangent ^ 2 + 6 * xTangent;

yTangent = 5 * xTangent .^ 3 + 3 * xTangent .^ 2 + 2;

hold on;

plot(xTangent, yTangent, 'r*', 'MarkerSize', 5);

yTangentLine = slope * (X - xTangent) + yTangent;

plot(X, yTangentLine, 'b-');

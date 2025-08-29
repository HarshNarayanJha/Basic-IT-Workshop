numbers = randi(100, 1, 10);
count = sum(mod(numbers,2) == 0);
disp(['Count of even numbers: ', num2str(count)]);


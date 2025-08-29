data = [0, 1, 2, 3, 4];
fid = fopen('check.txt', 'w');
fwrite(fid, data, 'double');
fclose(fid);


function trk= readTraks(fileName)

fid = fopen(fileName, 'r');

i = 0;
len = fscanf(fid,'%d');
%printf('%d', len);
%for j = 1:3
while (len) > 0    
    i = i + 1;
    A = fscanf(fid,'(%d,%d,%d)');
    trk(i).x = A(1:3:end);
    trk(i).y = A(2:3:end);
    trk(i).t = A(3:3:end);
    file_name = [sprintf('%d',i) '.txt'];
    printf('%s', file_name);
    trk_fid = fopen(file_name,'w');
    for k = 1:len
      fprintf(trk_fid, '%d\t%d\t%d\n', trk(i).x(k), trk(i).y(k), trk(i).t(k)); 
      %printf('%d\t%d\t%d\n', trk(i).x(k), trk(i).y(k), trk(i).t(k)); 
    end
    fclose(trk_fid);
 
    len = fscanf(fid,'%d');
end
fclose(fid);
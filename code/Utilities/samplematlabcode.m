function [ output_args ] = mattotext( matfileName )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
load(matfileName);
s = size(labled_tra);
noOfTrack = s(2); 
num = sprintf('number of tracks = %d .\n',noOfTrack);
disp(num);
for i = 1:noOfTrack
    x = labled_tra(1,i).x;
    x1 = round(x);
    y = labled_tra(1,i).y;
    y1 = round(y);
    t = labled_tra(1,i).t;
    n = size(labled_tra(1,i).x);
    noPts = n(2);
    nump = sprintf('number of points = %d in track %d.',noPts);
    disp(nump);
    file_name = [sprintf('%d',i) '.txt'];
    fid = fopen(file_name,'w');
    for k = 1:noPts
        fprintf(fid, '%d %d %d\n',x1(k),y1(k),t(k));   
    end
    fclose(fid);
end
end


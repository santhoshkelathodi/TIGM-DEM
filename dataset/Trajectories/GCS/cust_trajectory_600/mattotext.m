function [ output_args ] = mattotext( matfileName )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
load(matfileName);
s = size(trks);
noOfTrack = s(2); 
num = sprintf('number of tracks = %d .\n',noOfTrack);
disp(num);
fileIdx = 0;
for i = 1:noOfTrack
    pArr = trks(1,i);
    x = pArr.x;
    x1 = round(x);
    y = pArr.y;
    y1 = round(y);
    t = pArr.t;
    n = size(pArr.x);
    noPts = n(1);
    if (noPts < 600)
        continue;
    end;
    nump = sprintf('number of points = %d in track %d.',noPts);
    disp(nump);
    file_name = [sprintf('%d',fileIdx) '.txt'];
    fid = fopen(file_name,'w');
    for k = 1:noPts
        fprintf(fid, '%d %d\n',x1(k),y1(k));   
    end
    fileIdx = fileIdx + 1;
    fclose(fid);
end
trksStr = sprintf('number of Tracks = %d with more than 200 points',fileIdx);
disp(trksStr);
end


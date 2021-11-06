import csv
from moviepy.video.io.VideoFileClip import VideoFileClip

#these are parameters
dir='D:\\dataset\\figureSkating+\\2019 LS ISU world champion japan\\'
matchinfo='2019_WC_LS_'
videoname='Ladies Short Program Skating  2019 ISU World Figure Skating Championships Saitama JPN  #WorldFigure.mp4'

def getime(str):
    strlist=str.split(".")
    base=0
    for time in strlist:
        base=base*60
        base=base+int(time)
    return base

source=dir+videoname
with open(dir+'time.csv', "r") as f:
    reader = csv.reader(f)
    # headers = next(reader)
    # print(headers)
    for row in reader:
        print(row)
        name=row[0] #only the athlete name is needed
        start=row[1]
        end=row[2]
        startime=getime(start)
        endtime=getime(end) 
        target = dir+matchinfo+name+'.mp4'
        clip = VideoFileClip(source)
        print(source,target,startime,endtime)
        # continue
        video = VideoFileClip(source)  
        video = video.subclip(startime,endtime)  
        video.to_videofile(target, fps=25, remove_temp=True)

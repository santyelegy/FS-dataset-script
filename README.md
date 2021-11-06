# Figure Skating Dataset Related Script

dependencies: pandas,moviepy

## How to use
- download the original video

- write the `time.csv` file in the following format

    each row: player name,start time,end time

    example of the start time and end time:

    1.3 means 1 min 3 sec

    1.1.57 means 1h 1 min 57 sec

    the order of players shold be sequential, or the score can not match video name 

- run the `csvcut.py` to cut the video
  
    you shold check and change the parameters in the file
    ```python
    dir='D:\\dataset\\figureSkating+\\2019 LS ISU world champion japan\\'
    matchinfo='2019_WC_LS_'
    videoname='Ladies Short Program Skating  2019 ISU World Figure Skating Championships Saitama JPN  #WorldFigure.mp4'
    ```
- run the `makescore.py` to get the score from web
   you shold check and change the parameters in the file
    ```python
    #change this
    url = 'http://results.isu.org/results/season1819/wc2019/data0203.htm'
    prefix='2019_WC_LS_'
    factor=1 # need to check this
    ```
- if you forgot to change the prefix parameter, you can use `rename.py` to change the videos name

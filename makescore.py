import pandas as pd

#change this
url = 'http://results.isu.org/results/season1819/wc2019/data0203.htm'
prefix='2019_WC_LS_'
factor=1 # need to check this

def removePre(name):
    return int(name.lstrip('#'))
    
def makeVideoName(name):
    return prefix+name+'.mp4'


dfs = pd.read_html(url,header=0,index_col=0)
table=dfs[0]
table['StN.']=table['StN.'].apply(removePre)
table.sort_values(by='StN.',inplace=True)
table.reset_index(drop=True,inplace=True)
table.insert(table.shape[1],'factor',factor) 

#match
videonames=pd.read_csv('./time.csv',sep=',',header=None)
videonames=videonames[0].apply(makeVideoName)
#print(videonames)
#print(table)
table['videoName']=videonames
#print(table)
table=table.loc[:, ['videoName','TES','PCS','SS','TR','PE','CO','IN','factor']]
table.to_csv('./score.txt',sep=' ',header=False,index=False)
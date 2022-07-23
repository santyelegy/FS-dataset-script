import pandas as pd
from urldict import listdict
import os
#change this
#http://www.isuresults.com/results/season1920/gpfra2019/
for dict in listdict:
    url = dict["url"]
    prefix=dict["prefix"]
    factor=dict["factor"]
    count=-1
    def removePre(name):
        return int(name.lstrip('#'))
        
    def makeVideoName(name):
        global count
        count=count+1
        return prefix+str(count)+'.mp4'

    dfs = pd.read_html(url,header=0,index_col=0)
    try:
        table=dfs[0]
        table['StN.']=table['StN.'].apply(removePre)
    except Exception:
        try:
            table=dfs[1]
            table['StN.']=table['StN.'].apply(removePre)
        except Exception:
            try:
                table=dfs[2]
                table['StN.']=table['StN.'].apply(removePre)
            except Exception:
                pass
    table.sort_values(by='StN.',inplace=True)
    table.reset_index(drop=True,inplace=True)
    table.insert(table.shape[1],'factor',factor) # please use manpower to check this factor
    heads=table.columns.tolist()
    table[heads[0]]=table[heads[0]].apply(makeVideoName)
    try:
        table=table.loc[:, [heads[0],'TES+','PCS+','SS','TR','PE','CO','IN','factor']]
    except Exception:
        table=table.loc[:, [heads[0],'TES','PCS','SS','TR','PE','CO','IN','factor']]
    print(table)
    os.makedirs('./'+prefix+'/',exist_ok=True)
    table.to_csv('./'+prefix+'/score.csv',sep=',',header=False,index=False)

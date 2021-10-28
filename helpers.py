

import pandas as pd
import sqlite3


DB = 'test7.db'






def upload_prep(nums,date_vec):
    

    
    dic = {
    'date' : date_vec,
    'tips' : nums,
    }
    
    sql_upload = pd.DataFrame(dic)
    
    return sql_upload


def upload(df):
    
    # the daily table upload
    conn = sqlite3.connect(DB)
    df.to_sql('daily',con = conn, if_exists='append', index=False)
    
    # the high level upload
    date = df.iloc[0]['date']
    date_name = df.iloc[0]['date'].replace('/','')
    mean = df.groupby(['date']).mean().iloc[0]['tips']
    total = df.groupby(['date']).sum().iloc[0]['tips']
    n = df.groupby(['date']).count().iloc[0]['tips']
    
    df2 = pd.DataFrame({
        "date" : [date],
        "mean" : [mean],
        "total_tips" : [total],
        "drives" : [n]
    })
    
    df2.to_sql('rollup',con = conn, if_exists='append', index=False)

    # archive data
    archive1 = 'archive/' + date_name + '_daily_' '.csv'
    archive2 = 'archive/' + date_name + '_rollup_' '.csv'
    df.to_csv(archive1,index=False)
    df2.to_csv(archive2,index=False)
    
    print(df2)

    return print('successful upload')


    
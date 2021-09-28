

import pandas as pd
import sqlite3


DB = 'test5'






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
    archive1 = 'archive/' + date + '_daily_' '.csv'
    archive2 = 'archive/' + date + '_rollup_' '.csv'
    df.to_csv(archive1,index=False)
    df2.to_csv(archive2,index=False)
    
    print(df2)

    return print('successful upload')
    
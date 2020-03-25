import requests
import json
import pandas as pd
import datetime
today = datetime.date.today()
start_date = datetime.date(2020, 1, 22)
end_date   = datetime.date(today.year,today.month,today.day)

dates2020 = [ start_date + datetime.timedelta(n) for n in range(int ((end_date - start_date).days))]
date=[]
for i in dates2020:
    a=str(i.month)+"-"+str(i.day)+"-"+str(i.year)
    date.append(a)

def Extract_TimeSeries():
    data=[]
    for i in date:
        response_country = requests.get('https://covid19.mathdro.id/api/daily/'+i+'')
        data_dic = response_country.json()
        df = pd.DataFrame.from_dict(data_dic)
        df["confirmed"] = pd.to_numeric(df['confirmed'])
        df["death"] = pd.to_numeric(df['deaths'])
        df["recovered"] = pd.to_numeric(df['recovered'])
        df2 = df.groupby(['countryRegion']).agg('sum')
        dic=df2.to_dict()
        dic['date']=df.lastUpdate[0]
        data.append(dic)
    return data


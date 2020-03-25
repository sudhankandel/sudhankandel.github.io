import requests
import pandas as pd
from bs4 import BeautifulSoup
website_url = requests.get('https://www.worldometers.info/coronavirus')
soup = BeautifulSoup(website_url.text,'html.parser')

def Yesterday():
    table = soup.find('table',{'id':"main_table_countries_yesterday"})
    list_of_rows = []
    for tr in table.find_all('tr'):
        list_of_cells = []
        for td in tr.find_all(['td', 'th']):
            text = td.text
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    df = pd.DataFrame(list_of_rows)
    data=df
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])
    data=data.to_dict()
    return data

def Today():
    table = soup.find('table',{'id':"main_table_countries_today"})
    list_of_rows = []
    for tr in table.find_all('tr'):
        list_of_cells = []
        for td in tr.find_all(['td', 'th']):
            text = td.text
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    df = pd.DataFrame(list_of_rows)
    data=df
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])
    data=data.to_dict()
    return data

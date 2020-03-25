import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def Get_row():
    url=requests.get('https://heoc.mohp.gov.np')
    soup=BeautifulSoup(url.text,'html.parser')
    rows = soup.findAll('div',{'class':'nepal-update updates'})
    for row in rows:
        Value = row.findAll('span',{'class':'meta-value'})
        required_Value = [p_item.text.strip() for p_item in Value]

        key=row.findAll('span',{'class':'meta-key'})
        required_key = [p_item.text.strip() for p_item in key]
    data=dict(zip(required_key,required_Value))
    data['positive'] = data.pop('Positive (1 Recovered | 1 in Isolation)')
    return data
print(Get_row())

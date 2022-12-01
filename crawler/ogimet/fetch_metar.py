# Created by qdljerry 2022/11
# [Warning] This code is NOT completed as a library

from bs4 import BeautifulSoup
import requests
import datetime
from time import sleep

class MetarData:
    def __init__(self, station, date, time, metar):
        self.station = station
        self.date = date
        self.time = time
        self.metar = metar

class FetchMetar:
    def __init__(self, startDate, endDate, station, type='SA&FT', interval=5):
        self.startDate = startDate
        self.endDate = endDate
        self.station = station
        self.type = type
        self.interval = interval
        self.url = 'http://www.ogimet.com/display_metars2.php?lang=en&lugar=%s&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=%d&mes=%02d&day=%02d&hora=00&anof=%d&mesf=%02d&dayf=%02d&horaf=23&minf=59&send=send'

    def fetch(self, date):
        url = self.url % (self.station, date.year, date.month, date.day, date.year, date.month, date.day)
        while True:
            try:
                r = requests.get(url)
                print(r.status_code, len(r.content))
                if r.status_code == 200 and len(r.content) > 8000:
                    # Check if the page is valid
                    break
                sleep(1)
            except:
                sleep(1)
        soup = BeautifulSoup(r.content, 'html.parser')
        metar_data = soup.find_all('tr')
        return metar_data

def fetch_metar_data(date, station):
    url = 'http://www.ogimet.com/display_metars2.php?lang=en&lugar=%s&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=%d&mes=%02d&day=%02d&hora=00&anof=%d&mesf=%02d&dayf=%02d&horaf=23&minf=59&send=send'%(station, date.year, date.month, date.day, date.year, date.month, date.day)
    while True:
        try:
            r = requests.get(url)
            print(r.status_code, len(r.content))
            if r.status_code == 200 and len(r.content) > 8000:
                break
            sleep(1)
        except:
            sleep(1)
    soup = BeautifulSoup(r.content, 'html.parser')
    metar_data = soup.find_all('tr')
    return metar_data

with open('metar_data.csv', 'o') as f:
    f.write('airport,type,date,time,data\n')
start = datetime.datetime(2022, 10, 23)
end = datetime.datetime(2022, 11, 29)
airport = 'ZBAA'

d = start
while d <= end:
    print('Fetching "%s">'%airport,d)
    metars = fetch_metar_data(d, airport)
    for i in metars:
        con = i.find_all('td')
        type = con[0].text
        if(type == 'SA' or type == 'FT'):
            metar_datetime = con[1].text
            (metar_date, metar_time) = metar_datetime[:-2].split()
            metar_date = '/'.join(reversed(metar_date.split('/')))
            metar = con[2].text.replace('\n        ', '')
            with open('metar_data.csv', 'a') as f:
                f.write('%s,%s,%s,%s,%s\n'%(airport,type, metar_date, metar_time, metar))
    d+=datetime.timedelta(days=1)
    sleep(3)

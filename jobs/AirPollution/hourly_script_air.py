import requests
import json
import csv
import os
import schedule
import time
import pytz
import datetime
import xml.etree.ElementTree as ET

def air_parser(URL, URL2, city_name):

	result = requests.get(URL)
	result2 = requests.get(URL2)

	root = ET.fromstring(result.text)

	temp = []

	for item in root[0]:

		if(item.tag == "item"):
			# from URL
			time = item.find("title").text
			time = get_date_name_file()
			PM25 = item.find("Conc").text
			if(PM25 == "-999.0"):
				PM25 = ""
			AQI = item.find("AQI").text
			if(AQI == "-999"):
				AQI = ""
			## end of URL
			# from URL2
			xml_data = result2.text.split('\n')[1:]
			data1 = xml_data[10]
			data2 = xml_data[12]
			weather = data1.split(': ')[1].split(', ')[0]
			windSpeed = data2.split('Wind Speed: ')[1].split('mph')[0] #unit mph
			windDirection = data2.split('Wind Direction: ')[1].split(', ')[0]
			if(weather == "null"):
				weather = ""
			if(windDirection == "null"):
				windDirection = ""
				windSpeed = ""
			## end of URL2
			entry = {"city":city_name ,"time":time, "Concentration":PM25, "AQI":AQI, "weather":weather, "windSpeed":windSpeed, "windDirection":windDirection}
			temp.append(entry)

			break

	print temp
	return temp[0]

def get_date_name_file():
   print "running get_date"
   weekday=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
   month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
   tz = pytz.timezone('Asia/Shanghai')
   now = datetime.datetime.now(tz)
   #now=datetime.datetime.now()
   Crawl_date=weekday[now.weekday()]+'_'+month[now.month-1]+'_'+str(now.day)+str(now.hour)
   return  Crawl_date

beijingAQI_URL = 'http://www.stateair.net/web/rss/1/1.xml'
chengduAQI_URL = 'http://www.stateair.net/web/rss/1/2.xml'
guangzhouAQI_URL = 'http://www.stateair.net/web/rss/1/3.xml'
shanghaiAQI_URL = 'http://www.stateair.net/web/rss/1/4.xml'
shenyangAQI_URL = 'http://www.stateair.net/web/rss/1/5.xml'

beijingWeather_URL = 'http://open.live.bbc.co.uk/weather/feeds/en/1816670/observations.rss'
chengduWeather_URL = 'http://open.live.bbc.co.uk/weather/feeds/en/1815286/observations.rss'
guangzhouWeather_URL = 'http://open.live.bbc.co.uk/weather/feeds/en/1809858/observations.rss'
shanghaiWeather_URL = 'http://open.live.bbc.co.uk/weather/feeds/en/1796236/observations.rss'
shenyangWeather_URL = 'http://open.live.bbc.co.uk/weather/feeds/en/2034937/observations.rss'

#stream_output = '/data/AirPollution/stream/air_data.csv'
now_output = '/data/AirPollution/tests/air_data.csv'

beijing = air_parser(beijingAQI_URL, beijingWeather_URL, 'Beijing')
chengdu = air_parser(chengduAQI_URL, chengduWeather_URL, 'Chengdu')
guangzhou = air_parser(guangzhouAQI_URL, guangzhouWeather_URL, 'Guangzhou')
shanghai = air_parser(shanghaiAQI_URL, shanghaiWeather_URL, 'Shanghai')
shenyang = air_parser(shenyangAQI_URL, shenyangWeather_URL, 'Shenyang')

temp = [beijing,chengdu,guangzhou,shanghai,shenyang]

flag = 0
if(os.path.isfile(now_output)):
	flag = 1

with open(now_output, 'a') as outfile:
	samplewriter = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	if(flag == 0): # new file
		samplewriter.writerow(['Time', 'City', 'Concentration', 'AQI', 'Weather', 'Wind_Speed', 'Wind_Direction'])
	for city_ele in temp:
		samplewriter.writerow([city_ele['time'],city_ele['city'],city_ele['Concentration'],city_ele['AQI'],city_ele['weather'],city_ele['windSpeed'],city_ele['windDirection']])
	print "job is done"













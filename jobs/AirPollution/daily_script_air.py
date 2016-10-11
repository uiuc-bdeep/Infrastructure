#!/usr/bin/env python
import urllib2
import time
import os

new_folder_path = '/data/AirPollution/tests/' + time.strftime("%d-%m-%Y")
new_file_name = 'air_data-' + time.strftime("%d-%m-%Y-%M") + '.csv'

if not os.path.exists(new_folder_path):	
	os.makedirs(new_folder_path)
os.system('mv /data/AirPollution/tests/air_data.csv ' + new_folder_path)

print "finished job2 for weekly"

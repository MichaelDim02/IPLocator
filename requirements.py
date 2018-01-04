import os
import time

def sleep_():
	time.sleep(5)
def installation():
	os.system("wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz")
	sleep_()
	os.system("gunzip GeoLiteCity.dat.gz")
	sleep_()
	os.system("sudo pip install pygeoip")
installation()

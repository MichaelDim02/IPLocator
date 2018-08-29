#####################################
#          IP LOCATOR v0.6          #  
# BY MICHAEL CONSTANTINE DIMOPOULOS #
#     THESSALONIKI GREECE 2017      #
#####################################
from __future__ import print_function
import argparse
import socket
try:
	import pygeoip
except ImportError:
	print("[!] Could not run IPlocator. Please make sure you run the requirments.py script first.")
	exit()
	

def banner():
	print(".: IP LOCATOR v0.6 :.")
	print("IP Tracing tool by Michael C. Dim. // Thessaloniki, Greece 2018")
	print("Usage: python iplocator -u [URL] / -a [IP]")
def lookup(ip):
	print("IP:", ip)
	db = pygeoip.GeoIP("GeoLiteCity.dat")
	geo_data = db.record_by_name(ip)
	print("Country: " + geo_data["country_name"].encode("utf-8"))
	if geo_data["city"]:
		print("City: " + geo_data["city"].encode("utf-8"))
	print("Longitude: " + str(geo_data["longitude"]).encode("utf-8"))
	print("Latitude: " + str(geo_data["latitude"]).encode("utf-8"))
	s = raw_input("\nDo you want to save the data in a .txt file? [Y/n]: ")
	if s == "n" or s == "N" or s == "no" or s == "No" or s == "NO":
		exit()
	else:
		f = open(str(ip) ,'w+')
		c1 = "Country: " + geo_data["country_name"].encode("utf-8") + "\n"
		f.write(str(c1))
		if geo_data["city"]:
			c2 = "City: " + geo_data["city"].encode("utf-8") + "\n"
			f.write(str(c2))
		l1 = "Longitude: " + str(geo_data["longitude"]).encode("utf-8") + "\n"
		f.write(str(l1))
		l2 = "Latitude: " + str(geo_data["latitude"]).encode("utf-8") +"\n"
		f.write(str(l2))
		f.close()
	
def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--URL", help="The URL to the website.")	
	parser.add_argument("-a", "--IP", help="The IP of the device.")
	args = parser.parse_args()
	url = args.URL
	ip = args.IP
	if ip:
		try:
    			socket.inet_aton(ip)
			lookup(ip)			
		except socket.error:
			print("Invalid IP. Exiting..")
			exit()
	elif url:
		try:
			URL_IP = socket.gethostbyname(str(url))
			lookup(URL_IP)
		except socket.gaierror:
			print("Invalid URL. Exiting..")
			exit()
	if not ip and not url:
		banner()
arguments()


import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib2 
myAPI = "WRITE API IN THINGSPEAK CHANNEL" 
def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 2) 
   return (str(RH), str(T)) 
def main(): 
   print 'starting...' 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
   while True: 
       try: 
           RH, T = getSensorData() 
           f = urllib2.urlopen(baseURL + 
                               "&field1=%s&field2=%s" % (RH, T)) 
           print f.read() 
           f.close() 
           sleep(2) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.' 
           break 
# call main 
if __name__ == '__main__': 
   main()  

#!/usr/bin/python
import Adafruit_DHT
import MySQLdb

#sensor to read 
sensor = Adafruit_DHT.AM2302

#pin sensor is wired to
pin = 4

#MariaDB connection
db = MySQLdb.connect(host="localhost", 
                     user="[USERNAME]",  
                     passwd="[PASSWORD]", 
                     db="tempreadings") 

cur = db.cursor()

add_reading = ("INSERT INTO readings"
	"(temperature, humidity, timestamp)"
	"VALUES(%s,%s, NOW())")

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

data_reading = (( 9.0/5.0 * temperature + 32),humidity)

cur.execute(add_reading,data_reading)
db.commit()

cur.close()
db.close()

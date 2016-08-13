"""
Script to get temperature
"""
import Adafruit_DHT as dht
import time
import datetime


DELAY_SECONDS = 10


while True:
    try:
        h, t = dht.read_retry(dht.DHT11, 4)
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        print "%s Temperature: %f*C Humidity: %f%%" % (str(cur_time), t, h)
        with open('/var/data/dima_weather.txt', 'a+t') as history:
            history.write("%s Temperature: %.2f*C Humidity: %.2f%%\n" % (str(cur_time), t, h))
    except Exception as ex:
        print ex
    finally:
        time.sleep(DELAY_SECONDS)




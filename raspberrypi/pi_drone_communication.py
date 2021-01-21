from sense_hat import SenseHat
import serial
import logging
import time
import os 
import pynmea2

sense = SenseHat()

logging.basicConfig(filename="machinery_log.txt",
                level=logging.DEBUG,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S')

ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)

def accleormeter():
      
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x'] 
    y = acceleration['y']
    z = acceleration['z']
    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    
    return x,y,z

def temp_humidity():
     t = sense.get_temperature()
     p = sense.get_pressure()
     h = sense.get_humidity()

     # Round the values to one decimal place
     t = round(t, 1)
     p = round(p, 1)
     h = round(h, 1)
     
     return t,p,h

def gps():
   
    data = ser.readline()
    
    if data[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
 
        msg = pynmea2.parse(data)
 
        #parse the latitude and print
        lat = msg.lat
        lon = msg.lon
        
        return lat,lon
 
def zigbee_incoming():
    incoming = ser.readline().strip()
    return incoming
    
def zigbee_sender(message):
    ser.write(message)


if __name__=="__main__":
    current = time.localtime().tm_min
    
    while 1:
        if(zigbee_incoming()=="in"):
            zigbee_sender("done")
            
            x,y,z = accleormeter()
            t,p,h = temp_humidity()
            lat,lon = gps()
            message = str(t) + " " + str(p) + " " + str(h) + " " + str(x) + " " + str(y) + " " + str(z) + " "+str(lat)+" " +str(lon)
            logging.info(message)
            
            zigbee_sender(message)
            
            
        elif(zigbee_incoming()=="update"):
            zigbee_sender("send")
            time.sleep(5)
            code = zigbee_incoming()
            a = code.split('\n')
            file = open("led_blink.py","w")
            
            for x in a:
                file.write(x)
                if(x == "while 1:"):
                    file.write("\n")
                    file.write("\t ")
                else:
                    file.write("\n")
                
            file.close()
            
            os.system("python led_blink.py")

        else:
            
            if(time.localtime().tm_min - current == 1):
                x,y,z = accleormeter()
                t,p,h = temp_humidity()
                message = str(t) + " " + str(p) + " " + str(h) + " " + str(x) + " " + str(y) + " " + str(z)+ " "+str(lat)+" " +str(lon)
                logging.info(message)
                current = time.localtime().tm_min
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    

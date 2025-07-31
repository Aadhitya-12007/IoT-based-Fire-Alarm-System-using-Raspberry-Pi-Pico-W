import MicropyGPS
import network
from machine import UART, Pin, PWM
from time import sleep
import urequests
green = Pin(15,Pin.OUT)
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("your ssid here", "your password here") #enter your wifi ssid and password
    print('Waiting for connection...')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('wifi connected ...')
    green.on()
    print(wlan.ifconfig())

connect()

# Instantiate the micropyGPS object
my_gps = MicropyGPS()

# Define the UART pins and create a UART object
gps_serial = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

red = Pin(16,Pin.OUT)

button = Pin(19,Pin.IN,Pin.PULL_UP)
buzzer = PWM(Pin(11))
buzzer.freq(1000)
def tone():
    red.on()
    buzzer.duty_u16(1000)
    sleep(0.5)

def noTone():
    red.off()
    buzzer.duty_u16(0)
    
def send(message):
    s= "your telegram bot link here&text={}".format(message) #enter your telegram bot api link here after generating using botfather
    so = urequests.get(s)
send("HEY")


while True:
    while gps_serial.any():
        data = gps_serial.read()
        for byte in data:
            stat = my_gps.update(chr(byte))
            if stat is not None:
                # Print parsed GPS data
                #print('Date:', my_gps.date_string('long'))
                print(my_gps.latitude_string(),my_gps.longitude_string())
                if(button.value()==0):
                    tone()
                    sleep(2)
                    send("FIRE!")
                    sleep(2)
                    send(my_gps.latitude_string()+my_gps.longitude_string())
                    noTone()
                #print('Longitude:', my_gps.longitude_string())
                #print('Altitude:', my_gps.altitude)
                #print('Satellites in use:', my_gps.satellites_in_use)
                #print()
                sleep(0.1)

# # main.py -- put your code here!
from machine import SPI, Pin
import time
import lib.tinypico as TinyPICO
from lib.micropython_dotstar import DotStar
import time, random, micropython
import network
import json
import upip
wlan = network.WLAN(network.STA_IF)

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    with open('config.json') as f:
        config = json.load(f)
        wlan.connect(config['ssid'], config['ssid_password'])

    wlan.isconnected()
    wlan.ifconfig()


def packages():
      upip.install("micropython-firebase-firestore")
      print("installing packages")

packages()



# Configure SPI for controlling the DotStar
# Internally we are using software SPI for this as the pins being used are not hardware SPI pins
spi = SPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) )
# Create a DotStar instance
dotstar = DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
# Turn on the power to the DotStar
TinyPICO.set_dotstar_power( True )

# Say hello
print("\nHello from TinyPICO!")
print(f"--{TinyPICO.DOTSTAR_PWR}------------------\n")

# Show some info on boot
print("Battery Voltage is {}V".format( TinyPICO.get_battery_voltage() ) )
print("Battery Charge State is {}\n".format( TinyPICO.get_battery_charging() ) )

# # Show available memory
print("Memory Info - micropython.mem_info()")
# print("------------------------------------")
micropython.mem_info()

# # Create a colour wheel index int
color_index = 0


#MQTT 
# produce data to endpoint
# if response is 200 
      # write network = True 



# # Rainbow colours on the Dotstar
while True:
      print("\nHello from TinyPICO!")
      time.sleep(3)
#     # Get the R,G,B values of the next colour
      # r,g,b = TinyPICO.dotstar_color_wheel( color_index )
#     # Set the colour on the dotstar
      # dotstar[0] = ( r, g, b, 0.5)
#     # Increase the wheel index
      # color_index += 1
#     # Sleep for 20ms so the colour cycle isn't too fast
      # time.sleep_ms(20)

      # wifi = network.WLAN(network.STA_IF)
      # wifi.active(True)
      # networks = wifi.scan()
      import esp32

      print(f'read the internal hall sensor: {esp32.hall_sensor()}, read the internal temperature of the MCU, in Fahrenheit: {esp32.raw_temperature()}, access to the Ultra-Low-Power Co-processor:  {esp32.ULP() }')
      if wlan.isconnected():
            dotstar[0] = (0, 0, 128, 0.1) # Red, half brightness
            time.sleep(.1)
            # do_connect()
            print('do_connect called')
            print(wlan.ifconfig())
      else:
            dotstar[0] = (128, 0, 0, 0.8) # Red, half brightness
            print(wlan.ifconfig())

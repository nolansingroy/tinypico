# boot.py -- run on boot-up
# import ugit
import upip
import network
import json
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    with open('config.json') as f:
        config = json.load(f)
        wlan.connect(config['ssid'], config['ssid_password'])

    wlan.isconnected()
    wlan.ifconfig()

do_connect()

upip.install('micropython-urequests')

ugit.pull_all()

# def do_connect():
    
#     sta_if = network.WLAN(network.STA_IF)
#     if not sta_if.isconnected():
#         print('connecting to network...')
#         sta_if.active(True)
#         sta_if.connect('Singroyt62', 'TBA009278NRG')
#         while not sta_if.isconnected():
#             pass
#     print('network config:', sta_if.ifconfig())


# do_connect()


# ugit.pull_all(isconnected=True)


# import ugit

# wlan = ugit.wificonnect('Singroyt62', 'TBA009278NRG')

# backup internal files
# ugit.backup()

print('leaving boot file')
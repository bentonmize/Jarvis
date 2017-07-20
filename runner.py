# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import sys
import os

def main():
    print("Sir, there are still terabytes of calculations required before an actual flight is...")

    # Get all device that connected with USB 
    connected_devices = os.popen('adb devices').read().strip().split('\n')[1:]
    devices = []
    for deviceId in connected_devices:
        # Get device name
        deviceName = deviceId.split('\t')[0]
        print('deviceName: ' + deviceName)
        
        # Get connection of device 
        device = MonkeyRunner.waitForConnection(10.0, deviceName)
        devices.append(device)

    # Set start activity
    for device in devices:
        device.startActivity(component='com.android.settings/.Settings')
    
    print ('startActivity: Settings')

if __name__ == "__main__":
    main()

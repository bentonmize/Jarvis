# Imports the monkeyrunner modules used by this program
import time
import sys
import os
from com.android.monkeyrunner import MonkeyRunner

def main():
    print("Sir, there are still terabytes of calculations required before an actual flight is...")

    # Get all device that connected with USB
    connected_devices = os.popen('adb devices').read().strip().split('\n')[1:]
    devices = []
    for device_id in connected_devices:
        # Get device name
        serial = device_id.split('\t')[0]
        print('Device Serial: ' + serial)

        # Get connection of device
        device = MonkeyRunner.waitForConnection(10.0, serial)
        devices.append(device)

    # Set start activity
    for device in devices:
        device.startActivity(component='com.android.settings/.Settings')

    print('startActivity: Settings')

if __name__ == "__main__":
    main()

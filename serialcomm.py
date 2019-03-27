import time
import serial.tools.list_ports
import visa
from visa import constants
from pyvisa.constants import StopBits, Parity
import re
import numpy
#import gui


for device in serial.tools.list_ports.comports():
    print(device)

constants.VI_ASRL_FLOW_NONE
constants.VI_ASRL_FLOW_XON_XOFF
constants.VI_ASRL_FLOW_RTS_CTS
constants.VI_ASRL_FLOW_DTR_DSR
constants.VI_ATTR_ASRL_FLOW_CNTRL

rm = visa.ResourceManager()
print(rm)
VSource = rm.open_resource("COM5", baud_rate=9600, data_bits=7, flow_control=2, parity=Parity.odd, stop_bits=StopBits.two, ask_for_values=ascii)
print(VSource)
print(VSource.query("*IDN?"))

# Reset
VSource.write("*RST")

# Disable zerocheck
VSource.write(":SYStem:ZCHeck OFF")

def setVoltageSource(voltage):
    time.sleep(0.1)
    VSource.write("*RST")
    time.sleep(0.1)
    VSource.write(":SYStem:ZCHeck OFF")
    #Set preferred voltage
    print("Range before: " + VSource.query(":SOURce:VOLTage:RANGe?"))
    VSource.write(":SOURce:VOLTage:RANGe 1000")
    print("Range after: " + VSource.query(":SOURce:VOLTage:RANGe?"))
    print(VSource.write(":SOURce:VOLTage:AMPLitude " + voltage))
    print(VSource.query("SOURce:VOLTage:AMPLitude?"))
    time.sleep(0.2)
    return

def startVoltageSource():
    VSource.write(":OUTPut1 ON")
    return


def stopVoltageSource():
    VSource.write(":OUTPut1 OFF")
    return

def startVoltageSourceTime(time):
    VSource.write(":OUTPut1 ON")
    time.sleep(int(time))
    VSource.write(":OUTPut1 ON")
    return

def toggleCurrentMeasurement():
    VSource.write("*RST")

    # Prepare for current measurement
    VSource.write(":SENSe:FUNCtion 'CURRent:DC' ")

    #Data to receive
    VSource.write(":FORMat:ELEMents READing, TSTamp")

    VSource.write("SYST:ZCH OFF")
    VSource.write("SENSe:CURR:RANGe:AUTO ON")
    VSource.write("SENSe:VOLTage:GUARd OFF")
    VSource.write("SENSe:VOLTage:GUARd OFF")
    return

def currentMeasurement():
    measurement = ""
    for x in range(0, 10):
        measurement = measurement + VSource.query(":READ?")
        time.sleep(0.1)
    print(measurement)
    #.split(',')
    
    print(measurement.splitlines())
    return
    #TODO: number of measurements over timeperiod

def reset():
    VSource.write("*RST")
    return
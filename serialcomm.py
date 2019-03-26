import time
import serial.tools.list_ports
import visa
from visa import constants
from pyvisa.constants import StopBits, Parity
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

def currentMeasurement():
    #Prepare for current measurement
    print(VSource.query(":SENSe1:FUNCtion?"))
    VSource.write(":SENSe1:FUNCtion 'CURRent:DC' ")
    print(VSource.query(":SENSe1:FUNCtion?"))

def reset():
    VSource.write("*RST")
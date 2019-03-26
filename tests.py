from serial import win32
import serial
keyInput = input(">> ")

string = bytearray(keyInput, 'ascii')

print(string)



#To achieve higher resolution in the timestamps, I use relative timing
#VSource.write('system:tstamp:type relative')

#I'm not awfully concerned with noise from the powerline, so the sync
# is turned off. This also increases the sample rate drastically.
#kt.write('system:lsync:state 0')

#display a confirmation on the screen.
#VSource.write("display:text:data 'rst succesfull'")
#Setting absolute timestamps from initiation
#VSource.write('trace:timestamp:format absolute')
#immediate triggering
#enable and set trigger to be immediate - i.e. without delay
#VSource.write('trigger:source immediate')
#Quickest measurement averaging time
#VSource.write('voltage:nplc 0.01')
#A sufficiently high resolution is selected (6digit)
#VSource.write('voltage:digits 6')

#values = VSource.query_ascii_values('CURV?', container=numpy.array)

#Definition of read prepare function
"""
def readmeas(n):
    #clear internal memory
    VSource.write('*CLS')
    VSource.write('trace:clear')
    #Select number of points and the feed control
    VSource.write('trace:points ',str(n))
    VSource.write('trace:feed:control next')

#Return to ordinary display
VSource.write('display:text:state 0')

readmeas(3000)
"""

"""
print(VSource.write('system:zcheck 0'))

if int(VSource.query(":DISPlay:TEXT:STATe?")) == 1:
    print("Text messages already enabled")
else:
    VSource.write(":DISPlay:TEXT:STATe ON")
    print("Enabling text messages...")

print(VSource.query(":DISPlay:TEXT:STATe?"))
print(VSource.write("DISPlay:WINDow2:TEXT:DATA 'test' "))

#print(VSource.write(":DISPlay:TEXT:Data lol"))
#print(VSource.query(":DISPlay:TEXT:Data?"))
"""


#print(VSource.query('*OPT?'))
#print(VSource.write(":CONFigure:VOLTage:DC"))
#print(VSource.query(':MEASure:CURRent:DC?'))

#VSource.write(":OUTPut1 ON")
#time.sleep(1)
#VSource.write(":OUTPut1 OFF")
#print(VSource.write(":VOLTage:DC::RANGe:UPPer?"))

#print(VSource.query(":DISPlay:TEXT:STATe?"))


#print(VSource.read())


# Turn of guard shield.
#VSource.write('sense:voltage:guard 0')
#Disable math
#kt.write('calculate:state 0')

#Disable filters and reference
#kt.write('sense:voltage:average:state 0')
#kt.write('sense:voltage:median:state 0')
#kt.write('sense:voltage:reference:state 0')

#Fix the voltage range
#VSource.write('sense:voltage:range 2')
#Enable user input text shown on screen
#VSource.write('display:text:state 1')

:SYSTem:ZCHeck ON ‘ Enable zero check
:SYSTem:ZCORrect:ACQuire ‘ Acquire zero correct value
:SYSTem:ZCHeck OFF ‘ Disable zero check
:SYSTem:ZCORrect ON ‘ Perform zero correction

if self.text.isdigit():
    print(self.text)
    return True;
else:
    print("Enter a number")
    return False;


    time.sleep(3)
    VSource.write("OUTPut1 OFF")
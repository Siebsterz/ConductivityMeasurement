from tkinter import *
import time
import serialcomm
from statistics import mean

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.voltage = ""
        self.warning = str("")
        self.voltageOK = False
        self.currentMeasurementVar = IntVar()
        self.currentMeasurementActivated = False
        self.current = 0

        self.pack()
        self.createWidgets()
        self.pack()

        #self.getVoltage()
        self.onUpdate()
        #self.checkCurrentMode()
        print(self.voltage)

    def createWidgets(self):
        self.voltageLabel = Label(self, text="Enter desired voltage")
        self.voltageLabel.pack()

        self.voltageEntry = Entry(self)
        self.voltageEntry.pack()
        self.voltageEntry.focus_set()

        self.warningStringVar = StringVar()
        self.warningStringVar.set("test")
        self.warning = Label(self, textvariable=self.warningStringVar)
        self.warning.pack()

        self.buttonSubmit = Button(self, text="Set voltage", command=self.getVoltage)
        self.buttonSubmit.pack()

        self.buttonStart = Button(self, text="Turn on voltage source", command=serialcomm.startVoltageSource)
        self.buttonStart.pack()

        self.buttonStop = Button(self, text="Turn off voltage source", command=serialcomm.stopVoltageSource)
        self.buttonStop.pack()

        self.buttonCurrentMeasurement = Button(self, text="Measure current", command=self.measureCurrent)
        self.buttonCurrentMeasurement.pack()

        self.buttonSheetRes = Button(self, text="Calculate Sheet Resistance", command=self.calculateSheetResistance)
        self.buttonSheetRes.pack()

        self.checkboxCurrentMeasurement = Checkbutton(self, text="Current Measurement Mode", variable=self.currentMeasurementVar)
        self.checkboxCurrentMeasurement.pack()

        self.buttonReset = Button(self, text="RESET", fg="#f46e42", command=self.reset)
        self.buttonReset.pack()

        self.QUIT = Button(self, text="QUIT", fg="red", command=quitApp)
        self.QUIT.pack(side="bottom")

    def getVoltage(self):
        self.voltage = self.voltageEntry.get()
        self.voltageOK = False
        print(self.voltage)
        if self.voltage == "":
            self.warningStringVar.set("Enter a value")
        elif not self.voltage.isdigit():
            self.warningStringVar.set("Enter a real number")
        elif int(self.voltage) > 1000:
            self.warningStringVar.set("Max 1000V!")
        else:
            self.voltageOK = True
            return

    def setVoltage(self, voltage):
        serialcomm.setVoltageSource(voltage)

    def checkCurrentMode(self):
        if not self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            serialcomm.toggleCurrentMeasurement()
            self.currentMeasurementActivated = True
            return True
        elif self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            return True
        else:
            self.currentMeasurementActivated = False
            return False

    def measureCurrent(self):
        if self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            self.current = serialcomm.currentMeasurement()
            return True
        else:
            #TODO make label instead of print
            print("Activate current measurement mode plz")
            return False

    def calculateSheetResistance(self):
        # average current measurements
        avgCurrent = mean(self.current)

        # calculation
        rho = (53.4 * int(self.voltage)) / avgCurrent
        print("Applied voltage = " + str(self.voltage))
        print("Average current = " + str(avgCurrent))
        print("Sheet Resistance = " + str(rho) + "ohms")
        return rho

    def onUpdate(self):

        #Current Mode activated?
        self.checkCurrentMode()

        #Look for voltage to apply
        if self.voltageOK:
            self.setVoltage(self.voltage)
            self.voltageOK = False;
            self.after(1000, self.onUpdate)
        else:
            self.after(1000, self.onUpdate)

    def reset(self):
        self.currentMeasurementVar.set(0)
        serialcomm.reset()

def quitApp():
    serialcomm.reset()
    serialcomm.VSource.close()
    root.destroy()


root = Tk()
root.title("Conductivity Measurement")
root.geometry("300x300")
root.protocol("WM_DELETE_WINDOW", quitApp)
app = Application(master=root)
app.pack()
root.mainloop()
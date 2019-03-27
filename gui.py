from tkinter import *
import time
import serialcomm

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.text = str("")
        self.warning = str("")
        self.voltageOK = False
        self.currentMeasurementVar = IntVar()
        self.currentMeasurementActivated = False

        self.pack()
        self.createWidgets()
        self.pack()

        #self.getVoltage()
        self.onUpdate()
        #self.checkCurrentMode()
        print(self.text)

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

        self.buttonReset = Button(self, text="RESET", fg="#f46e42", command=self.reset)
        self.buttonReset.pack()

        self.checkboxCurrentMeasurement = Checkbutton(self, text="Current Measurement Mode", variable=self.currentMeasurementVar)
        self.checkboxCurrentMeasurement.pack()

        self.QUIT = Button(self, text="QUIT", fg="red", command=self.quitApp)
        self.QUIT.pack(side="bottom")

    def getVoltage(self):
        self.text = self.voltageEntry.get()
        self.voltageOK = False
        print(self.text)
        if self.text == "":
            self.warningStringVar.set("Enter a value")
        elif not self.text.isdigit():
            print("No number")
            self.warningStringVar.set("Enter a real number")
        elif int(self.text) > 1000:
            self.warningStringVar.set("Max 1000V!")
        else:
            print(self.text)
            self.voltageOK = True
            return self.voltageOK

    def setVoltage(self, voltage):
        print("set voltage")
        serialcomm.setVoltageSource(voltage)

    def checkCurrentMode(self):
        print("Current mode: " + str(self.currentMeasurementVar.get()))
        print("Var: " + str(self.currentMeasurementActivated))
        if not self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            print("toggle")
            serialcomm.toggleCurrentMeasurement()
            self.currentMeasurementActivated = True
            return True
        elif self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            print("toggled")
            return True
        else:
            self.currentMeasurementActivated = False
            return False

    def measureCurrent(self):
        if self.currentMeasurementActivated and self.currentMeasurementVar.get() == 1:
            serialcomm.currentMeasurement()
            return True
        else:
            print("Activate current measurement mode plz")
            return False

    def onUpdate(self):
        print("onUpdate started")

        #Current Mode activated?
        self.checkCurrentMode()

        #Look for voltage to apply
        if self.voltageOK:
            self.setVoltage(self.text)
            self.voltageOK = False;
            self.after(1000, self.onUpdate)
        else:
            print("waiting for number")
            self.after(1000, self.onUpdate)

    def reset(self):
        self.currentMeasurementVar.set(0)
        serialcomm.reset()

    def quitApp(self):
        serialcomm.reset()
        serialcomm.VSource.close()
        root.destroy()


root = Tk()
root.title("Conductivity Measurement")
app = Application(master=root)
app.pack()
root.mainloop()
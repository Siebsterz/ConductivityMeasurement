from tkinter import *
import time
import serialcomm

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.text = str("")
        self.warning = str("")
        self.voltageOK = False;

        self.pack()
        self.createWidgets()
        self.pack()

        #self.getVoltage()
        self.onUpdate()
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

    def onUpdate(self):
        print("onUpdate started")
        if self.voltageOK:
            self.setVoltage(self.text)
            self.voltageOK = False;
            self.after(1000, self.onUpdate)
        else:
            print("waiting for number")
            self.after(1000, self.onUpdate)

    def quitApp(self):
        serialcomm.reset()
        serialcomm.VSource.close()
        root.destroy()

root = Tk()
root.title("Conductivity Measurement")
app = Application(master=root)
app.pack()
root.mainloop()

#threads
#qt
#multiprocessing
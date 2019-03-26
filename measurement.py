class Measurement:
    def __init__(self):
        self.voltage = float(0)
        self.resistance = float(0)
        self.current = float(0)

    def printMeasurement(self):
        print("Voltage = " + str(self.voltage) + ", Current = " + str(self.current))

    def getVoltage(self):
        return self.voltage

    def getCurrent(self):
        return self.current

    def getResistance(self):
        return self.resistance

    def setVoltage(self, analog_voltage):
        self.voltage = analog_voltage * (5.0 / 1023.0)

    def setCurrent(self):
        self.current = self.voltage / self.resistance

    def setResistance(self, newResistance):
        self.resistance = float(newResistance)

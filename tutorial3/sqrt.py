from breezypythongui import EasyFrame
import math

class sqrt(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Sqrt Calc")
        self.addLabel(text="Enter the Number:", row=0, column=0)
        self.inputField = self.addFloatField(value=0.0, row=0, column=1, width=15)
        self.addLabel(text="sqrt:", row=1, column=0)
        self.resultField = self.addFloatField(value=0.0, row=1, column=1, width=15, precision=2)
        self.resultField["state"] = "readonly"
        self.addButton(text="Compute sqrt", row=2, column=0, columnspan=2, command=self.Sqrt_c)

    def Sqrt_c(self):
        try:
            num = self.inputField.getNumber()
            if num < 0:
                raise ValueError()
            self.resultField.setNumber(math.sqrt(num))
        except:
            self.messageBox("Invalid i/p", "Please enter a valid non -ve number.")

if __name__ == "__main__":
    sqrt().mainloop()

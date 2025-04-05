from breezypythongui import EasyFrame

class cap(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Convert to UpperCase")

        
        self.addLabel(text="Enter the Text to be converted:", row=0, column=0)
        self.inputField = self.addTextField(text="", row=0, column=1, width=30)

       
         self.addButton(text="Convert", row=1, column=0, columnspan=2, command=self.convertToUpper)

        
        self.resultLabel = self.addLabel(text="Result:", row=2, column=0, columnspan=2, sticky="NSEW")

    def convertToUpper(self):
        text = self.inputField.getText()
        self.resultLabel["text"] = f"Result: {text.upper()}"


if __name__ == "__main__":
    cap().mainloop()

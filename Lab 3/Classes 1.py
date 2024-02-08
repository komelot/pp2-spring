class String:
    def __init__(self):
        self.string = ""

    def printString(self):
        self.string =(input("Enter the string: "))
        return self.string.upper()

    def getString(self):
        self.string = (input("Enter the string: "))
        return self.string

s = String()
print(s.printString())
print(s.getString())





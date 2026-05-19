class HellCat:

    def __init__(self, name, color, eyeColor):
        # initalizing
        if name.strip().isalpha():
            self.__name__ = name.strip()

        if color.strip().isalpha():
            self.color = color.strip()

        if eyeColor.strip().isalpha():
            self.eyeColor = eyeColor.strip()

        self.__wearing__ = True

    def __str__(self):
        # incase of print
        return "uh, you cant print a car..."


    def toggleOn(self):
        # taking off/putting on
        if self.__wearing__:
            self.__wearing__ = False

        else:
            self.__wearing__ = True


    def isOn(self):
        # checks if on
        return self.__wearing__
    

    def dye(self,new):
        # changing color
        if new.strip().isalpha():
            self.color = new.strip()
            print("badge color changed to", self.color)


bob = HellCat("bob",input("body color: "), input("eye color: "))
bob.dye(input("new body color: "))
class HellCat:

    def __init__(self, color, eyeColor):
        # initalizing

        if color.strip().isalpha():
            self.__color = color.strip()

        if eyeColor.strip().isalpha():
            self.__eyeColor = eyeColor.strip()

        self.__wearing = True

    def __str__(self):
        # incase of print
        return "uh, you cant print a car..."


    def toggleOn(self):
        # taking off/putting on
        if self.__wearing:
            self.__wearing = False

        else:
            self.__wearing = True


    def isOn(self):
        # checks if on
        return self.__wearing
    

    def checkEye(self):
        return self.__eyeColor


    def dye(self,new):
        # changing color
        if new.strip().isalpha():
            self.__color = new.strip()
            print("badge color changed to", self.__color)


bob = HellCat(input("body color: "), input("eye color: "))
bob.dye(input("dye color: "))
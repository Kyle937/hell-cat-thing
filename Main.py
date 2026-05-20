class HellCat:

    def __init__(self, color, eyeColor):
        # initalizing

        if color.strip().isalpha():
            self.__color__ = color.strip()

        if eyeColor.strip().isalpha():
            self.__eyeColor__ = eyeColor.strip()

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
            self.__color__ = new.strip()
            print("badge color changed to", self.__color__)


bob = HellCat(input("body color: "), input("eye color: "))
bob.dye(input("dye color: "))
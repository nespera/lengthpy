class LengthUnit:

    def __init__(self, short_name, millimetres):
        self.short_name = short_name
        self.millimetres = millimetres 

    def __str__(self):
        return self.short_name

YARD = LengthUnit('yd', 9140)
METRE = LengthUnit('m', 1000)
INCH = LengthUnit('in', 254)


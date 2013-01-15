class LengthUnit:

    def __init__(self, short_name, millimetres):
        self.short_name = short_name
        self.millimetres = millimetres 

    def __str__(self):
        return self.short_name

YARD = LengthUnit('yd', 9140)
METRE = LengthUnit('m', 1000)
INCH = LengthUnit('in', 254)

class Length:

    def __init__(self, magnitude, unit):
        self.magnitude = magnitude
        self.unit = unit

    def __str__(self):
        return '%.2f %s' %(self.magnitude, self.unit)

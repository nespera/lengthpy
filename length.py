class _LengthUnit:

    def __init__(self, short_name, millimetres):
        self._short_name = short_name
        self._millimetres = millimetres 

    def __str__(self):
        return self._short_name

YARD = _LengthUnit('yd', 9140)
METRE = _LengthUnit('m', 1000)
INCH = _LengthUnit('in', 254)

class Length:

    def __init__(self, magnitude, unit):
        self.magnitude = magnitude
        self.unit = unit

    def __str__(self):
        return '%.2f %s' %(self.magnitude, self.unit)

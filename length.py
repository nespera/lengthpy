class _LengthUnit:

    def __init__(self, short_name, millimetres):
        self._short_name = short_name
        self._millimetres = millimetres 

    def __str__(self):
        return self._short_name

    def to_mm(self, size):
        return float(size) * float(self._millimetres)

    def from_mm(self, mm):
	return float(mm) / float(self._millimetres)

YARD = _LengthUnit('yd', 914)
METRE = _LengthUnit('m', 1000)
INCH = _LengthUnit('in', 254)

class Length:

    def __init__(self, magnitude, unit):
        self.magnitude = magnitude
        self.unit = unit

    def __str__(self):
        return '%.2f %s' % (self.magnitude, self.unit)

    def convert_to(self, to_unit):
        mm = self.unit.to_mm(self.magnitude)
        return Length(to_unit.from_mm(mm), to_unit)

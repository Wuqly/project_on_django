class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)
    
    def to_erl(self, value):
        return "%04d" % value
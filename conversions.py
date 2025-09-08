from config import CONVERSIONS

def convert_t(value, from_unit, to_unit):
    units = CONVERSIONS['Temperature']['units']
    if from_unit not in units or to_unit not in units:
        return None
    if from_unit == to_unit:
        result = value
        return result
    if from_unit == 'C' and to_unit == 'F':
        result = value*9/5+32
        return result
    if from_unit == 'C' and to_unit == 'K':
        result = value+273.15
        return result
    if from_unit == 'F' and to_unit == 'C':
        result = (value-32)*5/9
        return result
    if from_unit == 'F' and to_unit == 'K':
        result = (value-32)*5/9+273.15
        return result
    if from_unit == 'K' and to_unit == 'C':
        result = value-273.15
        return result
    if from_unit == 'K' and to_unit == 'F':
        result = (value-273.15)*9/5+32
        return result

def convert(value, from_unit, to_unit, conversion_type):
    if conversion_type == 'Temperature':
        return convert_t(value, from_unit, to_unit)

    else:
        factors = CONVERSIONS[conversion_type]['factors']
        if from_unit not in factors or to_unit not in factors:
            return None
        result = value * factors[from_unit] / factors[to_unit]
        return result

from config import CONVERSIONS

def convert(value, from_unit, to_unit, conversion_type):
    factors = CONVERSIONS[conversion_type]['factors']

    if from_unit not in factors or to_unit not in factors:
        return None
    
    result=value * factors[from_unit] / factors[to_unit]
    return result
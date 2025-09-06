def convert(value, from_unit, to_unit):
    conversions={'m':1, 'in':0.0254, 'ft':0.3048, 'yd':0.9144, 'mi':1609}
    if from_unit not in conversions or to_unit not in conversions:
        return None
    result=value * conversions[from_unit] / conversions[to_unit]
    return result
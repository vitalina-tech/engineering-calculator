import math


CONVERSIONS = {
    'Length': {
        'units': ['m', 'ft', 'in', 'yd', 'mi'],
        'factors': {'m': 1, 'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144, 'mi': 1609}
    },
    'Weight': {
        'units': ['kg', 'lb', 'oz', 'g'],
        'factors': {'kg': 1, 'lb': 0.453592, 'oz': 0.0283495, 'g': 0.001}
    },
    'Angle': {
        'units': ['deg', 'rad', 'grad'],
        'factors': {'deg': 1, 'rad': math.pi/180, 'grad': 0.9}
    },
    'Temperature': {
        'units': ['C', 'F', 'K']
    }
}

COLORS = {
    'background': '#0a1c70',
    'text': '#f5f5f5',
    'button': '#ffd447',
    'button_text': '#1a1a1a'
}

WINDOW_SIZE = "600x450"
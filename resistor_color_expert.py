def resistor_label(colors):
    color_map = {
        'black':0,
        'brown':1,
        'red':2,
        'orange':3,
        'yellow':4,
        'green':5,
        'blue':6,
        'violet':7,
        'grey':8,
        'white':9
    }
    
    tol_map = {
        'grey': 0.05,
        'violet': 0.1,
        'blue': 0.25,
        'green': 0.5,
        'brown': 1,
        'red': 2,
        'gold': 5,
        'silver': 10
    }
    
    prefixes = [
       (1000000000,'gigaohms'),
       (1000000,'megaohms'),
       (1000,'kiloohms')
    ]
    
    def format_value(val,factor):
        v = val / factor
        return f'{v:.15g}'
    
    if len(colors) == 1:
        return '0 ohms'
    
    if len(colors) == 4:
        result = color_map[colors[0]]*10 + color_map[colors[1]]
        result *= 10**color_map[colors[2]]
        if result == 0:
            return f'0 ohms ±{tol_map[colors[3]]}%'
        for factor,name in prefixes:
            if result >= factor:
                return f'{format_value(result,factor)} {name} ±{tol_map[colors[3]]}%'
        return f'{result} ohms ±{tol_map[colors[3]]}%'
    elif len(colors) == 5:
        result = color_map[colors[0]]*100 + color_map[colors[1]]*10 + color_map[colors[2]]
        result *= 10**color_map[colors[3]]
        if result == 0:
            return f'0 ohms ±{tol_map[colors[4]]}%'
        for factor,name in prefixes:
            if result >= factor:
                return f'{format_value(result,factor)} {name} ±{tol_map[colors[4]]}%' 
        return f'{result} ohms ±{tol_map[colors[4]]}%'

print(resistor_label(['black']))
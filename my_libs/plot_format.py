import re

def tex_times(s, omitplus=True, unit=''):
    if 'e' in s:
        mantissa, exponent = s.split('e')
        exponent = int(exponent.replace('+', '')) if omitplus else int(exponent)
        return r'${} \times 10^{{{:d}}}$'.format(mantissa, exponent)+r' '+tex_unit(unit)
    return s

def tex_unit(unit_string):
    # Using regular expression to find units and their exponents
    units = re.findall(r'([A-Za-z]+)(?:-([0-9]+))?', unit_string)
    formatted_units = []
    for unit, exponent in units:
        if exponent:
            formatted_unit = r'\mathrm{' + unit + r'^{-' + exponent + r'}}'
        else:
            formatted_unit = r'\mathrm{' + unit + r'}'
        formatted_units.append(formatted_unit)
    
    return r'$'+r'\cdot{}'.join(formatted_units)+r'$'
#!/usr/bin/env python3.3
'''
Created on 09/01/2013
@summary: A simple command line Unit Converter which allows conversions between basic unit.
@author: iseijin
'''

import unit_converter.converters
import sys

def main():
    welcome_message = (
        "Welcome to our Python-powered Unit Converter v1.0 by iseijin!\n\n"
        "You can convert Lengths, Masses , Volumes & Temperatures\n"
        "within units of the same category, which are shown below. E.g.: 1 mi in ft\n\n"
        "    Lengths: ft cm mm mi m yd km in\n"
        "    Masses: lb mg kg oz g\n"
        "    Volumes: flozUK flozUS qtUK qtUSdry qtUSliq cupSI cupUS galUK galUSdry galUSliq pintUK pintUSdry pintUSliq mL L\n"
        "    Temperatures: c f k"
    )
    help_message = (
        "    Lengths: ft cm mm mi m yd km in\n"
        "    Masses: lb mg kg oz g\n"
        "    Volumes: flozUK flozUS qtUK qtUSdry qtUSliq cupSI cupUS galUK galUSdry galUSliq pintUK pintUSdry pintUSliq mL L\n"
        "    Temperatures: c f k"
    )
    # Lists of all units
    length_units = ['ft', 'cm', 'mm', 'mi', 'm', 'yd', 'km', 'in']
    mass_units = ['lb', 'mg', 'kg', 'oz', 'g']
    vol_units = ['flozUK', 'flozUS', 'qtUK', 'qtUSdry', 'qtUSliq', 'cupSI', 'cupUS', 'galUK', 'galUSdry', 'galUSliq', 'pintUK', 'pintUSdry', 'pintUSliq', 'mL', 'L']
    temp_units = ['c', 'f', 'k']
    all_units = length_units + mass_units + vol_units + temp_units
    # Dictionary to format units with full names.
    unit_names = {
                  'ft': "feet", 'cm': "centimetres", 'mm': "millimetres", 'mi': "miles", 'm': "metres", 'yd': "yards", 'km': "kilometres", 'in': "inches",
                  'lb': "pounds", 'mg': "milligrams", 'kg': "kilograms", 'oz': "ounces", 'g': "grams", 'flozUK': "fluid ounces[UK]", 'flozUS': "fluid ounces[US]",
                  'qtUK': "quarts[UK]", 'qtUSdry': "quarts[US, dry]", 'qtUSliq': "quarts[US, liquid]", 'cupSI': "cups[metric]", 'cupUS': "cups[US]",
                  'galUK': "gallons[UK]", 'galUSdry': "gallons[US, dry]", 'galUSliq': "gallons[US, liquid]", 'pintUK': "pint[UK]", 'pintUSdry': "pint[US, dry]",
                  'pintUSliq': "pint[US, liquid]", 'mL': "millilitres", 'L': "litres", 'c': "degrees Celcius", 'f': "degrees Fahrenheit", 'k': "degrees Kelvin"
                  }
    print(welcome_message)
    while True: # Loop program till exit
        while True: # Loop for input validation
            try:
                usr_input = input("\nConvert [AMT SOURCE_UNIT in DEST_UNIT, or (h)elp or (q)uit]:\n")
                if usr_input in ['q', 'quit']:
                    print("Will now exit...")
                    sys.exit(0)
                elif usr_input in ['h', 'help']:
                    print(help_message)
                    break
                input_list = usr_input.split(" ", 3)
                amount = float(input_list[0])
                source_unit = input_list[1]
                dest_unit = input_list[3]
                if source_unit == dest_unit:
                    print("%0.2f %s = %0.4f %s. You are a little bit silly." % (amount, unit_names[source_unit], amount, unit_names[dest_unit]))
                elif source_unit not in all_units or dest_unit not in all_units:
                    raise Exception
                elif source_unit in length_units and dest_unit in length_units:
                    conversion = unit_converter.converters.Length()
                    result = conversion.convert(amount, source_unit, dest_unit)
                    print("%0.2f %s = %0.4f %s." % (amount, unit_names[source_unit], result, unit_names[dest_unit]))
                elif source_unit in mass_units and dest_unit in mass_units:
                    conversion = unit_converter.converters.Mass()
                    result = conversion.convert(amount, source_unit, dest_unit)
                    print("%0.2f %s = %0.4f %s." % (amount, unit_names[source_unit], result, unit_names[dest_unit]))
                elif source_unit in vol_units and dest_unit in vol_units:
                    conversion = unit_converter.converters.Volume()
                    result = conversion.convert(amount, source_unit, dest_unit)
                    print("%0.2f %s = %0.4f %s." % (amount, unit_names[source_unit], result, unit_names[dest_unit]))
                elif source_unit in temp_units and dest_unit in temp_units:
                    conversion = unit_converter.converters.Temperature()
                    result = conversion.convert(amount, source_unit, dest_unit)
                    print("%0.2f %s = %0.4f %s." % (amount, unit_names[source_unit], result, unit_names[dest_unit]))
                else:
                    print("Error: Units must be in the same category.")
                break
            except (ValueError, Exception):
                print("Error: Wrong format.")
    
if __name__ == '__main__':
    main()
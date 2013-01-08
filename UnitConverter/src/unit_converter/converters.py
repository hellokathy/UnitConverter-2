'''
Created on 09/01/2013

@author: iseijin
'''
# Unit conversion using factors
# new_amount = amount * factor_source/factor_dest

class Length():
    def __init__(self):
        # Length Factors (all in metres)
        self.factors = {
                        'in': 0.0254,
                        'ft': 0.3048,
                        'yd': 0.9144 ,
                        'mi': 1609.344 ,
                        'mm': 0.001,
                        'cm': 0.01,
                        'm': 1.0,
                        'km': 1000.0
                        }
        
    def convert(self, amt, src, dest):
        self.amount = amt
        self.src_factor = self.factors[src]
        self.dest_factor = self.factors[dest]
        return self.amount * (self.src_factor/self.dest_factor)
        
class Mass():
    def __init__(self):
        # Mass Factors (all in g)
        self.factors = {
                        'oz': 28.349523125,
                        'lb': 453.59237,
                        'mg': 0.001,
                        'g': 1,
                        'kg': 1000
                        }
        def convert(self, amt, src, dest):
            self.amount = amt
            self.src_factor = self.factors[src]
            self.dest_factor = self.factors[dest]
            return self.amount * (self.src_factor/self.dest_factor)
class Volume():
    def __init__(self):
        # Volume Factors (all in mL)
        self.factors = {
                        'cupSI': 250.0, 
                        'cupUS': 236.5882365, 
                        'flozUK': 28.4130742, 
                        'flozUS': 29.5735296, 
                        'qtUK': 1136.52297, 
                        'qtUSdry': 1101.22095, 
                        'qtUSliq': 946.352946, 
                        'pintUK': 568.26125, 
                        'pintUSdry': 550.610475, 
                        'pintUSliq': 473.176473,
                        'galUK': 4546.09, 
                        'galUSdry': 4404.8838, 
                        'galUSliq': 3785.411784,
                        'mL': 1.0, 
                        'L': 1000.0
                        }
    def convert(self, amt, src, dest):
        self.amount = amt
        self.src_factor = self.factors[src]
        self.dest_factor = self.factors[dest]
        return self.amount * (self.src_factor/self.dest_factor)

class Temperature():
    # Couldn't work out a nice way of doing temp conversion like with the factors so fuck the police.
    # Temperature: c f k
    def __init__(self):
        self.amount = 0
        self.source = ''
        self.destination = ''
    def convert(self, amt, src, dest):
        self.amount = amt
        self.source = src
        self.destination = dest
        if self.source == 'c' and self.destination == 'f':
            return self.amount * (9.0/5.0) + 32
        elif self.source == 'c' and self.destination == 'k':
            return self.amount + 273.2
        elif self.source == 'f' and self.destination == 'c':
            return (self.amount - 32) * (5.0/9.0)
        elif self.source == 'f' and self.destination == 'k':
            # Convert to celcius first
            return (self.amount - 32) * (5.0/9.0) + 273.2
        elif self.source == 'k' and self.destination == 'c':
            return self.amount - 273.2
        elif self.source == 'k' and self.destination == 'f':
            # Convert to celcius first
            return (self.amount - 273.2) * (9.0/5.0) + 32
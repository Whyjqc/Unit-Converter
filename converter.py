# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:58:15 2020

@author: why_j
"""
# This unit converter works by taking a unit and changing it into
# the appropriate si unit for that measurement. Then it's converted
# into whatever unit is requested.

# This converter is not intended to stand alone. It is intended to 
# work with an equation solver. So features that are not used, such
# as including unit name and the dimention measured in the Unit class
# are put there to help facilitate future functions.


class Unit():
    def __init__(self,name,measure,standard):
        # Unit name
        self.name=name
        # To what does the unit apply? (time, space, mass, ect.)
        self.measure=measure
        # How many of this unit is one of the si unit for this
        # measure?
        self.standard=standard
            
    def convert(self,num,out):
        #This is the conversion method
        #num is the numerical value to be converted
        #out is the unit to be converted to
        m=self.standard*num
        x=m/out.standard
        return x
           
        
# Units
# Metric        
decimeter=Unit('decimeter','space',0.1)
centimeter=Unit('centimeter','space',0.01)
meter=Unit('meter','space',1)
kilometer=Unit('kilometer','space',1000)
gram=Unit('gram','mass',0.001)
kilogram=Unit('kilogram','mass',1)

# English
inch=Unit('inch','space',1/39.3696)
foot=Unit('foot','space',1/3.2808)
yard=Unit('yard','space',3/3.2808)
mile=Unit('mile','space',5280/3.2808)
pound_mass=Unit('pound_mass','mass',1/2.046)

# Both/Neither
second=Unit('second','time',1)
minute=Unit('minute','time',60)
hour=Unit('hour','time',3600)
day=Unit('day','time',86400)
year=Unit('year','time',31536000)


print(minute.convert(60,second))

# To convert something use the name of the unit to be converted.
# type '.convert' after
# then(number of units to be converted,unit to be converted to)

# Example:
# inch.convert(12,foot)
# the output is 1 because there are 12 inches in 1 foot.



        

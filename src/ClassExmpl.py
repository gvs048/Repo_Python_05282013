'''
Created on May 23, 2013

@author: Tsss-Pc1
'''

class Vehicle :
    
    name = ''
    color=''
    valueis=100
    
    def description(self):
        print(self.name+" car color is "+self.color+" and cost is "+self.valueis)
        
        
obj1 = Vehicle();
obj1.name='Rao'
obj1.color='Meroon'
obj1.valueis='5000'
obj1.description()


obj2 = Vehicle();
obj2.name='gvs'
obj2.color='red'
obj2.valueis='8000'
obj2.description()

#from distutils.archive_util import make_archive


class motorcycle():
    is_light_on = False
    is_engine_on = False
    make = None
    model = None
    
    def turn_light_off(self):
        self.is_light_on = True
        
    def __init__(self, make, model):
        self.make = make
        self.model = model

moto = motorcycle("jo", "Cho")
print(moto.is_light_on)
moto.turn_light_off()
print(moto.is_light_on)

# print(motorcycle().is_light_on)
# print(motorcycle().is_light_off)

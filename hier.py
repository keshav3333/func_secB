class Mtca:
    chairman ='Mr. Sunil '
    location = 'Palamaner'
    college  = 'MTCA'

    def __init__(self,name,mobile):
        self.name = name 
        self.mobile = mobile

class Mca(Mtca):
    principal = 'Mr. Prabhakar naidu'
    strength  = 240
    staff     = 9
class Btech(Mtca):
    principal = 'Ms. Sravani'
    strength  = 350
    staff     = 35

Navyasree = Mca('Navyasree',7896787744)
Rajashekhar = Btech('Rajashekhar',7578934526)

class Mtca:
    principal = 'Mr.Prabhakar Naidu'
    college = 'MTCA'
    location = 'Palamaner'

    def __init__(self,name,mob,email,sem):
        self.name = name
        self.mobile = mob
        self.email = email
        self.sem  = sem

    def update_mob(self,new):
        self.mobile =new
        print('mobile number updated')

    @classmethod
    def change_principal(cls,new):
        cls.principal=new

    @staticmethod
    def add(a,b):
        return a+b


mohan = Mtca('mohan',8906713245,'m@gmail.com','1st')
mounika = Mtca('mounika',8899760123,'mo@gmail.com','1st')


from POO.Persona import Persona

class Vendedor(Persona):
    
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    
    def get_name(self):
        return super().get_name()    
    
    def get_email(self):
        return self.email
    
    def __str__(self):
        return super().__str__()
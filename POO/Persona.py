class Persona:
    
    def __init__(self, name='None'):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f'Clase {self.__class__.__name__} ejecutandose, nombre: {self.get_name()}'
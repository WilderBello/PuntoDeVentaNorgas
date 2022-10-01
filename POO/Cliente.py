from POO.Persona import Persona

class Cliente(Persona):
    
    def __init__(self, document, name, telf, direccion, ref, estado, deuda, anotacion, vendedor, id_pedido, fecha_pedido):
        super().__init__(name)
        self.document = document
        self.telf = telf
        self.direccion = direccion
        self.ref = ref
        self.estado = estado
        self.deuda = deuda
        self.anotacion = anotacion
        self.vendedor = vendedor
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
    
    def get_name(self):
        return super().get_name()    
    
    def get_document(self):
        return self.document
    
    def get_telf(self):
        return self.telf
    
    def get_direccion(self):
        return self.direccion
    
    def get_ref(self):
        return self.ref
    
    def get_estado(self):
        return self.estado
    
    def get_deuda(self):
        return self.deuda
    
    def get_anotacion(self):
        return self.anotacion
    
    def get_vendedor(self):
        return self.vendedor
    
    def get_id_pedido(self):
        return self.id_pedido
    
    def get_fecha_pedido(self):
        return self.fecha_pedido
    
    def __str__(self):
        return f'Documento: {self.document}, Nombre: {self.name},  Telefono: {self.telf}, Direccion: {self.direccion}, ref: {self.ref}, estado: {self.estado}, deuda: {self.deuda}, anotacion: {self.anotacion}, vendedor: {self.vendedor}, id_pedido: {self.id_pedido}, fecha_pedido: {self.fecha_pedido}'

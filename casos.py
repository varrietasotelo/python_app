class casos:
    def __init__(self, _id, ID, Fecha, DIVIPOLA, Ciudad , Departamento , atencion, Edad, Sexo, Tipo, Estado, Pais):
        self._id = _id
        self.ID = ID
        self.Fecha = Fecha
        self.DIVIPOLA = DIVIPOLA
        self.Ciudad = Ciudad
        self.Departamento = Departamento
        self.atencion = atencion
        self.Edad = Edad
        self.Sexo = Sexo
        self.Tipo = Tipo
        self.Estado = Estado
        self.Pais = Pais     
       
    def ToDB(self):
        return{
            'ID de caso': self.ID,
            'Fecha': self.Fecha,
            'Código DIVIPOLA': self.DIVIPOLA,
            'Ciudad': self.Ciudad,
            'Departamento': self.Departamento,
            'atencion': self.atencion,
            'Edad': self.Edad,
            'Sexo': self.Sexo,
            'Tipo': self.Tipo,
            'Estado': self.Estado,
            'Pais de procedencia': self.Pais
            }
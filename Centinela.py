class Tratamiento:
    def __init__(self, dni, name, lastname, codigo, monto_base, complejidad, id_algoritmo):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.codigo = codigo
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.id_algoritmo = id_algoritmo

    def __str__(self):
        return (f"-Dni:{self.dni}-Nombre:{self.name}-Apellido{self.lastname}-Codigo{self.codigo}-"
                f"Monto Base{self.monto_base}-Complejidad{self.complejidad}-Id del algoritmo{self.id_algoritmo}")



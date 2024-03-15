class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


persona1=Persona()
persona1.inicializar("Miqueas")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Joaco")
persona2.imprimir()
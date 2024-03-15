class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir (self):
        print(f"Nombre,self.nombre")
        print(f"Nota,self.nota")

    def  mostrar_nota (self):
        if self.nota>=4:
            print(f"tu nota es regular")
        else:
            print(f"quedaste libre ")

alumno1=Alumno()
alumno1.inicializar("Franco",7)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("Lucia",6)
alumno2.imprimir()
alumno2.mostrar_estado()

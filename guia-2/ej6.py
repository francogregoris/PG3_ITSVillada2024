class familia:
    def __init__(self,nom_padre,nom_madre,hijos=[]) :
        self.nom_padre=nom_padre
        self.nom_madre=nom_madre
        self.hijos = hijos
 
    def __str__(self) :
        hijos_str = ', '.join(self.hijos)
        return f"Papá: {self.nom_padre}, Mamá: {self.nom_madre}, Hijos: {hijos_str}"

flia = familia("Calderón", "Momo", ["Cusco", "Ingeniero"])
print(flia)
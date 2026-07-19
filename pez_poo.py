class Pez :
    def __init__(self,nombre,nombre_cientifico,tamaño,peso,habitad,lugares_de_origen,tipo_de_cuerpo,estado_en_la_cadena_alimenticia):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.tamaño = tamaño 
        self.alimento = self.alimento
        self.peso = peso
        self.habitad = habitad
        self.lugares_de_origen = lugares_de_origen
        self.tipo_de_cuerpo = tipo_de_cuerpo
        self.estado_en_la_cadena_alimenticia = estado_en_la_cadena_alimenticia
        #Luego agregar tiempo_estimado_de_vida
        #dependiendo del pez, se puede agregar una dato adicional
    def presentar_pez(self):
        print(f"Hola, este pez es animal acuatico y se llama {self.nombre}, vive en hábitads {self.habitad}, esta especie de pez esta dispersa en {self.lugares_de_origen}")

class Pez_espada(Pez):
    def __init__(self, nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, tipo_de_cuerpo, estado_en_la_cadena_alimenticia,velocidad):
        super().__init__(nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, tipo_de_cuerpo, estado_en_la_cadena_alimenticia)
        self.velocidad = velocidad
    
    def nadar(self):
        print("Nadando   :)")
    
    def presentar_pez(self):
        print(f"Este es un {self.nombre}.")
        print(f"Su nombre cientifico es {self.nombre_cientifico}")
        print(f"Su peso es de {self.peso} kg.")
        print(f"Se tamaño es de {self.tamaño} m.")
        print(f"viven en hábitads como {self.habitad}")
        print(f"Este pez se encuentra en disperso en {self.lugares_de_origen}")
        print(f"Su velocidad es de {self.velocidad}")
        print(f"Este pez se aliemnta de {self.alimento}")
        print(f"Su estado en la cadena alimenticia es {self.estado_en_la_cadena_alimenticia}")
        print(f"Su tipo de cuerpo es {self.tipo_de_cuerpo}")

datos_pez_espada = Pez_espada()


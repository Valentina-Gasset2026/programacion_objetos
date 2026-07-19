class Pez :
    def __init__(self,nombre,nombre_cientifico,tamaño,peso,habitad,lugares_de_origen, alimento ,tipo_de_cuerpo,estado_en_la_cadena_alimenticia):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.tamaño = tamaño 
        self.peso = peso
        self.habitad = habitad
        self.lugares_de_origen = lugares_de_origen
        self.alimento = alimento
        self.tipo_de_cuerpo = tipo_de_cuerpo
        self.estado_en_la_cadena_alimenticia = estado_en_la_cadena_alimenticia
        #Luego agregar tiempo_estimado_de_vida
        #Agregar estado de conservación 
        #dependiendo del pez, se puede agregar una dato adicional
    #def presentar_pez(self):
       # print(f"Hola, este pez es animal acuatico y se llama {self.nombre}, vive en hábitads {self.habitad}, esta especie de pez esta dispersa en {self.lugares_de_origen}")

class Pez_espada(Pez):
    def __init__(self, nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, tipo_de_cuerpo, estado_en_la_cadena_alimenticia,velocidad):
        super().__init__(nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, tipo_de_cuerpo, estado_en_la_cadena_alimenticia,velocidad)
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
        print(f"Su velocidad es de {self.velocidad} km/hrs")
        print(f"Este pez se aliemnta de {self.alimento}")
        print(f"Su estado en la cadena alimenticia es {self.estado_en_la_cadena_alimenticia}")
        print(f"Su tipo de cuerpo es {self.tipo_de_cuerpo}")

datos_pez_espada = Pez_espada("Pez Espada", "Xiphias gladius", 4.5, 500, "El Pez Espada vive en aguas tropicales, subtropicales y templadas", "Norte de Hawái, Pacífico Norte y Sur (Perú y Chile), costas orientales de EEUU, México y al este de Japón", "Atún, barracuda, Pez volador, verdel, calamares, etc.", "El Pez Espada es un Pez Oseo", "Este pez se ubica en la cima de la cadena alimenticia, es decir, que es un super depredador, sin embargo, este pez tiene algunos depredadores que lo acechan, dichos depredadores son las Orcas y El marrajo dientuso(un tipo de Tiburón).", 100)
datos_pez_espada.nadar()
datos_pez_espada.presentar_pez()



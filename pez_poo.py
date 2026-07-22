from abc import ABC, abstractmethod
from PIL import Image
class Pez(ABC):
    def __init__(self,nombre,nombre_cientifico,tamaño,peso,habitad,lugares_de_origen, alimento ,tipo_de_cuerpo,estado_en_la_cadena_alimenticia, ruta_imagen=None):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.tamaño = tamaño 
        self.peso = peso
        self.habitad = habitad
        self.lugares_de_origen = lugares_de_origen
        self.alimento = alimento
        self.tipo_de_cuerpo = tipo_de_cuerpo
        self.estado_en_la_cadena_alimenticia = estado_en_la_cadena_alimenticia
        self.ruta_imagen = ruta_imagen
        #Luego agregar tiempo_estimado_de_vida
        #Agregar estado de conservación 
        #dependiendo del pez, se puede agregar una dato adicional

    def mostrar_imagen(self):
        """Abre la imagen del pez en una ventana emergente"""
        if self.ruta_imagen:
            try:
                img = Image.open(self.ruta_imagen)
                img.show()  # Esto abre la ventana del visor de imágenes de tu sistema
                print(f"Mostrando imagen: {self.ruta_imagen}")
            except FileNotFoundError:
                print(f"Error: No encontré la imagen en '{self.ruta_imagen}'")
        else:
            print("Este pez no tiene una imagen asignada.")

    @abstractmethod
    def presentar_pez(self):
      pass 

class Pez_espada(Pez):
    def __init__(self, nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, velocidad, ruta_imagen=None):
        super().__init__(nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, ruta_imagen)
        self.velocidad = velocidad
    
    def nadar(self):
        print("Nadando   :)")
    
    def presentar_pez(self):
        print(f"Este es un {self.nombre}.")
        print(f"Su nombre cientifico es {self.nombre_cientifico}")
        print(f"Su peso es de {self.peso} kg.")
        print(f"Se tamaño es de {self.tamaño} m.")
        print(f"Viven en hábitads como {self.habitad}")
        print(f"Este pez se encuentra en disperso en {self.lugares_de_origen}")
        print(f"Su velocidad es de {self.velocidad} km/hrs")
        print(f"Este pez se aliemnta de {self.alimento}")
        print(f"Su estado en la cadena alimenticia es {self.estado_en_la_cadena_alimenticia}")
        print(f"Su tipo de cuerpo es {self.tipo_de_cuerpo}")
        
datos_pez_espada = Pez_espada("Pez Espada", "Xiphias gladius", 4.5, 500, "En aguas tropicales, subtropicales y templadas", "El Norte de Hawái, Pacífico Norte y Sur (Perú y Chile), costas orientales de EEUU, México y al este de Japón", "Atún, barracuda, Pez volador, verdel, calamares, etc.", "Oseo", "En la cima de la cadena alimenticia, es decir, que es un super depredador, sin embargo, este pez tiene algunos depredadores que lo acechan, dichos depredadores son las Orcas y El marrajo dientuso(un tipo de Tiburón).", 100, ruta_imagen="pez_espada.png")
datos_pez_espada.mostrar_imagen()
datos_pez_espada.nadar()
datos_pez_espada.presentar_pez()

class Pez_Koi(Pez):
    def __init__(self, nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, variedad, domesticar, resistencia, ruta_imagen=None):
        super().__init__(nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, ruta_imagen)
        self.variedad = variedad
        self.domesticar = domesticar
        self.resistencia = resistencia
        
    
    def nadar(self): #Metodo
        print("Pez koi nadando :) 🐟")

    def presentar_pez(self):
        print(f"Este es un {self.nombre}.")
        print(f"Su nombre cientifico es {self.nombre_cientifico}")
        print(f"Su peso es de {self.peso}")
        print(f"Se tamaño es de {self.tamaño}")
        print(f"Viven en hábitads {self.habitad}")
        print(f"Este pez se encuentra en disperso en {self.lugares_de_origen}")
        print(f"Este pez tiene {self.variedad}")
        print(f"Este pez se puede {self.domesticar}")
        print(f"Este pez tiene {self.resistencia}")
        print(f"Este pez se aliemnta de {self.alimento}")
        print(f"Su estado en la cadena alimenticia es {self.estado_en_la_cadena_alimenticia}")
        print(f"Su tipo de cuerpo es {self.tipo_de_cuerpo}")

datos_pez_koi = Pez_Koi("Pez Koi o Carpas Koi", "Cyprinus carpio", "80 cm o más", "10 kilos o más", "arenosos o con fango", "Asia Central(especificamente en las cuencas de los mares Negro, Caspio y Aral, dicho lugares corresponde el lugar de origen de este Pez), Japón, China(En Japón y China se domesticaron), también se peuden encontrar en los parques, estanques y criaderos al rededor del mundo", "pellets o sticks, Larvas de mosquito, gusanos de sangre, camarones pequeños, Vegetales,etc", "óseo", "nivel de consumidor primario y secundario", "más de 100 variedades, las cuales se clasifican a partir de los aptrones de colores, tipo de escamas y origen, sus clasificaciones son las siguientes: Gosanke, Utsurimono, Tarcho, Asagi, Ochiba, etc", "domesticar", "Una gran resistencia, tiene una adaptabilidad térmica que los permite tolerar fríos inviernos, además, tiene una gran resistencia a las enfermedades y cuenta con una dieta omnívora, al cual le permite comer plantas, algas, insectos y crustáceos", ruta_imagen= "Pez_koi.PNG")
datos_pez_koi.mostrar_imagen()
datos_pez_koi.nadar()
datos_pez_koi.presentar_pez()

class salmon_rojo(Pez):
    def __init__(self, nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, fuerza, ruta_imagen=None):
        super().__init__(nombre, nombre_cientifico, tamaño, peso, habitad, lugares_de_origen, alimento, tipo_de_cuerpo, estado_en_la_cadena_alimenticia, ruta_imagen)
        self.fuerza = fuerza
    
    def nadar(self):
        print("Nadando   :)")
    
    def presentar_pez(self):
        print(f"Este es un {self.nombre}.")
        print(f"Su nombre cientifico es {self.nombre_cientifico}")
        print(f"Su peso es de {self.peso} kg.")
        print(f"Se tamaño es de {self.tamaño} cm.")
        print(f"Viven en hábitads como {self.habitad}")
        print(f"Este pez se encuentra en disperso en {self.lugares_de_origen}")
        print(f"Su velocidad es de {self.fuerza}")
        print(f"Este pez se aliemnta de {self.alimento}")
        print(f"Su estado en la cadena alimenticia es {self.estado_en_la_cadena_alimenticia}")
        print(f"Su tipo de cuerpo es {self.tipo_de_cuerpo}")
        
datos_salmon_rojo = salmon_rojo("Pez Salmón rojo", "Oncorhynchus nerka", "45-84", "1.8-7", "En aguas frías del océano Pácífico Norte y ríos de agua dulce", "En Norteamerica(Alaka,Canadá y en el estado de California),Asia(Japón) y Europa(Rusia)","zooplancton, krill, insectos y larvas","óseo", " es un consumidor secundario y terciario (carnívoro)", " Su musculatura está adaptada para nadar contracorriente. Pueden realizar saltos de hasta 3,7 metros de altura para superar cascadas o rápidos durante su migración.", ruta_imagen= "Salmon_rojo.PNG") 
datos_salmon_rojo.mostrar_imagen()
datos_salmon_rojo.nadar()
datos_salmon_rojo.presentar_pez()
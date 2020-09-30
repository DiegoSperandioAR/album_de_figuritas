import random


random.random()
#random.random() devuelve un número random entre el o y 1
#print(random.random())

random.randint(1, 10)
#print(random.randint(1, 10)) devuelve un número entre los 2 elegidos
#print(random.randint(1, 10))
    

#funcion de comprar figus
def comprar_una_figu(figus_total):
  figu = random.randint(0, figus_total - 1)
  #retorna un número random entre 0 y figus_total
  return figu

 #Vamos a recorrer el album
def album_esta_completo(album):
  i = 0
  while i < len(album):
   #Si encontramos que en alguna posición hay un cero, no hemos completado el album
    if album[i] == 0:
      return False
    #sumamos al contador (i) para que momentáneamente finalice el while
    i += 1
  #Si NO encontramos ningún cero, Sí hemos completado el album
  return True

def album_completo(album):
  i = 0
  while i < len(album):
    if album[i] == 0:
      return False
  return True

#El contador de las figus que hemos comprado
def cuantas_figus(figus_total):
  #Creando una album de 669 posiciones con 0 (álbum vacío)
  #Los 0 representan que no tenemos esa figura
  #Los 1 representan que sí tenemos esa figura
  album = []
  i = 0
  while i < figus_total:
    album.append(0)
    i += 1
  #contador de figuras compradas
  cantidad_figus = 0
  #Album completo
  album_completo = False
  #Mientras el album no esté completo...
  while not album_completo:
    #Compramos una figura
    numero_de_figurita = comprar_una_figu(figus_total)
    #Aumentamos una figurita
    cantidad_figus += 1
    #Pegamos la figura en el album
    album[numero_de_figurita] = 1
    #Usando la función "album_esta_completo" verificamos si está completo
    album_completo = album_esta_completo(album)
  
  return cantidad_figus

#print(cuantas_figus(669))


#función para repetir 1000 veces el proceso de cuantas_figus
def promedio_de_figus(n_repeticiones, album_total):
  #El contador
  cantidad = 0
  #Ésta es la lista donde se guardaran las repeticiones de "cuantas_figus" antes de sumarlo
  lista_suma = []
  #El while se usa para repetir la función "cuántas_figus" mientras sea menor que "n_repeticiones"
  while cantidad < n_repeticiones:
    #Variable para guardar el resultado de la función cuantas_figus en una lista
    figus = cuantas_figus(album_total)
    lista_suma.append(figus)
    cantidad += 1
    #La lista_promedio es la suma de todos los resultados de "cuantas_figus" guardados
    # en la lista "lista_suma"
  lista_promedio = sum(lista_suma)
    #OPCIÓN 3: la lista_promedio (toda la suma) entre el número de repeticiones (n_repeticiones)
  promedio = lista_promedio / n_repeticiones
  #Promedio es la variable para guardar el promedio de cuántas figuritas hay que comprar para 
  #completar el álbum, diviendo el total de figuritas compradas en todas las repeticiones entre las 
  #que se necesitan para llenar el álbum
  return promedio

#print(promedio_de_figus(1000, 6))

#Generador de paquete de 5 figuritas
def generar_paquete(figus_total, figus_paquete):
  i = 0
  paquete = []
  while i < figus_paquete:
    figu = random.randint(0, figus_total - 1)
    paquete.append(figu)
    i += 1
  return paquete
#print(generar_paquete(669, 5))

def cuantos_paquetes(figus_total, figus_paquete):
  contador = 0
  album = []
  while contador < figus_total:
    album.append(0)
    contador += 1
  cantidad_paquetes = 0
  album_completo = False
  while not album_completo:
    figu_del_paquete = 0
    paquete = generar_paquete(figus_total, figus_paquete)
    while figu_del_paquete < len(paquete):
      figu = paquete[figu_del_paquete]
      album[figu] = 1
      figu_del_paquete += 1
    cantidad_paquetes += 1
    album_completo = album_esta_completo(album)
  return cantidad_paquetes
print(cuantos_paquetes(669, 5))

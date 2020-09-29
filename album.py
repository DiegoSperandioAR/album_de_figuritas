import random


random.random()
#random.random() devuelve un número random entre el o y 1
print(random.random())

random.randint(1, 10)
#print(random.randint(1, 10)) devuelve un número entre los 2 elegidos
print(random.randint(1, 10))
    

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

print(cuantas_figus(669))

  
#Tuplas
mi_tupla =(2,4)
print ("Mi tupla:", mi_tupla)

#Lista
mi_lista = [1, 3.1416, "Gloria", mi_tupla]
print("El primer elemento de mi lista:", mi_lista[0])
print("El cuarto elemento de mi lista:", mi_lista[3])
print("El Tercer elemento de mi lista:", mi_lista[2])
      
#Diccionario
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "Gloria",
    "pi": 3.1416,
    "Tel": "664 749 9649"
}
print("Llave para accesar a mi diccionario mi_lista:", mi_diccionario["mi_lista"])
print("Llave para accesar a mi diccionario pi:", mi_diccionario["pi"])
print("Llave para accesar a mi diccionario Tel:", mi_diccionario["Tel"])
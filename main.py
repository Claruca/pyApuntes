# +++++++++ Lista +++++++++
coches = ["Subaru", "Ford", "Ka", "Mazda", "Peugeot"]

coches.remove("Subaru")
coches.append("Fiat")
coches.remove(coches[3])
print(coches.index("Ford"))
print(len(coches))

for coche in coches:
    print(coche)
for coche in range(len(coches)):
    print("Num " + str(coche), " Marca: " + coches[coche])

numeros = []
for i in range(10):
    numeros.append(i)
print(numeros)
print(numeros[0:10])     # imprime toda la lista
print(numeros[3:8])      # desde el 3 hasta el 7
print(numeros[0:10:2])   # imprime la lista de dos en dos
print(numeros[::-1])     # al revés
print(numeros[8:2:-2])   # contando hacia atrás de dos en dos
numeros.reverse()        # gira la lista y lo guarda
print(numeros)


#palabra como cadena caracteres
fruta = "banana"
for x in fruta:         #imprime caracter a caracter como una array
    print(x)


#++++++ Diccionario +++++++++

dic = {
    "Marco": "Polo",
    "Sindria": "Melo",
    7: "CR7",
    "Indiana": 18
}

print(dic)                                #Tot el dic
print(dic["Sindria"])                     #imprime value de la key
print(dic.items())                        #todos los items como clave:valor
print(dic.keys())                         #solo keys
print(dic.values())                       #solo values

print(len(dic))                           #Tamaño
print(dic.get("Indiana"))
print(dic.get(7,"No encontrado"))           #imprime value con key, si no existe, imprime No encontrado
print(dic.get("Caca","No encontrado"))
print("Marco" in dic)                       #True
print("Caca" not in dic)                    #True

#bucle que recorre diccionario, con dos maneras distintas de print
for key,value in dic.items():
    print("La clave es " + str(key) + " y el valor es: " + str(value))
    print(f'La clave es {key} y el valor es {value}')


#++++++ Tuplas +++++++++
# igual que listas pero no modificables

food = ("spam", "eggs", "sausages")
print(food[2])        #imprime por índice

# Lista con varias tuplas
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

c = 'Amy'
for i in contacts:
    if c in i:
        print(f'{str(i[0])} is {str(i[1])}')
        break
else: print("Not found")







from Persona import *

#
# def saludo(nombre):
#     print(f'Hola {nombre}')
#
# print(saludo("YO"))
# name = input("Nombre: ")
# names = "Clara"
# def saluda(n):
#     print("Hola " + n)
#
#
# print(f'El nombre {name} es ese y el otro es {names}')
# saluda(name)




# Juan = Persona("Juan", 20)
# Clara = Persona("Clara", 30)
# Clara.anyos()
#
# print(Clara.edad)



# Practica de busqueda


# def search(text, word):
#     if word in text:
#         print("Word found")
#     else:
#         print("Word not found")
#
#
# search("Hola que tal", "Hola")






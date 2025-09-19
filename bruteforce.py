print("Daniel García")

import time
import matplotlib.pyplot as plt

def Password(combinacion, intentos, contraseña, alfabeto):
    intentos += 1
    if len(combinacion) > len(contraseña):
        return None, intentos
    if combinacion == contraseña:
        return combinacion, intentos
    for letra in alfabeto:
        resultado, intentos = Password(combinacion + letra, intentos, contraseña, alfabeto)
        if resultado:
            return resultado, intentos
    return None, intentos


alfabeto = "abcd"
longitudes = range(1, 3)
tiempos_longitud = []
intentos_por_longitud = []
encontradas = []
for i in longitudes:
    contraseña = "a" * i
    inicio = time.perf_counter()
    encontrada, intentos = Password("", 0, contraseña, alfabeto)
    fin = time.perf_counter()
    tiempos_longitud.append(fin - inicio)
    intentos_por_longitud.append(intentos)
    encontradas.append(encontrada)


print("La contraseña es: ", encontrada)
print("El número de intentos fue: ", intentos)
print("Tiempo que se tardo en buscar: ", fin - inicio)




plt.figure(figsize=(8,5))
plt.plot(list(longitudes), tiempos_longitud, marker= 'o')
plt.title("Tiempo de busqueda y Longitud de la contraseña")
plt.xlabel("Tiempo (segundos)")
plt.grid(True)
plt.show()



#Ej.1  Validador de notas con promedio
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método promedio() que retorne el promedio de notas almacenadas.
class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

calificador = Calificador()

print(calificador.cargar_notas(80, 90, 150, 70, -5))
print(calificador.promedio())



#--------------------Ejer. 2----------------------------- 
# Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; (3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.
class AnalizadorTexto:

    def __init__(self):
        # Un conjunto (set) para evitar palabras repetidas
        self.conjunto_palabras = set()
        # Una lista para guardar el orden en que van llegando
        self.lista_palabras = []

    def agregar_palabra(self, palabra):
        # Guardar en el conjunto (automáticamente descarta si ya existe)
        self.conjunto_palabras.add(palabra)
        # Guardar en la lista para mantener el orden
        self.lista_palabras.append(palabra)

    def contar_palabras(self):
        # Contar cuántos elementos hay en el conjunto de palabras únicas
        total = len(self.conjunto_palabras)
        return total

    def agregar_multiples(self, *args):
        # Recorrer cada palabra que le pasemos
        for palabra in args:
            # Reutilizar el método que ya creamos
            self.agregar_palabra(palabra)

analizador = AnalizadorTexto()

# 1. Probamos agregar_palabra
analizador.agregar_palabra("hola")
analizador.agregar_palabra("mundo")

# 2. Probamos agregar_multiples (incluyendo palabras repetidas)
analizador.agregar_multiples("hola", "python", "mundo", "código")
print("Lista completa con orden de llegada:", analizador.lista_palabras)
print("Conjunto sin duplicados:", analizador.conjunto_palabras)
print("Cantidad de palabras únicas:", analizador.contar_palabras())


#Ej. 3
#Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito() que retorne la suma de todos los precios; (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.
class CarroCompras:

    def __init__(self):
        #  Diccionario vacío para los artículos
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        # Guardar en el diccionario {nombre: precio}
        self.articulos[nombre] = precio

    def total_carrito(self):
        # Sumar todos los precios
        total = 0
        for precio in self.articulos.values():
            total = total + precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        # Buscar artículos entre el rango de precios
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)
        return resultado

mi_carrito = CarroCompras()

mi_carrito.agregar_articulo("Pan", 1.50)
mi_carrito.agregar_articulo("Leche", 2.00)
mi_carrito.agregar_articulo("Carne", 12.00)
mi_carrito.agregar_articulo("Queso", 5.00)


print("Total a pagar:", mi_carrito.total_carrito())

# Buscar artículos entre $1.00 y $6.00
en_rango = mi_carrito.articulos_por_rango(1.00, 6.00)
print("Artículos dentro del rango ($1 a $6):", en_rango)

#----------------- Ejer.4-------------------------                                                   Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}.
class InversorSecuencia:

    def __init__(self):
        pass

    def invertir_lista(self, lista):
        lista_invertida = []
        # Recorrer la lista desde el último elemento hasta el primero
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        # Procesar cada lista que se pasa en los argumentos
        for lista in listas:
            # 1. Reutilizar el método para invertir
            invertida = self.invertir_lista(lista)

            # 2. Convertir la lista original a tupla para usarla como clave
            clave_original = tuple(lista)

            # 3. Guardar en el diccionario
            resultado[clave_original] = invertida

        return resultado



inversor = InversorSecuencia()

# Prueba 1: Invertir una sola lista
l1 = [1, 2, 3, 4]
print("Lista 1 invertida:", inversor.invertir_lista(l1))

# Prueba 2: Invertir múltiples listas
l2 = ["a", "b", "c"]
l3 = [10, 20, 30]

diccionario_resultados = inversor.invertir_multiples(l1, l2, l3)
print("\nDiccionario de resultados:")
for original, invertida in diccionario_resultados.items():
print(f"Original: {original} -> Invertida: {invertida}")  

   



#Ej. 5. Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
class AnalizadorNumeros:

    def __init__(self):
        # Listas vacías para guardar los números clasificados
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        # Un número es par si al dividirlo entre 2 el residuo (%) es 0
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        # Reiniciamos las listas por si llamamos al método varias veces
        self.pares = []
        self.impares = []

        for numero in numeros:
            # Reutilizamos el método es_par para clasificar
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        # Devolvemos el diccionario con las listas resultantes
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        # Contamos cuántos elementos hay en cada lista
        cant_pares = len(self.pares)
        cant_impares = len(self.impares)

        # Retornamos ambos valores en una tupla (cant_pares, cant_impares)
        return (cant_pares, cant_impares)

analizador = AnalizadorNumeros()

# 1. Probar si un número es par
print("¿El 4 es par?:", analizador.es_par(4))
print("¿El 7 es par?:", analizador.es_par(7))

# 2. Separar varios números
resultado_diccionario = analizador.separar(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Diccionario de números separados:", resultado_diccionario)

# 3. Obtener la tupla con las cantidades
cantidades = analizador.cantidad_pares_impares()
print("Tupla de cantidades (pares, impares):", cantidades)
#Ej. 6                                                                                                   Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; (3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
class GestorTemperatura:

    def __init__(self):
        # Lista vacía para guardar todas las temperaturas
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        # Guardar una temperatura en la lista
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        # Recorrer cada temperatura enviada en *temps
        for temp in temps:
            # Reutilizar el método de registro individual
            self.registrar_temperatura(temp)

    def minima(self):
        # Si la lista está vacía, no hay mínima
        if len(self.temperaturas) == 0:
            return None

        # Opción básica con bucle para encontrar el número más pequeño
        temp_min = self.temperaturas[0]
        for temp in self.temperaturas:
            if temp < temp_min:
                temp_min = temp

        return temp_min

    def maxima(self):
        # Si la lista está vacía, no hay máxima
        if len(self.temperaturas) == 0:
            return None

        # Opción básica con bucle para encontrar el número más grande
        temp_max = self.temperaturas[0]
        for temp in self.temperaturas:
            if temp > temp_max:
                temp_max = temp

        return temp_max

    def promedio(self):
        # Si la lista está vacía, el promedio es 0
        if len(self.temperaturas) == 0:
            return 0.0

        # Sumar todas las temperaturas
        suma = 0
        for temp in self.temperaturas:
            suma = suma + temp

        # Dividir la suma entre la cantidad total
        resultado = suma / len(self.temperaturas)
        return resultado

gestor = GestorTemperatura()

# 1. Registrar una por una
gestor.registrar_temperatura(18.5)
gestor.registrar_temperatura(22.0)

# 2. Registrar múltiples temperaturas de golpe
gestor.registrar_multiples(15.2, 30.1, 25.4, 19.8)

# 3. Mostrar estadísticas
print("Todas las temperaturas:", gestor.temperaturas)
print("Temperatura mínima:", gestor.minima())
print("Temperatura máxima:", gestor.maxima())
print("Temperatura promedio:", round(gestor.promedio(), 2))
#8  Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
class Equipos:
    def __init__(self):
        # Diccionario para guardar cada equipo con su lista de jugadores
        # Ejemplo: {"Barcelona": ["Messi", "Pedri"]}
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        # Crear la clave con una lista vacía si el equipo no existe
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        # Si el equipo no se ha creado aún, lo creamos primero
        if equipo not in self.equipos:
            self.crear_equipo(equipo)

        # Agregamos el jugador a la lista de ese equipo
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        # Si no hay equipos creados
        if not self.equipos:
            return None

        equipo_ganador = None
        max_jugadores = -1

        # Recorremos cada equipo y su lista de jugadores
        for equipo, lista_jugadores in self.equipos.items():
            cantidad = len(lista_jugadores)

            # Comparar si este equipo tiene más integrantes que el máximo guardado
            if cantidad > max_jugadores:
                max_jugadores = cantidad
                equipo_ganador = equipo

        return equipo_ganador

gestor = Equipos()

# 1. Crear equipos
gestor.crear_equipo("Tigres")
gestor.crear_equipo("Águilas")

# 2. Agregar jugadores
gestor.agregar_jugador("Tigres", "Carlos")
gestor.agregar_jugador("Tigres", "Ana")

gestor.agregar_jugador("Águilas", "Luis")
gestor.agregar_jugador("Águilas", "María")
gestor.agregar_jugador("Águilas", "Pedro")

# 3. Ver cuál tiene más integrantes
print("Equipos y sus listas:", gestor.equipos)
print("El equipo con más jugadores es:", gestor.equipo_mayor_integrantes())

#--------------------Ejer.9------------------------------
#Clase AnalizadorString que:                                                                          (1) tenga método solo_vocales(letra) que retorne True si es vocal;                                     (2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos;                                                           (3) tenga atributo que guarde el texto más largo analizado.

class AnalizadorString:
 def __init__(self):
   self.texto_mas largo=""
 def solo_vocales(self, letra):
  return letra.lower() in "aeiouáéíóú" #Convierte a minuscula y verifica si está en las vocales 
 def contar_por_tipo(self, texto):
   #Actualiza el texto mas largo si la nueva entrada supera la anterior 
   if len(texto) > len(self.texto_mas_largo):
      self.texto_mas_largo= texto
      # Inicializar las cajas de conteo 
   conteo={  'vocales':0,                                                                                        'consonante':0,                                                                                      'digitos':0     }
   
   for carater in texto:  
      if caracter.isdigit():
          conteo['digitos']+=1
      elif self.solo_vocales(caracter):
          conteo['vocales']+=1
       elif caracter.isalpha():
           conteo['consonante']+=1
   # Retorna el diccionario resultante 
    return conteo
astr=AnalizadorString()
resultado=astr.contar_por_tipo("Hola123")
print(resultado)

#--------------------Ejer.10------------------------------
#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.
class Tareas:
    def __init__(self):
        # Lista principal donde guardaremos las tuplas (descripcion, prioridad)
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        # Guardamos los dos valores agrupados en una tupla
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        # Retorna solo las tuplas cuya prioridad sea "alta"
        return [tarea for tarea in self.lista_tareas if tarea[1] == "alta"]

    def eliminar_completada(self, descripcion):
        # Conserva las tareas que NO coincidan con la descripción eliminada
        self.lista_tareas = [tarea for tarea in self.lista_tareas if tarea[0] != descripcion]

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")

print(t.tareas_prioritarias())  # Salida: [('Estudiar', 'alta')]


#--------------------Ejer.11------------------------------
#Clase ContadorFrecuencia que:                                                                                                  (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones;        (2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia;                  (3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.

class ContadorFrecuencia:

    def __init__(self):
        # Creamos un diccionario vacío para guardar los elementos y sus conteos
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        # Si el elemento ya está en el diccionario, le sumamos 1 a su contador
        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        # Si es la primera vez que aparece, lo guardamos con valor 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        # Si no hay elementos en el diccionario, devolvemos None
        if len(self.frecuencias) == 0:
            return None

        # Variables para ir comparando cuál es el mayor
        mas_frecuente = None
        max_conteo = 0

        # Recorremos cada elemento y su cantidad en el diccionario
        for elemento, cantidad in self.frecuencias.items():
            if cantidad > max_conteo:
                max_conteo = cantidad
                mas_frecuente = elemento

        return mas_frecuente

    def frecuencia_elemento(self, elemento):
        # Si el elemento está en el diccionario, devolvemos su conteo
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        # Si nunca se agregó, devolvemos 0
        else:
            return 0                                                                                            
contador = ContadorFrecuencia()
# (1) Agregar elementos
contador.agregar_elemento("manzana")
contador.agregar_elemento("pera")
contador.agregar_elemento("manzana")
contador.agregar_elemento("manzana")
contador.agregar_elemento("uva")

# (2) Ver el elemento más frecuente
print("Elemento más frecuente:", contador.elemento_mas_frecuente())
# Output: Elemento más frecuente: manzana

# (3) Ver la frecuencia de un elemento específico
print("Frecuencia de manzana:", contador.frecuencia_elemento("manzana"))
# Output: Frecuencia de manzana: 3

print("Frecuencia de pera:", contador.frecuencia_elemento("pera"))
# Output: Frecuencia de pera: 1

print("Frecuencia de sandía:", contador.frecuencia_elemento("sandía"))
# Output: Frecuencia de sandía: 0


#--------------------Ejer.12------------------------------
#Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.
class SelectorRango:

    def crear_rango(self, inicio, fin):
        # Creamos una lista vacía para guardar los números del rango
        numeros = []

        # Usamos fin + 1 para incluir el número 'fin' (ej: de 1 a 3 inclusive)
        for num in range(inicio, fin + 1):
            numeros.append(num)

        # Convertimos la lista a tupla y la retornamos
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        # Creamos un conjunto (set) vacío para no permitir duplicados
        elementos_unicos = set()

        # Recorremos cada tupla (inicio, fin) pasada en *rangos
        for r in rangos:
            inicio = r[0]
            fin = r[1]

            # Reutilizamos el método crear_rango para obtener los números de esta tupla
            tupla_numeros = self.crear_rango(inicio, fin)

            # Agregamos los números al conjunto (los duplicados se ignoran automáticamente)
            for num in tupla_numeros:
                elementos_unicos.add(num)

        # Convertimos el conjunto a lista para entregar el resultado final
        return list(elementos_unicos)
# Crear la instancia
sr = SelectorRango()

# (1) Probar el método crear_rango
print(sr.crear_rango(1, 3))
# Output: (1, 2, 3)

# (2) Probar el método con múltiples rangos
resultado = sr.elementos_en_multiples_rangos((1, 3), (2, 4))
print(resultado)
# Output: [1, 2, 3, 4]

#--------------------Ejer.13------------------------------
#Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        # Buscamos el tamaño de la lista más larga para no quedarnos cortos en el bucle
        max_longitud = max(len(lista1), len(lista2))

        # Recorremos posición por posición
        for i in range(max_longitud):
            # Si la posición existe en la primera lista, la agregamos
            if i < len(lista1):
                resultado.append(lista1[i])
            # Si la posición existe en la segunda lista, la agregamos
            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        # Si no pasan ninguna lista, devolvemos una lista vacía
        if not listas:
            return []

        # Comenzamos tomando la primera lista como base
        resultado = listas[0]

        # Reutilizamos el método intercalar() para ir uniendo el resto de las listas
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)

        return resultado

cl = CombinadorListas()

# (1) Probar con dos listas (ejemplo de la imagen)
print(cl.intercalar([1, 2], [3, 4]))
# Output: [1, 3, 2, 4]

# (2) Probar con múltiples listas
print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
# Output: [1, 5, 3, 6, 2, 4]


#--------------------Ejer.14------------------------------
#Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.

class RegistroNotas:

    def __init__(self):
        # Creamos un diccionario vacío para guardar estudiante: nota
        self.notas = {}

    def registrar(self, estudiante, nota):
        # Guardamos al estudiante como clave y su nota como valor
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        # Lista vacía para ir guardando los nombres de los aprobados
        aprobados = []

        # Recorremos el diccionario obteniendo (estudiante, nota)
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        # Si no hay estudiantes registrados, devolvemos None
        if not self.notas:
            return None

        # Variables para llevar el control del mejor alumno y su nota
        mejor_nombre = None
        mejor_nota = -1

        # Recorremos cada pareja estudiante-nota para buscar la calificación mayor
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        # Retornamos una tupla con (nombre, nota)
        return (mejor_nombre, mejor_nota)

rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)
print(rn.mejor_estudiante())

# Probar estudiantes_aprobados() con nota mínima de 80
print(rn.estudiantes_aprobados(80))#  ['Ana', 'Carlos']

#--------------------Ejer.15------------------------------

#Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; (2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; (3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []
        # Probamos todos los números desde 1 hasta el número mismo
        for i in range(1, numero + 1):
            # Si el residuo es 0, significa que i divide exactamente al número
            if numero % i == 0:
                divisores.append(i)

        # Convertimos la lista resultante a tupla
        return tuple(divisores)

    def es_perfecto(self, numero):
        # Reutilizamos el método para obtener los divisores del número
        divisores = self.encontrar_divisores(numero)

        # Excluimos el propio número (el último elemento de la tupla)
        divisores_propios = divisores[:-1]

        # Sumamos todos los divisores propios y comparamos con el número original
        return sum(divisores_propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        # Recorremos cada número recibido en los parámetros
        for num in numeros:
            # Asociamos el número con su tupla de divisores en el diccionario
            resultado[num] = self.encontrar_divisores(num)

        return resultado
df = DivisorFinder()

# (1) Probar encontrar_divisores() con el valor del ejercicio
print(df.encontrar_divisores(12))
# Output: (1, 2, 3, 4, 6, 12)

# (2) Probar es_perfecto() (6 es número perfecto: 1 + 2 + 3 = 6)
print(df.es_perfecto(6))
# Output: True

print(df.es_perfecto(12))
# Output: False

# (3) Probar encontrar_multiples_divisores()
print(df.encontrar_multiples_divisores(6, 12))

#--------------------Ejer.16------------------------------
#Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); (2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; (3) tenga un diccionario como atributo para historial de codificaciones.


class CodificadorCesar:

    def __init__(self):
        # Diccionario para guardar el historial de codificaciones {"palabra_original": "palabra_codificada"}
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        # Si es una letra minúscula
        if "a" <= letra <= "z":
            # Convertimos a posición 0-25, aplicamos desplazamiento con %, y volvemos a ASCII
            codigo_base = ord("a")
            posicion = ord(letra) - codigo_base
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(codigo_base + nueva_posicion)

        # Si es una letra mayúscula
        elif "A" <= letra <= "Z":
            codigo_base = ord("A")
            posicion = ord(letra) - codigo_base
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(codigo_base + nueva_posicion)

        # Si no es una letra (espacios, números, símbolos), se deja igual
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = ""

        # Recorremos cada letra y reutilizamos codificar_letra
        for letra in palabra:
            palabra_codificada += self.codificar_letra(letra, desplazamiento)

        # Guardamos en el historial
        self.historial[palabra] = palabra_codificada

        return palabra_codificada

cc = CodificadorCesar()

# (1) Codificar la palabra "hola" con desplazamiento de 3
resultado = cc.codificar_palabra("hola", 3)
print(resultado)
# Output: "krod"  ('h'->'k', 'o'->'r', 'l'->'o', 'a'->'d')
print(cc.historial)

#--------------------Ejer.17------------------------------
#Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; (3) tenga método edad_promedio_categoria(categoria).

class AgrupadorEdades:

    def __init__(self):
        # Inicializamos el diccionario con las categorías requeridas y sus listas vacías
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        # Clasificamos según los rangos típicos de edad
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        # Recorremos cada edad recibida en *edades
        for edad in edades:
            # Obtenemos la categoría reutilizando clasificar_edad
            categoria = self.clasificar_edad(edad)
            # Agregamos la edad a la lista de su respectiva categoría
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        # Verificamos si la categoría existe y si tiene edades registradas
        if categoria in self.grupos and len(self.grupos[categoria]) > 0:
            lista_edades = self.grupos[categoria]
            return sum(lista_edades) / len(lista_edades)
        
        # Si no hay edades registradas en esa categoría
        return 0.0


ae = AgrupadorEdades()

# (1) Agrupar por categoría
resultado = ae.agrupar_por_categoria(5, 15, 30, 70)
print(resultado)
# Output: {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# (2) Probar clasificar_edad
print(ae.clasificar_edad(10))
# Output: 'niño'

# (3) Probar edad_promedio_categoria
print(ae.edad_promedio_categoria("adulto"))
# Output: 30.0


#--------------------Ejer.18------------------------------
#Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; (2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; (3) tenga un atributo lista para guardar todas las distancias calculadas.

class CalculadorDistancia:

    def __init__(self):
        # Creamos una lista vacía para guardar todas las distancias
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        # Desempaquetamos las coordenadas x e y de cada punto
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        # Aplicamos la fórmula: raíz de ((x2 - x1)^2 + (y2 - y1)^2)
        # Elevar a 0.5 es lo mismo que sacar raíz cuadrada
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        # Guardamos la distancia en nuestra lista historial
        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        # Si no nos dan puntos, devolvemos None
        if len(puntos) == 0:
            return None

        # Tomamos el primer punto como el más cercano por defecto
        punto_mas_cercano = puntos[0]
        distancia_minima = self.distancia_euclidiana(referencia, puntos[0])

        # Recorremos el resto de los puntos para comparar
        for p in puntos:
            distancia_actual = self.distancia_euclidiana(referencia, p)

            # Si encontramos una distancia más pequeña, actualizamos
            if distancia_actual < distancia_minima:
                distancia_minima = distancia_actual
                punto_mas_cercano = p

        return punto_mas_cercano

cd = CalculadorDistancia()

# (1) Probar distancia_euclidiana 
print(cd.distancia_euclidiana((0, 0), (3, 4)))
# Output: 5.0

# (2) Probar punto_mas_cercano
punto_ref = (0, 0)
print(cd.punto_mas_cercano(punto_ref, (5, 5), (1, 1), (3, 4)))
# Output: (1, 1)
print(cd.distancias)

#--------------------Ejer.19------------------------------
#Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
class Inventario:

    def __init__(self):
        # Creamos un diccionario vacío para guardar producto: cantidad
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        # Si el producto ya existe en el diccionario, le sumamos la cantidad
        if producto in self.productos:
            self.productos[producto] = self.productos[producto] + cantidad
        # Si es un producto nuevo, lo creamos con esa cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        # Primero verificamos si el producto existe y si hay suficiente stock
        if producto in self.productos and self.productos[producto] >= cantidad:
            # Restamos la cantidad del inventario
            self.productos[producto] = self.productos[producto] - cantidad
            return True
        else:
            # Si no existe o no alcanza el stock, no restamos y devolvemos False
            return False

    def productos_bajo_stock(self, minimo):
        # Lista vacía para ir agregando los nombres de los productos bajos en stock
        bajos = []

        # Recorremos cada producto y su cantidad almacenada
        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                bajos.append(producto)

        return bajos

inv = Inventario()

inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))


# 4. Consultar productos con stock menor a 15
# Como quedan 20 panes, no entra en la lista aún
print(inv.productos_bajo_stock(15))

# 5. Restar 10 panes más (20 - 10 = 10)
inv.restar_stock("pan", 10)

# Ahora quedan 10 panes, lo cual es menor a 15 
print(inv.productos_bajo_stock(15))


#--------------------Ejer.20------------------------------
#Clase AnalizadorPatrones que:                                                                        (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista;                                                                                   (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]};        (3) tenga método palabras_unicas() usando un conjunto.

class AnalizadorPatrones:

    def __init__(self):
        # Inicializa la lista para el historial de palabras
        self.historial_palabras = []

    def encontrar_palabras(self, texto, patron):
        # Separa el texto en palabras
        palabras = texto.split()
        coincidencias = []

        for palabra in palabras:
            # Guarda la palabra en el historial
            self.historial_palabras.append(palabra)
            # Filtra las palabras que inician con el patrón
            if palabra.startswith(patron):
                coincidencias.append(palabra)

        return coincidencias

    def agrupar_por_longitud(self, texto):
        # Separa el texto en palabras
        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            # Guarda la palabra en el historial
            self.historial_palabras.append(palabra)
            # Obtiene la longitud de la palabra
            longitud = len(palabra)

            # Crea la lista para la longitud si no existe
            if longitud not in grupos:
                grupos[longitud] = []

            # Agrupa la palabra por su longitud
            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        # Convierte el historial a un conjunto para obtener palabras únicas
        return set(self.historial_palabras)


# Instancia de la clase
ap = AnalizadorPatrones()

# Probamos el método encontrar_palabras()
resultado_palabras = ap.encontrar_palabras("el gato está en la casa", "ca")
print(resultado_palabras)
# Salida: ['casa']

# Probamos el método agrupar_por_longitud()
resultado_agrupado = ap.agrupar_por_longitud("el gato está aquí")
print(resultado_agrupado)
# Salida: {2: ['el'], 4: ['gato'], 4: ['está'], 4: ['aquí']}

# Probamos el método palabras_unicas()
resultado_unicas = ap.palabras_unicas()
print(resultado_unicas)


#----------------Practica 21-----------------------------
#  Ejercicio de ejemplo del ejercicio #1

#Crea una clase llamada RegistroTemperaturas que:

#Tenga un método validar_temperatura(temperatura) que retorne True si la temperatura está entre -50 y 60 grados, y False en caso contrario.
#Tenga un método cargar_temperaturas(*args) que reciba múltiples temperaturas, valide cada una y agregue únicamente las válidas a una lista interna.

#Tenga un método promedio() que retorne el promedio de las temperaturas almacenadas.
class RegistroTemperaturas:

    def __init__(self):
        self.temperaturas = []

    def validar_temperatura(self, temperatura):
        return -50 <= temperatura <= 60

    def cargar_temperaturas(self, *args):
        for temperatura in args:
            if self.validar_temperatura(temperatura):
                self.temperaturas.append(temperatura)

        return self.temperaturas

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


# Crear el objeto
registro = RegistroTemperaturas()

# Cargar temperaturas
print(registro.cargar_temperaturas(20, 25, 100, -10, 30, -80))

# Calcular promedio
print(registro.promedio())

#----------------Practica 22-----------------------------
#  Ejercicio de ejemplo del ejercicio #2


#Crea una clase llamada RegistroProductos que:

#Tenga un método agregar_producto(producto) que agregue el producto a un conjunto para evitar productos duplicados y también a una lista para conservar el orden en que fueron agregados.

#Tenga un método contar_productos() que retorne la cantidad de productos únicos registrados.

#Tenga un método agregar_multiples(*args) que permita agregar varios productos y que reutilice el método agregar_producto().
class RegistroProductos:

    def __init__(self):
        self.productos = set()
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.productos.add(producto)
        self.lista_productos.append(producto)

    def contar_productos(self):
        return len(self.productos)

    def agregar_multiples(self, *args):
        for producto in args:
            self.agregar_producto(producto)


# Crear el objeto
registro = RegistroProductos()

# Agregar productos individualmente
registro.agregar_producto("Laptop")
registro.agregar_producto("Mouse")
registro.agregar_producto("Laptop")

# Mostrar conjunto
print(registro.productos)

# Mostrar lista
print(registro.lista_productos)

# Contar productos únicos
print(registro.contar_productos())

# Agregar varios productos
registro.agregar_multiples(
    "Teclado",
    "Monitor",
    "Mouse",
    "Audífonos"
)

print(registro.productos)
print(registro.lista_productos)
print(registro.contar_productos())

#----------------Practica 23-----------------------------
#Crea una clase llamada Biblioteca que cumpla con los siguientes requisitos:

#Tenga un método agregar_libro(titulo, precio) que permita agregar libros a un diccionario, utilizando el título como clave y el precio como valor.

#Tenga un método valor_total() que retorne la suma de los precios de todos los libros almacenados.

#Tenga un método libros_por_rango(precio_min, precio_max) que reciba un precio mínimo y uno máximo, y retorne una lista con los títulos de los libros cuyo precio se encuentre dentro de ese rango, incluyendo los límites.

class Biblioteca:

    def __init__(self):
        self.libros = {}

    def agregar_libro(self, titulo, precio):
        self.libros[titulo] = precio

    def valor_total(self):
        return sum(self.libros.values())

    def libros_por_rango(self, precio_min, precio_max):
        libros = []

        for titulo, precio in self.libros.items():
            if precio_min <= precio <= precio_max:
                libros.append(titulo)

        return libros


# Crear objeto
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro("Python Básico", 25)
biblioteca.agregar_libro("Java Avanzado", 40)
biblioteca.agregar_libro("HTML y CSS", 15)
biblioteca.agregar_libro("Bases de Datos", 50)

# Mostrar diccionario
print(biblioteca.libros)

# Mostrar valor total
print(biblioteca.valor_total())

# Buscar libros entre 20 y 45
print(biblioteca.libros_por_rango(20, 45))


#----------------Practica 24-----------------------------
#Crea una clase llamada ProcesadorSecuencias que:

T#enga un método invertir_secuencia(secuencia) que reciba una lista y retorne una nueva lista con los elementos en orden inverso, sin utilizar reversed(), reverse() ni slicing ([::-1]). Debes hacerlo manualmente utilizando un bucle.

#Tenga un método invertir_multiples(*secuencias) que reciba varias listas y reutilice el método invertir_secuencia() para invertir cada una.

#El método invertir_multiples() debe retornar un diccionario donde cada lista original se relacione con su lista invertida.

class ProcesadorSecuencias:

    def invertir_secuencia(self, secuencia):
        invertida = []

        for i in range(len(secuencia) - 1, -1, -1):
            invertida.append(secuencia[i])

        return invertida

    def invertir_multiples(self, *secuencias):
        resultado = {}

        for secuencia in secuencias:
            invertida = self.invertir_secuencia(secuencia)
            resultado[tuple(secuencia)] = invertida

        return resultado


# Crear objeto
procesador = ProcesadorSecuencias()

# Crear listas
lista1 = [1, 2, 3, 4]
lista2 = ["A", "B", "C"]
lista3 = [10, 20, 30]

# Invertir una lista
print(procesador.invertir_secuencia(lista1))

# Invertir varias listas
print(procesador.invertir_multiples(lista1, lista2, lista3))

#----------------Practica 25-----------------------------
#Crea una clase llamada AnalizadorEdades que:

#Tenga un método es_mayor_edad(edad) que retorne True si la edad es 18 o mayor, y False en caso contrario.

#Tenga un método separar(*edades) que reciba varias edades y retorne un diccionario

class AnalizadorEdades:

    def __init__(self):
        self.mayores = []
        self.menores = []

    def es_mayor_edad(self, edad):
        return edad >= 18

    def separar(self, *edades):
        for edad in edades:
            if self.es_mayor_edad(edad):
                self.mayores.append(edad)
            else:
                self.menores.append(edad)

        return {
            'mayores': self.mayores,
            'menores': self.menores
        }

    def cantidad_mayores_menores(self):
        return (len(self.mayores), len(self.menores))


# Crear objeto
analizador = AnalizadorEdades()

# Separar edades
print(analizador.separar(12, 18, 25, 15, 30, 10, 17, 20))

# Mostrar cantidades
print(analizador.cantidad_mayores_menores())

#----------------Practica 26-----------------------------
#Crea una clase llamada GestorCalificaciones que:
#Tenga un método registrar_calificacion(nota) que guarde la calificación en una lista.
#Tenga los métodos:
#minima() → retorne la calificación más baja.

#maxima() → retorne la calificación más alta.

#promedio() → retorne el promedio de todas las calificaciones almacenadas.

#Tenga un método registrar_multiples(*notas) que reciba varias calificaciones y reutilice registrar_calificacion() para guardar cada una.


class GestorCalificaciones:

    def __init__(self):
        self.calificaciones = []

    def registrar_calificacion(self, nota):
        self.calificaciones.append(nota)

    def minima(self):
        return min(self.calificaciones)

    def maxima(self):
        return max(self.calificaciones)

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_calificacion(nota)


# Crear objeto
gestor = GestorCalificaciones()

# Registrar una calificación
gestor.registrar_calificacion(80)

# Registrar varias calificaciones
gestor.registrar_multiples(95, 70, 85, 100)

# Mostrar la lista
print(gestor.calificaciones)

# Mostrar estadísticas
print("Mínima:", gestor.minima())
print("Máxima:", gestor.maxima())
print("Promedio:", gestor.promedio())

#----------------Practica 27----------------------------

#Crea una clase llamada GestorEmpleados que:

#Tenga un método agregar_empleado(nombre, salario) que guarde los empleados en un diccionario, utilizando el nombre como clave y el salario como valor.

#Tenga un método empleados_por_salario(salario_minimo) que retorne una lista con los nombres de los empleados cuyo salario sea mayor o igual al salario mínimo indicado.

#Tenga un método salario_promedio() que retorne el promedio de los salarios de todos los empleados almacenados.

class GestorEmpleados:

    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, nombre, salario):
        self.empleados[nombre] = salario

    def empleados_por_salario(self, salario_minimo):
        resultado = []

        for nombre, salario in self.empleados.items():
            if salario >= salario_minimo:
                resultado.append(nombre)

        return resultado

    def salario_promedio(self):
        return sum(self.empleados.values()) / len(self.empleados)


# Crear objeto
gestor = GestorEmpleados()

# Agregar empleados
gestor.agregar_empleado("Carlos", 800)
gestor.agregar_empleado("Ana", 1200)
gestor.agregar_empleado("Pedro", 950)
gestor.agregar_empleado("Maria", 1500)

# Mostrar empleados
print(gestor.empleados)

# Buscar empleados con salario >= 1000
print(gestor.empleados_por_salario(1000))

# Mostrar salario promedio
print(gestor.salario_promedio())


#----------------Practica 28----------------------------

#Crea una clase llamada Cursos que:
#Tenga un método crear_curso(nombre_curso) que cree un curso como una lista vacía dentro de un diccionario.
#Tenga un método agregar_estudiante(curso, estudiante) que añada el estudiante a la lista correspondiente al curso.
#Tenga un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga más estudiantes.

class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        mayor = None
        cantidad_mayor = 0

        for curso, estudiantes in self.cursos.items():
            if len(estudiantes) > cantidad_mayor:
                cantidad_mayor = len(estudiantes)
                mayor = curso

        return mayor


# Crear objeto
cursos = Cursos()

# Crear cursos
cursos.crear_curso("Python")
cursos.crear_curso("Java")
cursos.crear_curso("HTML")

# Agregar estudiantes
cursos.agregar_estudiante("Python", "Ana")
cursos.agregar_estudiante("Python", "Carlos")
cursos.agregar_estudiante("Python", "Pedro")

cursos.agregar_estudiante("Java", "Luis")
cursos.agregar_estudiante("Java", "Maria")

cursos.agregar_estudiante("HTML", "Sofia")

# Mostrar cursos
print(cursos.cursos)

# Mostrar curso con más estudiantes
print(cursos.curso_mayor_estudiantes())


#----------------Practica 29----------------------------
#Crea una clase llamada AnalizadorString que cumpla con los siguientes requisitos:

T#enga un método solo_vocales(letra) que retorne True si el carácter recibido es una vocal (a, e, i, o, u) y False en caso contrario.

#Tenga un método contar_por_tipo(texto) que recorra el texto y retorne un diccionario con la cantidad de:
#vocales
#consonantes
#dígitos
#El método debe reutilizar solo_vocales() para identificar las vocales.
#Tenga un atributo llamado texto_mas_largo que almacene el texto más largo que haya sido analizado mediante contar_por_tipo().

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:

            if letra.isdigit():
                digitos += 1

            elif letra.isalpha():

                if self.solo_vocales(letra):
                    vocales += 1
                else:
                    consonantes += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }


# Crear objeto
analizador = AnalizadorString()

# Analizar textos
print(analizador.contar_por_tipo("Hola123"))

print(analizador.contar_por_tipo("Programacion2025"))

print(analizador.contar_por_tipo("Python"))

# Mostrar el texto más largo
print("Texto más largo:", analizador.texto_mas_largo)

#----------------Practica 30----------------------------

#Crea una clase llamada Tareas que cumpla con los siguientes requisitos:
#Tenga un método agregar_tarea(descripcion, prioridad) que agregue una tarea a una lista como una tupla con la estructura:
#(descripcion, prioridad)
#Tenga un método tareas_prioritarias() que recorra la lista y retorne únicamente las tareas cuya prioridad sea "alta".
#Tenga un método eliminar_completada(descripcion) que busque una tarea por su descripción y la elimine de la lista.
class Tareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.lista_tareas.append(tarea)

    def tareas_prioritarias(self):
        prioritarias = []

        for tarea in self.lista_tareas:
            if tarea[1].lower() == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tareas:
            if tarea[0] == descripcion:
                self.lista_tareas.remove(tarea)
                break


# Crear objeto
tareas = Tareas()

# Agregar tareas
tareas.agregar_tarea("Estudiar Python", "alta")
tareas.agregar_tarea("Hacer ejercicio", "baja")
tareas.agregar_tarea("Entregar proyecto", "alta")
tareas.agregar_tarea("Ordenar habitación", "media")

# Mostrar todas las tareas
print("Todas:", tareas.lista_tareas)

# Mostrar tareas prioritarias
print("Prioritarias:", tareas.tareas_prioritarias())

# Eliminar una tarea
tareas.eliminar_completada("Hacer ejercicio")

# Mostrar tareas después de eliminar
print("Después de eliminar:", tareas.lista_tareas)


#----------------Practica 31----------------------------
#Crea una clase llamada ContadorFrecuencia que cumpla con los siguientes requisitos:
#Tenga un método agregar_elemento(elemento) que guarde elementos en un diccionario y aumente su contador cada vez que el mismo elemento sea agregado.
#Tenga un método elemento_mas_frecuente() que recorra el diccionario y retorne el elemento que tenga la mayor frecuencia.
#Tenga un método frecuencia_elemento(elemento) que reciba un elemento y retorne cuántas veces ha sido agregado.

class ContadorFrecuencia:

    def __init__(self):
        self.elementos = {}

    def agregar_elemento(self, elemento):
        if elemento in self.elementos:
            self.elementos[elemento] += 1
        else:
            self.elementos[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = None
        frecuencia_mayor = 0

        for elemento, frecuencia in self.elementos.items():
            if frecuencia > frecuencia_mayor:
                frecuencia_mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        return self.elementos.get(elemento, 0)


# Crear objeto
contador = ContadorFrecuencia()

# Agregar elementos
contador.agregar_elemento("Python")
contador.agregar_elemento("Java")
contador.agregar_elemento("Python")
contador.agregar_elemento("C++")
contador.agregar_elemento("Python")
contador.agregar_elemento("Java")

# Mostrar diccionario
print(contador.elementos)

# Consultar frecuencia
print("Frecuencia de Python:", contador.frecuencia_elemento("Python"))

# Elemento más frecuente
print("Más frecuente:", contador.elemento_mas_frecuente())


#----------------Practica 32----------------------------
#Crea una clase llamada SelectorRango que cumpla con los siguientes requisitos:
#Tenga un método crear_rango(inicio, fin) que reciba un número inicial y uno final, y retorne una tupla con todos los números del rango, incluyendo el inicio y sin incluir el final.
#Tenga un método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas con la estructura (inicio, fin) y retorne una lista combinada con todos los números de los rangos, sin duplicados.
#Para eliminar los números repetidos debe utilizar un conjunto (set).
class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for inicio, fin in rangos:
            rango = self.crear_rango(inicio, fin)

            for numero in rango:
                elementos.add(numero)

        return list(elementos)


# Crear objeto
selector = SelectorRango()

# Crear un rango
print(selector.crear_rango(1, 5))

# Trabajar con varios rangos
resultado = selector.elementos_en_multiples_rangos(
    (1, 5),
    (3, 8),
    (10, 13)
)

print(resultado)

#----------------Practica 33----------------------------
#Crea una clase llamada MezcladorNumeros que cumpla con los siguientes requisitos:
#Tenga un método mezclar(lista1, lista2) que reciba dos listas y retorne una nueva lista alternando los elementos de ambas listas.
#Si una lista tiene más elementos que la otra, debe agregar los elementos restantes al final.
#Tenga un método mezclar_multiples(*listas) que reciba varias listas y reutilice el método mezclar() para combinarlas.
class MezcladorNumeros:

    def mezclar(self, lista1, lista2):
        resultado = []

        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def mezclar_multiples(self, *listas):
        resultado = listas[0]

        for lista in listas[1:]:
            resultado = self.mezclar(resultado, lista)

        return resultado


# Crear objeto
mezclador = MezcladorNumeros()

# Mezclar dos listas
print(mezclador.mezclar(
    [10, 20, 30],
    [1, 2, 3]
))

# Mezclar varias listas
print(mezclador.mezclar_multiples(
    [10, 20],
    [1, 2],
    [100, 200]
))


#----------------Practica 34----------------------------
#Crea una clase llamada RegistroEmpleados que cumpla con los siguientes requisitos:
#Tenga un método registrar(nombre, salario) que guarde en un diccionario el nombre del empleado como clave y su salario como valor.
#Tenga un método empleados_destacados(salario_minimo) que retorne una lista con los nombres de los empleados cuyo salario sea mayor o igual al salario mínimo indicado.
#Tenga un método empleado_mejor_pagado() que retorne una tupla con el nombre y salario del empleado que tenga el salario más alto.
class RegistroEmpleados:

    def __init__(self):
        self.empleados = {}

    def registrar(self, nombre, salario):
        self.empleados[nombre] = salario

    def empleados_destacados(self, salario_minimo):
        destacados = []

        for nombre, salario in self.empleados.items():
            if salario >= salario_minimo:
                destacados.append(nombre)

        return destacados

    def empleado_mejor_pagado(self):
        mejor_nombre = None
        mejor_salario = 0

        for nombre, salario in self.empleados.items():
            if salario > mejor_salario:
                mejor_salario = salario
                mejor_nombre = nombre

        return (mejor_nombre, mejor_salario)


# Crear objeto
registro = RegistroEmpleados()

# Registrar empleados
registro.registrar("Carlos", 800)
registro.registrar("Ana", 1200)
registro.registrar("Pedro", 950)
registro.registrar("Maria", 1500)

# Mostrar empleados
print(registro.empleados)

# Empleados con salario >= 1000
print(registro.empleados_destacados(1000))

# Empleado con mayor salario
print(registro.empleado_mejor_pagado())

#----------------Practica 35----------------------------
#Crea una clase llamada BuscadorPares que cumpla con los siguientes requisitos:
#Tenga un método es_par(numero) que retorne True si el número es par y False si es impar.
#Tenga un método buscar_pares(*numeros) que reciba varios números y retorne una lista con solamente los números pares. Debe reutilizar el método es_par().
#Tenga un método buscar_multiples(*listas) que reciba varias listas y retorne un diccionario donde cada posición indique la lista original y su lista de números pares

class BuscadorPares:

    def es_par(self, numero):
        return numero % 2 == 0

    def buscar_pares(self, *numeros):
        pares = []

        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)

        return pares

    def buscar_multiples(self, *listas):
        resultado = {}

        for i, lista in enumerate(listas, 1):
            resultado[i] = self.buscar_pares(*lista)

        return resultado


# Crear objeto
buscador = BuscadorPares()

# Comprobar si es par
print(buscador.es_par(8))

# Buscar pares
print(buscador.buscar_pares(3, 6, 8, 11, 20))

# Buscar pares en varias listas
print(buscador.buscar_multiples(
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12]
))







#----------------Practica 36----------------------------
#Crea una clase llamada TransformadorLetras que cumpla con los siguientes requisitos:
#Tenga un método cambiar_letra(letra, desplazamiento) que reciba una letra y un desplazamiento, y retorne la letra desplazada dentro del alfabeto. Debe utilizar el operador % para evitar salir del rango del alfabeto.
#Tenga un método cambiar_palabra(palabra, desplazamiento) que recorra una palabra y reutilice cambiar_letra() para transformar cada letra.
#Tenga un atributo llamado historial que sea un diccionario donde se guarden las palabras originales y sus respectivas palabras transformadas.

class TransformadorLetras:

    def __init__(self):
        self.historial = {}

    def cambiar_letra(self, letra, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        posicion = alfabeto.index(letra.lower())

        nueva_posicion = (posicion + desplazamiento) % len(alfabeto)

        return alfabeto[nueva_posicion]

    def cambiar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.cambiar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


# Crear objeto
transformador = TransformadorLetras()

# Cambiar una letra
print(transformador.cambiar_letra("a", 2))

# Cambiar una palabra
print(transformador.cambiar_palabra("hola", 2))

# Cambiar otra palabra
print(transformador.cambiar_palabra("python", 3))

# Mostrar historial
print(transformador.historial)





#----------------Practica 37----------------------------
#Crea una clase llamada AgrupadorNotas que cumpla con los siguientes requisitos:
#Tenga un método clasificar_nota(nota) que retorne una categoría según la calificación:
#"baja" → nota menor a 60
#"media" → nota entre 60 y 79
#"alta" → nota entre 80 y 100
#Tenga un método agrupar_por_categoria(*notas) que reciba varias notas y retorne un diccionario con la siguiente estructura:
#{
 #   "baja": [...],
 #   "media": [...],
 #   "alta": [...]
#}

#Debe utilizar clasificar_nota() para determinar dónde colocar cada nota.
#Tenga un método promedio_categoria(categoria) que retorne el promedio de las notas pertenecientes a la categoría indicada.

class AgrupadorNotas:

    def __init__(self):
        self.notas = {
            "baja": [],
            "media": [],
            "alta": []
        }

    def clasificar_nota(self, nota):

        if nota < 60:
            return "baja"

        elif nota < 80:
            return "media"

        else:
            return "alta"

    def agrupar_por_categoria(self, *notas):

        for nota in notas:
            categoria = self.clasificar_nota(nota)
            self.notas[categoria].append(nota)

        return self.notas

    def promedio_categoria(self, categoria):

        lista = self.notas[categoria]

        if len(lista) == 0:
            return 0

        return sum(lista) / len(lista)


# Crear objeto
agrupador = AgrupadorNotas()

# Agregar y clasificar notas
print(
    agrupador.agrupar_por_categoria(
        50, 65, 90, 75, 85, 40, 100
    )
)

# Promedios
print("Promedio baja:", agrupador.promedio_categoria("baja"))
print("Promedio media:", agrupador.promedio_categoria("media"))
print("Promedio alta:", agrupador.promedio_categoria("alta"))

#----------------Practica 38----------------------------
#Crea una clase llamada CalculadorDiferencias que cumpla con los siguientes requisitos:
#Tenga un método diferencia(p1, p2) que reciba dos números y calcule la diferencia absoluta entre ellos.
#Tenga un método valor_mas_cercano(referencia, *valores) que reciba un número de referencia y varios valores, y retorne el valor que tenga la menor diferencia con respecto a la referencia.
#Tenga un atributo llamado diferencias que sea una lista donde se guarden todas las diferencias calculadas.

class CalculadorDiferencias:

    def __init__(self):
        self.diferencias = []

    def diferencia(self, p1, p2):
        resultado = abs(p1 - p2)

        self.diferencias.append(resultado)

        return resultado

    def valor_mas_cercano(self, referencia, *valores):

        valor_cercano = None
        diferencia_menor = None

        for valor in valores:

            diferencia_actual = self.diferencia(
                referencia,
                valor
            )

            if diferencia_menor is None or diferencia_actual < diferencia_menor:
                diferencia_menor = diferencia_actual
                valor_cercano = valor

        return valor_cercano


# Crear objeto
calculador = CalculadorDiferencias()

# Calcular una diferencia
print(calculador.diferencia(10, 15))

# Buscar el valor más cercano
print(
    calculador.valor_mas_cercano(
        10,
        5,
        8,
        14,
        20
    )
)

# Mostrar todas las diferencias calculadas
print(calculador.diferencias)


#----------------Practica 39----------------------------
#Crea una clase llamada GestorCupos que cumpla con los siguientes requisitos:
#Tenga un método agregar_cupos(evento, cantidad) que guarde en un diccionario la cantidad de cupos disponibles para cada evento. Si el evento ya existe, debe sumar la nueva cantidad.

#Tenga un método reservar_cupos(evento, cantidad) que disminuya la cantidad de cupos disponibles y retorne:
#True si hay suficientes cupos.
#False si no hay suficientes cupos o el evento no existe.
#Tenga un método eventos_bajo_cupos(minimo) que retorne una lista con los nombres de los eventos cuya cantidad de cupos sea menor que el mínimo indicado.
class GestorCupos:

    def __init__(self):
        self.cupos = {}

    def agregar_cupos(self, evento, cantidad):

        if evento in self.cupos:
            self.cupos[evento] += cantidad
        else:
            self.cupos[evento] = cantidad

    def reservar_cupos(self, evento, cantidad):

        if evento in self.cupos and self.cupos[evento] >= cantidad:
            self.cupos[evento] -= cantidad
            return True

        return False

    def eventos_bajo_cupos(self, minimo):

        resultado = []

        for evento, cantidad in self.cupos.items():
            if cantidad < minimo:
                resultado.append(evento)

        return resultado


# Crear objeto
gestor = GestorCupos()

# Agregar cupos
gestor.agregar_cupos("Concierto", 100)
gestor.agregar_cupos("Conferencia", 30)
gestor.agregar_cupos("Taller", 10)

# Agregar más cupos al mismo evento
gestor.agregar_cupos("Taller", 5)

print(gestor.cupos)

# Reservar cupos
print(gestor.reservar_cupos("Concierto", 20))

# Intentar reservar más de lo disponible
print(gestor.reservar_cupos("Taller", 20))

# Eventos con pocos cupos
print(gestor.eventos_bajo_cupos(20))

#----------------Practica 40 ----------------------------
#Crea una clase llamada AnalizadorNombres que cumpla con los siguientes requisitos:
#Tenga un método buscar_por_inicio(texto, inicio) que reciba un texto y un patrón, y retorne una lista con las palabras que empiecen con ese patrón.
#Tenga un método agrupar_por_longitud(texto) que reciba un texto y retorne un diccionario donde:
#La clave sea la longitud de la palabra.
#El valor sea una lista con las palabras que tienen esa longitud.
#Ejemplo:

#{
#    3: ["Ana", "Luis"],
#    5: ["Pedro"]
#}
#Tenga un método nombres_unicos(texto) que utilice un conjunto (set) para eliminar los nombres repetidos y retorne una lista con los nombres únicos.


class AnalizadorNombres:

    def buscar_por_inicio(self, texto, inicio):
        resultado = []

        palabras = texto.split()

        for palabra in palabras:
            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}

        palabras = texto.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def nombres_unicos(self, texto):
        palabras = texto.split()

        unicos = set(palabras)

        return list(unicos)


# Crear objeto
analizador = AnalizadorNombres()

texto = "Ana Luis Pedro Ana Maria Luis Juan Pedro"

# Buscar nombres que empiezan con "A"
print(analizador.buscar_por_inicio(texto, "A"))

# Agrupar por longitud
print(analizador.agrupar_por_longitud(texto))

# Obtener nombres únicos
print(analizador.nombres_unicos(texto))

























































































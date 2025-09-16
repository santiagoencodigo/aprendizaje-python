

# Estos son mis ejercicios para aprender python


while True:    #    Ciclo infinito hasta que el usuario decida salir


    #Menú principal de ejercicios


    print()
    print()

    print()
    print("Estos son diferentes ejercicios de python para seguir la ruta de mi aprendizaje")
    print()

    print("Inserte el numero 0 si no quiere ver ningún ejercicio.")
    print()

    print("Inserte el numero 1 para mirar ejercicios propuestos por ING. Galvis ")
    print()

    print("Inserte el numero 2 para mirar otro grupo de ejercicios propuestos por ING. Triana")
    print()

    print("Inserte el numero 3 para observar historias de usuario OperPan")
    print()


    # Proceso de selección de caso/ejercicio de 
    

    seleccion = int(input("Escribe un numero para escojer el tema que quieres ver: "))
    print()

    if seleccion == 0:

        print("Saliendo del programa. Hasta luego, gracias por haber estado aqui.")
        print()

        break   # Salir del bucle principal


    # Condicionales para selección del ejercicio propuesto


        # Ejercicios Propuestos por Ingeniero Julio Galvis

    elif seleccion == 1: 
        print()

        print("Ejercicios Propuestos por Ingeniero Julio Galvis:")

        print()


            # Menú ejercicios Propuestos ING. Galvis.


        print("Inserte el numero 1 para - Mirar Ejercicios de LISTAS")
        print("Inserte el numero 2 para - Mirar Ejercicios de DICCIONARIOS")  
        print("Inserte el numero 3 para - Mirar Ejercicios de TUPLAS") 
        print("Inserte el numero 4 para - Mirar Ejercicios de CONJUNTOS")  

        print()
        
        galvis_seleccion =int(input("Escribe el numero de acuerdo a lo que quieras ver: "))
        print()

            #Ejercicios de Lista Python

        if galvis_seleccion == 1:

            print()

            print("Ejercicios de LISTAS")
            print()

            print("A continuación ejercicios de listas en Python")
            print("Una lista de Python es una secuencia ordenada de elementos.")
            print("Las propiedades de una lista son Mutable, Ordenado, Heterogéneo, Duplicados")

            print("Estos ejercicios fueron propuestos por el Ingeniero Julio Galvis.")
            print()


                #Menú de ejercicios listas.


            print("Inserte el numero 1 para mirar - Ejercicio 1: Realizar operaciones básicas con listas")
            print("Inserte el numero 2 para mirar - Ejercicio 2: Realizar manipulación de listas")
            print("Inserte el numero 3 para mirar - Ejercicio 3: Suma y promedio de todos los números de una lista")
            print("Inserte el numero 4 para mirar - Ejercicio 4: Invertir una lista")
            print("Inserte el numero 5 para mirar - Ejercicio 5: Convierte cada elemento de una lista en su cuadrado")

            print()

            print("Inserte el numero 6 para mirar - Ejercicio 6: Encuentra el máximo y el mínimo")
            print("Inserte el numero 7 para mirar - Ejercicio 7: Contar ocurrencias")
            print("Inserte el numero 8 para mirar - Ejercicio 8: Ordenar una lista de números")
            print("Inserte el numero 9 para mirar - Ejercicio 9: Crear una copia de una lista")
            print("Inserte el numero 10 para mirar - Ejercicio 10: Combinar dos listas")

            print()

            print("Inserte el numero 11 para mirar - Ejercicio 11: Eliminar cadenas vacías de la lista de cadenas")
            print("Inserte el numero 12 para mirar - Ejercicio 12: Eliminar duplicados de la lista")
            print("Inserte el numero 13 para mirar - Ejercicio 13: Eliminar todas las ocurrencias de un elemento específico de una lista")
            print("Inserte el numero 14 para mirar - Ejercicio 14: Comprensión de listas para números")
            print("Inserte el numero 15 para mirar - Ejercicio 15: Acceder a listas anidadas")

            print()

            print("Inserte el numero 16 para mirar - Ejercicio 16: Aplanar lista anidada")
            print("Inserte el numero 17 para mirar - Ejercicio 17: Concatenar dos listas índice por índice")
            print("Inserte el numero 18 para mirar - Ejercicio 18: Concatenar dos listas en el siguiente orden")
            print("Inserte el numero 19 para mirar - Ejercicio 19: Iterar ambas listas simultáneamente")
            print("Inserte el numero 20 para mirar - Ejercicio 20: Agregar un nuevo elemento a la lista después de un elemento específico")

            print()

            print("Inserte el numero  para mirar - Ejercicio 21: Ampliar la lista anidada agregando la sublista")
            print("Inserte el numero  para mirar - Ejercicio 22: Reemplazar el elemento de la lista con el nuevo valor si se encuentra")

            print()

            print("Escoje 10 para mirar - Juegos con listas --> Eliminar diccionario ")
            print("Escoje 20 para mirar - Juegos con listas --> Vaciar diccionario ")
            print("Escoje 30 para mirar - Juegos con listas --> Limpiar diccionario")
            print("Escoje 40 para mirar - juegos con listas --> Fusionar Diccionarios")
            print()



                #INPUT
            galvis_ejercicios_listas = int(input("¿Qué ejercicio deseas ver? : "))



                # Ejercicio 1: Realizar operaciones básicas con listas

            if galvis_ejercicios_listas == 1 :

                print()
                print("Ejercicio 1: Realizar operaciones básicas con listas")

                my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #Una lista se caracteriza por tener [ ]

                    # Se espera imprimir el tercer elemento

                print("Esta es una lista original", my_list)
                print()
                print("Este es el tercer elemento de esa lista", my_list[2])
                print()

                    # Se espera imprimir el número de elementos en la lista

                list_length = len(my_list) #Variable con valor len de la lista
                print("La lista contiene ",list_length,"elementos")
                print()

                    # Se espera comprobar si la lista esta vacia

                    # Se determina si esta vacio comparando el valor del len de la lista con 0

                if list_length == 0:
                    print("La lista esta vacia.")
                else:
                    print("La lista no esta vacia.")
            


                #Ejercicio 2: Realizar manipulación de listas

            elif galvis_ejercicios_listas == 2:

                my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                print()
                print("Ejercicio 2: Realizar manipulación de listas")

                print()
                print("La lista original es: ",my_list)

                    # Cambiar Elemento: el segundo elemento de la lista "20" por 200 e imprime la lista actualizada

                print()
                my_list[1] = 200
                print("my_list[1] = 200")
                print("De la lista, en la posición 2 será = a 200.")
                print("Por lo que: ", my_list)
                print()

                    # Añadir Elemento: 600 al final de la lista  e imprimir de nuevo la lista 

                my_list.append(600)
                print("my_list.append(600)")
                print("La lista despues de usar Append para añadirle el numero 600 al final: ", my_list)
                print()

                    # Insertar Elemento: 300 en la tercera posición de la lista e imprimir a lista actualizada

                my_list.insert(2, 300) #En el indice 2 de la lista, remplazar el valor por 300
                print("my_list.insert(2, 300)")
                print("Al insertarle el numero 300 en la tercera posición: ", my_list)
                print()

                    # Eliminar Elemento por valor: Elimina 600 de la lista e imprime la lista 

                my_list.remove(600)
                print("my_list.remove(600)")
                print("La lista al remover el nuevo elemento al final de la lista - 600 : ", my_list)
                print()

                    # Eliminar Elemento por indice: Elimina el primer elemento de la lista e imprime la lista

                del my_list[0]  
                print("del my_list[0]")   
                print("La lista al eliminar el elemento de la posición 0: ")
                print(my_list)    



                # Ejercicio 3: Suma y promedio de todos los números de una lista

            elif galvis_ejercicios_listas == 3:
                print()
                print("Ejercicio 3: Suma y promedio de todos los números de una lista")
                print()      
                
                numeros_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                print("La lista es: ", numeros_lista)
                
                    #Proceso
                    
                total_numeros = sum(numeros_lista)
                print("La suma de todos los numeros de la lista es: ", total_numeros)
                    #  sum() es una función incorporada que calcula directamente la suma de
                    #  todos los elementos numéricos de la lista.
                total_elementos = len(numeros_lista)
                print("El total de numeros de elementos de la lista es: ", total_elementos)
                    # len() es otra función incorporada que devuelve el número de elementos de la lista.
                print()
                
                print("por lo que el promedio aritmetico de los valores de esta lista es: ", total_numeros/total_elementos)
                
                
                
                #Ejercicio 4: Invertir una lista
                
            elif galvis_ejercicios_listas == 4:
                print()
                print("Ejercicio 4: Invertir una lista")
                print()
                
                numeros_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                print("La lista es: ", numeros_lista)
                
                numeros_lista_invertida = numeros_lista.reverse()    
                print("Por medio de numeros_lista.reverse() la lista se invierte dando como resultado:", numeros_lista_invertida)  
                
                    #Segunda Solución
                    
                print()
                print("La segunda solución puede ser mediante lista[::-1]")
                
                numeros_lista_invertida_dos = numeros_lista[::-1]
                print("La lista invertida es: ", numeros_lista_invertida_dos)



                #  Ejercicio 5: Convierte cada elemento de una lista en su cuadrado
                
            elif galvis_ejercicios_listas == 5:
                print()
                print("Ejercicio 5: Convierte cada elemento de una lista en su cuadrado")
                print()
                print("Dada una lista de números, escriba un programa para convertir cada elemento de una lista en su cuadrado.")
                print("Iterar números de una lista uno por uno usando a para bucle y calcula el cuadrado del número actual")
                print()
                
                numbers = [1, 2, 3, 4, 5, 6, 7]
                print("La lista es: ", numbers)
                
                res = [] # RES = Lista Vacia
                for i in numbers: # Recorre cada elemento de la lista 
                    res.append(i * i) # Se agrega cada a elemento de la lista res ese mismo numero multiplicado por ese mismo numero
                                      # La letra I representa cada elemento de la lista de forma temporal 
                print(res)
                print()
                
                print("Segunda Solución --> Comprensión de listas")
                res_dos = [x * x for x in numbers]
                print(res_dos)
                
                
                # Ejercicio 6: Encuentra el máximo y el mínimo
                
            elif galvis_ejercicios_listas == 6:
                print()
                print("Ejercicio 6: Encuentra el máximo y el mínimo")
                print()
                print("Encuentre e imprima el número más grande y más pequeño de una lista [8, 2, 15, 1, 9]")
                print()
                
                data = [8, 2, 15, 1, 9]
                print("La lista es: ", data)
                
                minimo = min(data) # Saca el numero más pequeño de la lista
                max = max(data) # Saca el numero mayor de la lista
                
                print("En la lista el numero mayor es: ", max, ", y el numero menor es: ", minimo)
                
            
                # Ejercicio 7: Contar ocurrencias

            elif galvis_ejercicios_listas == 7:
                print()
                print("Ejercicio 7: Contar ocurrencias")
                print()
                print("Cuente e imprima cuántas veces 'Football' aparece en la lista.")
                print()
                
                sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis', 'Football']
                
                cuenta_de_elementos_listas = sports.count('Football')
                print("La lista es: ", sports)
                print()
                print("Las listas de Python tienen un count() método que permite contar las ocurrencias de un elemento específico dentro de la lista.")
                print("Por lo que sports.count('Football') ")
                
                print()
                
                print("La palabra 'FootBall' en la lista aparece ", cuenta_de_elementos_listas, "veces.")
                
                
                
                # Ejercicio 8: Ordenar una lista de números
                
            elif galvis_ejercicios_listas == 8: 
                print()
                print("Ejercicio 8: Ordenar una lista de números")
                print()
                print("Ordene una lista determinada de números en orden ascendente e imprímala.")
                print()
                print("Las listas de Python tienen un método incorporado sort() para ordenar elementos in situ, y también hay una función incorporada sorted() que devuelve una nueva lista ordenada sin modificar la original.")
                print()
                
                numbers = [5, 2, 8, 1, 9]
                numbers_dos = [55, 23, 81, 1, 39]
                
                print()
                print("La lista es: ", numbers)
                
                print("Solución con Sort")
                print()
                
                    # Modifica la lista original
                numbers.sort() # .sort() es un metodo de listas y modifica la lista original devolviendolas en orden (menor - mayor)
                print("La lista ordenada con Sort = ", numbers)
                print()
                
                print("Solución con Sorted")
                
                print("La lista es: ", numbers_dos)
                    # No modifica la lista original
                Sorted = sorted(numbers_dos) # sorted es una función incorporada de Python y devuelve una lista diferente por lo que no modifica la original.
                print("La lista ordenada con Sorted = ", Sorted)
                
                
                
                # Ejercicio 9: Crea una copia de una lista
            
            elif galvis_ejercicios_listas == 9:
                print()
                print("Ejercicio 9: Crea una copia de una lista")
                print()
                print("Crea una copia de una lista [10, 20, 30] y modificar la copia. Imprima tanto la lista original como la copiada para demostrar que son independientes.")
                print()
                
                original_list = [10, 20, 30] # Lista Original
                print("La lista original es: ", original_list)
                print()
                    # Primer Forma de copiar una lista
                lista_copiada = original_list[:] # Copia los elementos de la lista
                print("La lista copiada es igual a la original: ", lista_copiada)
                print()
                
                    # Proceso
                lista_copiada.append(40) # Agrega al final de la lista un 40
                lista_copiada[0] = 100 # En el indice 0 de la lista (10) va a ser modificado por 100
                
                print("La lista copiada al ser modificada queda como: ", lista_copiada)
                print()
                print("Pero la lista original sigue manteniendo sus mismos atributos: ", original_list)
                print()
                
                    # Segunda forma de copiar una lista
                tercera_copia = list(original_list) # list() constructor para crear una nueva lista a partir de una existente, lo que también da como resultado una copia superficial.
                print("La tercera copia de la lista es: ", tercera_copia)
                
                tercera_copia.append(50)
                print("La tercera copia de la lista al modificarla es: ", tercera_copia)
                
                tercera_copia[1] = 916
                print("Al añadirle una ultima modificición la lista queda como: ", tercera_copia)
                print()
                
                    # Tercera forma de copiar una lista
                cuarta_copia = original_list.copy() # Realiza una copia desde una función
                                                    # Esta es la forma más explícita de crear una copia superficial, disponible desde Python 3.3 en adelante.
                print("La cuarta copia de la lista original es: ", cuarta_copia)
                
                print()
                print("Se espera añadirle como numero final (911), y modificar el segundo numero por (400)")
                
                    # Proceso
                cuarta_copia.append(911)
                cuarta_copia[1] = 400
                
                print("La lista al ser modificada: ",cuarta_copia)
                print()
                
                
                
                # Ejercicio 10: Combina dos listas
                
            elif galvis_ejercicios_listas == 10:
                print()
                print("Ejercicio 10: Combina dos listas")
                print()
                print("Combine las dos listas dadas en una sola lista e imprímala.")
                print()
                
                list_a = [1, 2] # Lista 1
                print("La lista A es: ", list_a)
                print()
                
                list_b = [3, 4] # Lista 2
                print("La lista B es: ", list_b)
                print()
                
                    # Primera forma de combinar listas
                
                list_c = list_a + list_b
                
                print("La primera forma es utilizando el operador + para sumar las dos listas como string")
                print("Por lo que la lista quedo como: ", list_c)
                print()
                
                    # Segundo metodo de combinar listas
                
                print("El segundo metodo es por medio de: .extend() en la lista")
                lista_d = [1, 2]
                lista_d.extend(list_b)
                
                print("La lista combinada por medio del segundo metodo es: ", lista_d)
                print()
                
                    # Tercer metodo para combinar listas
                    
                combinacion_listas = [*list_a, *list_b]
                print("Este es el metodo [*list_a, *list_b]")
                print("Por lo que la lista combinada queda como: ", combinacion_listas)
                print()
                
                
                
                #  Ejercicio 11: Eliminar cadenas vacías de la lista de cadenas
             
            elif galvis_ejercicios_listas == 11:   
                print()
                print("Ejercicio 11: Eliminar cadenas vacías de la lista de cadenas")
                print()
                print("Elimine los elementos vacios de la lista")
                print()
                
                list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"] # Lista con " " vacias.
                
                print("La lista es: ", list1)
                print()
                print("Nuestro metodo para esto es: lista_filtrada = list(filter(None, list1))")
                
                lista_filtrada = list(filter(None, list1)) # Se usa FILTER 
                    # filter(función, iterable) recorre cada elemento del iterable y se queda con aquellos para los que la función devuelve True.
                    
                print("Se utiliza un filter() función para eliminar None escriba de la lista")
                print(lista_filtrada)
                
                
            
                # Ejercicio 12: Eliminar duplicados de la lista
                
            elif galvis_ejercicios_listas == 12: 
                print()                
                print("Ejercicio 12: Eliminar duplicados de la lista")
                print()
                print("Escriba una función que tome una lista con elementos duplicados y devuelva una nueva lista con solo elementos únicos.")
                print()
                
                list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4] # Lista original
                print("La lista original es: ", list_with_duplicates)
                
                print()
                
                set_unico_elementos = set(list_with_duplicates) # set() en Python crea un conjunto, los conjuntos no permiten repetidos
                                                                # Asi que automaticamente elimina los valores repetidos
                                                                
                lista_unica = list(set_unico_elementos) # Convierte el conjunto en una lista nuevamente
                
                print("La lista sin duplicados es: ", lista_unica)
                
                
                
                # Ejercicio 13: Eliminar todas las apariciones de un elemento específico de una lista
                
            elif galvis_ejercicios_listas == 13:
                print()
                print("Ejercicio 13: Eliminar todas las apariciones de un elemento específico de una lista")
                print()
                print("Dada una lista de Python, escriba un programa para eliminar todas las apariciones del elemento 20.")
                print()
                
                list1 = [5, 20, 15, 20, 25, 50, 20, 5, 20, 15, 20, 25, 50, 20]
                print("La lista original es: ", list1)
                
                def remove_value(sample_list, val):
                    return [i for i in sample_list if i != val]
                
                nueva_lista = remove_value(list1, 20)
                print("La lista al eliminarle el valor 20", nueva_lista)
                
                    # Segunda Solución
                print()
                
                
                
            elif galvis_ejercicios ==10:  #  Juegos con listas { }  -->  DEL = DELETE

                my_dict = {'name':'alice', 'age':25, 'city':'Bogotá', 'profesion':'Doctor'}
                print(f"Original Dictionary: {my_dict} ")

                del my_dict['profesion']
                print(f"Updated dictionary after removing 'profesion': {my_dict} ")

                print("printing all key-value pairs:")
                for key, value in my_dict.items():
                    print(f"{key}: {value}")

                def check_key_exist(dictionary, key_to_check):
                    return key_to_check in dictionary
                
                key1 = 'age'
                print(f"Does {key1} exist? {check_key_exist(my_dict, key1)} ")


            elif galvis_ejercicios == 20: # Juegos con listas { } --> Funcion vacia


                llaves = ['Ten' 'Twenty' 'Thirty']
                valores = [10, 20, 30]

                resultado_diccionario = dict(zip(llaves,valores))
                print(resultado_diccionario)

                #Diccionario Vacio = Empty Dictionary
                resultado_diccionario = dict()

                for i in range(len(llaves)):
                    resultado_diccionario.update({llaves[i] : valores[i]})
                print(resultado_diccionario)


            elif galvis_ejercicios == 30: # Juegos con listas { } --> Limpiar diccionario

                my_dict = {'name':'alice', 'age':25, 'city':'Bogotá', 'profesion':'Doctor'}
                print(f"Original Dictionary: {my_dict} ")

                my_dict.clear()
                print(f"Dictionary after removing all items: {my_dict}")


            elif galvis_ejercicios == 40: # Juegos con listas { } --> Fusionar Diccionarios

                diccionario1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
                diccionario2 = {'Diez': 10, 'Veinte':20, 'Treinta': 30}

                diccionario3 = {**diccionario1, **diccionario2}
                print(diccionario3)

        elif galvis_seleccion == 2:
            print()
            print("Ejercicios de DICCIONARIOS")
            print("Estos ejercicios fueron propuestos por    ING. Galvis")


            

        elif galvis_seleccion == 3: 
            print("Ejercicios de TUPLAS")

        elif galvis_seleccion == 4:
            print("Ejercicios de CONJUNTOS") 

        else:
            print("No existe este ejercicio.")



        # Ejercicios propuestos por la Ingeniera Angelica Triana

    elif seleccion == 2: 

        #Inicio de temario

        print("A continuación vamos a mirar ejercicios propuestos por la ING. Triana")

        print()

        apuntes_triana = int(input("Ingrese el numero de acuerdo a lo que quiera ver:"))

        print()

        print('Inserte el numero 1 para mirar ejemplo de función utilizando "DEF" ')


        if apuntes_triana == 1:

            print("Funcion DEF - SUMAR")
            def sumar(a,b):
                resultado = a + b
                return resultado

                # LLamar a la funcion

            suma = sumar(3,5)
            print(f"la suma es: {suma}")

        else:
            print()
            print("Este caso no se encuentra, entonces esta en Proceso")


        #Algoritmos de Historias de Usuario
    elif seleccion == 3: # Historia de usuario HU-TR-01

        print()
        print("Ingrese el numero 1 para mirar Historia de usuario: HU-TR-01")
        print("Ingrese el numero 2 para mirar Historia de usuario: HU-LG-01")
        print()


        seleccion_historia_usuario = int(input("Inserte el numero de acuerdo a lo que quiera ver: "))


        if seleccion_historia_usuario == 1:

            print("")
            print("Historia de usuario: HU-TR-01 ")
            print("Como Administrador necesito asignar tareas a empleados asociándolas a un turno y fecha límite, organizar el trabajo asegurando trazabilidad y cumplimiento en los tiempos.")
            print("")

            # Inputs

            # Identificación del trabajador (ID/NOMBRE)
            HU_TR_01_identificador_trabajador = (input("Ingrese el ID/Nombre del trabajador: "))
            HU_TR_01_turno = (input('Ingrese "Diurno" o "Nocturno" de acuerdo al turno del trabajador:'))

            print()

            # Tiempos en fecha y hora del inicio y fin de la tarea
            HU_TR_01_fecha_inicio = (input("Ingrese la fecha de inicio de la tarea en formato (12-09-2025): "))
            HU_TR_01_hora_inicio = (input("Ingrese la hora de inicio de la tarea en formato (4:00 PM): "))

            print()

            HU_TR_01_fecha_limite = (input("Ingrese la fecha limite de la tarea en formato (12-09-2025): "))
            HU_TR_01_hora_limite = (input("Ingrese la hora limite de la tarea en formato (4:00 PM):: "))

            # Tarea a realizar
            HU_TR_01_asignar_tarea = (input("Ingrese la tarea a asignar al trabajador: "))

            #Outputs
            print()
            print("Resumen")
            print()

            print("El trabajador", HU_TR_01_identificador_trabajador, "En el turno", HU_TR_01_turno)
            print()

            print("En la fecha", HU_TR_01_fecha_inicio, "A las horas", HU_TR_01_hora_inicio)
            print()

            print("Debe realizar la tarea: ", HU_TR_01_asignar_tarea, "con maximo plazo a la fecha", HU_TR_01_fecha_limite, "A las horas ", HU_TR_01_hora_limite )
            print()


        elif seleccion_historia_usuario == 2:
            print()
            print("Historia de usuario: HU-LG-01")
            print("Como Administrador necesito ingresar al sistema con usuario y contraseña, con la finalidad de acceder a las funciones de gestión de empleados.")

            print()
            print("Nombre Usuario Administrador: cuentaAdmin ")
            print("Contraseña Administrador: admin ")

            #Inputs

            print()
            HU_LG_01_usuario = input("Escriba el nombre de su usuario: ")
            print()

            HU_LG_01_contraseña = input("Escriba su contraseña: ")
            print()

            print("¿Role?")
            print()

            #Identificación de Usuario

        else:
            print("Historia de usuario en Proceso")

        # Ultima opción por descarte en python
    else:
        print("Ejercicio En Proceso")

# FIN DE CICLO

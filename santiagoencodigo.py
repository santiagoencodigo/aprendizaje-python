# Estos son mis ejercicios para aprender python
print()
print("Estos son diferentes ejercicios de python para seguir la ruta de mi aprendizaje")
print()

#Menú de ejercicios
print("Escoje 1 para mirar ejercicio-lista-1-funcion-delete ")
print("Escoje 2 para mirar ejercicio-lista-2-funcion-delete ")
print("Escoje 3 para mirar ejercicio-lista-2-funcion-limpiar-diccionario")
print("Escoje 4 para mirar ejercicio-lista-2-funcion")

print("")

print("Inserte el numero 800 para observar ejercicio de historias de usuario OperPan")

# Proceso de selección de caso/ejercicio de aprendizaje
seleccion = int(input("Escribe un numero para escojer el tema que quieres ver: "))
print()


#Condicionales para selección del ejercicio propuesto


if seleccion == 1: # Juegos con listas { }  -->  DEL = DELETE

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

elif seleccion == 2: # Juegos con listas { } --> Funcion vacia 
    llaves = ['Ten' 'Twenty' 'Thirty']
    valores = [10, 20, 30]

    resultado_diccionario = dict(zip(llaves,valores))
    print(resultado_diccionario)

    #Diccionario Vacio = Empty Dictionary
    resultado_diccionario = dict()

    for i in range(len(llaves)):
        resultado_diccionario.update({llaves[i] : valores[i]})
    print(resultado_diccionario)


elif seleccion == 3: # Juegos con listas { } --> Limpiar diccionario
    my_dict = {'name':'alice', 'age':25, 'city':'Bogotá', 'profesion':'Doctor'}
    print(f"Original Dictionary: {my_dict} ")

    my_dict.clear()
    print(f"Dictionary after removing all items: {my_dict}")


elif seleccion == 4: # Juegos con listas { } --> Fusionar Diccionarios
    diccionario1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
    diccionario2 = {'Diez': 10, 'Veinte':20, 'Treinta': 30}

    diccionario3 = {**diccionario1, **diccionario2}
    print(diccionario3)


#Algoritmos de Historias de Usuario
elif seleccion == 800: # Historia de usuario HU-TR-01
    print("")
    print("Historia de usuario: HU-TR-01 ")
    print("Como Administrador necesito asignar tareas a empleados asociándolas a un turno y fecha límite, organizar el trabajo asegurando trazabilidad y cumplimiento en los tiempos.")
    print("")

    # Inputs

    # Identificación del trabajador (ID/NOMBRE)
    HU_TR_01_identificador_trabajador = (input("Ingrese el ID/Nombre del trabajador: "))
    HU_TR_01_turno = (input('Ingrese "Diurna" o "Noctura" de acuerdo al turno del trabajador:'))

    print()

    # Tiempos en fecha y hora del inicio y fin de la tarea
    HU_TR_01_fecha_inicio = (input("Ingrese la fecha de inicio de la tarea: "))
    HU_TR_01_hora_inicio = (input("Ingrese la hora de inicio de la tarea: "))

    print()

    HU_TR_01_fecha_limite = (input("Ingrese la fecha limite de la tarea: "))
    HU_TR_01_hora_limite = (input("Ingrese la hora limite de la tarea: "))

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

    # Ultima opción por descarte en python
else:
    print("En proceso")
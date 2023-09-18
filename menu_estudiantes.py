import os   #modulo con el metodo system para enviar instrucciones al sistema a traves de la consola.
import time     #modulo con el metodo sleep para hacer pausas en la apliacion.
from msvcrt import getch    #modulo con su metodo para recibir una interaccion con el teclado y procesarla instantaneamente.

#Comprobar si una cadena de caracteres contiene un numero flotante.
def isfloat(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False
    
#Crear la lista de alumnos.
def crearLista(num_alumnos:int, num_notas:int) -> list:
    alumnos = [0]*num_alumnos   #Se crea la lista que va a albergar los registros.
    
    for i in range(0, len(alumnos)):
        validar_nombre = False  #Validador para el nombre del alumno.
        
        #Recibe el nombre del alumno y convierte los espacios de la lista en diccionarios.
        while not validar_nombre:
            alumnos[i] = dict(nombre=input(f"Ingrese el nombre del alumno #{i+1}: "))
            if alumnos[i]['nombre'].isalnum():
                validar_nombre = True
            else:
                print("El nombre ingresado no puede ser alfanumerico...")
                
        validar_nota = False    #Validador de nota
        
        #Recibe cada una de las notas del alumno y las guarda en el correspondiente registro
        while not validar_nota:
            j = 0
            while j in range(0, num_notas):
                alumnos[i][f'Nota {j+1}'] = input(f"Ingrese la nota {j+1} del alumno {alumnos[i].get('nombre')}: ")
                if isfloat(alumnos[i][f'Nota {j+1}']) and float(alumnos[i][f'Nota {j+1}']) <= 5:
                    alumnos[i][f'Nota {j+1}'] = float(alumnos[i][f'Nota {j+1}'])
                    validar_nota = True
                    j += 1
                else:
                    print("\nLa nota debe ser un numero entero o decimal en el rango (0 - 5.0)...\n")

        #Calculo del promedio o nota final por alumno.
        print("") 
        alumnos[i]['Promedio'] = 0.0
        for key, value in alumnos[i].items():
            if key != 'Promedio' and type(value) == float:
                alumnos[i]['Promedio'] += value        
        alumnos[i]['Promedio'] /= round(num_notas, 2)
        
    print("¡Se ha creado la lista exitosamente!...")
    time.sleep(4)
    os.system("cls")
    return alumnos

#Editar notas de un alumno.
def editarLista(alumnos:list, num_notas:int) -> list:
    search = [] #Lista que alberga los resultados de la busqueda.
    apendice = []   #Lista que alberga el indexado de las coincidencias dentro de la lista de alumnos.
    
    find_name = input("Ingrese el nombre del alumno a buscar: ")
    print("")
    
    #Busqueda de coincidencias con el nombre ingresado.
    for find in alumnos:
        if find_name.lower() in find.get('nombre').lower():
            apendice.append(alumnos.index(find))
            search.append(find)
    contador_result = 0
    
    #Mostrar los resultados de la busqueda.
    for result in search:
        contador_result+=1
        print("\033[94m\033[1m" + f"Resultado {contador_result}" + "\033[0m")
        for key, value in result.items():
            if key == 'Promedio':
                print(f"{key}:\t{value:.2f}")
            else:
                print(f"{key}:\t\t{value}")
        print("")
     
    #En caso de que la busqueda arroje resultados se realiza el proceso de cambio de notas.  
    if len(search) > 0:
        validar_resultado = False #Validador resultado.
        
        while not validar_resultado:
            resultado = int(input(f"¿Qué resultado desea editar? (1 - {len(search)}): ")) #Seleccion de resutado a editar.
            print("")
            
            #Si el resultado seleccionado esta dentro del rango, procede a recibir nota.
            if resultado in range(1, len(search)+1):
                validar_nota = False    #Validador nota.
                
                while not validar_nota:
                    nota = int(input(f"¿Que nota desea modificar? (1 - {len(search[resultado-1])-2}): ")) #Seleccion de nota a modificar.
                    print("")
                    
                    #Si la nota seleccionada esta dentro del rango, procede a modificar.
                    if (nota in range(1, len(search[resultado-1])-1)):
                        
                        while True: #Validador de la nota ingresada
                            try:
                                search[resultado-1][f'Nota {nota}'] = float(input(f"Ingrese el nuevo valor de la nota {nota}: "))
                                if search[resultado-1][f'Nota {nota}'] in range[0, 6]:
                                    break
                                else:
                                    print("\nLa nota debe ser un numero entero o decimal en el rango (0 - 5.0)...\n")
                            except ValueError:
                                print("\nLa nota debe ser un numero entero o decimal en el rango (0 - 5.0)...\n")
                        
                        #Se calcula nuevamente el promedio del registro editado.    
                        for key, value in search[resultado-1].items():
                            if key != 'Promedio' and type(value) == float:
                                search[resultado-1]['Promedio'] += value
                        search[resultado-1]['Promedio'] /= round(num_notas, 2)
                        
                        #Se realizan los cambios en el registro correspondiente dentro de la lista de alumnos.
                        alumnos[apendice[resultado-1]] = search[resultado-1]
                        print("\n¡Se ha cambiado la nota con exito!\n")
                        validar_nota = True
                        time.sleep(3)
                        decision = "" #Control de la decision.
                        
                        #Consulta si desea editar nuevamente.
                        while not decision in ["si", "no"]:
                            decision = input("¿Desea volver a buscar? (si / no): ")
                            
                            if decision == "no":
                                validar_resultado = True
                            elif decision == "si":
                                validar_resultado = True
                                print("")
                                alumnos = editarLista(alumnos, num_notas)
                            else:
                                print("La opcion no es valida...")
                    
                    else:
                        print("El numero de nota no esta dentro del rango...\n")
                        
            else:
                print("El resultado no es válido...\n")
                
    else:
        print("La busqueda no arrojo ningun resultado...\n")
        time.sleep(4)
        decision = ""
        
        while not decision in ["si", "no"]:
            decision = input("¿Desea volver a buscar? (si / no): ")
            
            if decision == "no":
                validar_resultado = True
            elif decision == "si":
                validar_resultado = True
                print("")
                alumnos = editarLista(alumnos, num_notas)
            else:
                print("\nLa opcion no es valida...\n")                
                
    return alumnos
    
#Muestra la lista de los alumnos.
def mostrarLista(alumnos:list):
    for i in range(len(alumnos)):
        print("\033[94m\033[1m" + f"{i+1}." + "\033[0m")
        for key, value in alumnos[0].items():
            if key == 'Promedio':
                print(f"{key}:\t{value:.2f}")
            else:
                print(f"{key}:\t\t{value}")
    print("")

#Menu de opciones.
def menu():
    lista = False #Verifica si ya se ha creado una lista.
    opcion = 0
    validar_menu = False    #Validador de menu.
    
    while not validar_menu:
        print("¿Que deseas hacer?\n\n1. Crear lista de alumnos.\n2. Editar lista.\n3. Mostrar lista\n4. Salir")
        opcion = str(getch())[2]    #El metodo getch devuelve un str de forma b'tecla pulsada', con el [2] selecciono unicamente la tecla pulsada dentro de ese str.
        os.system("cls")
        
        #Si la opcion seleccionada está dentro del rango establecido, se procede.
        if opcion.isdigit() and int(opcion) in range(0, 5):
            
            #Si la opcion es 1, se crea la lista, se comprueba si ya existe una lista y se da la opcion de crearla nuevamente.
            if opcion == "1":
                decision = ""
                validar_lista = False #Validador de lista.
                
                while not validar_lista:
                    
                    if not lista:
                        
                        while True:
                            try:
                                num_alumnos = int(input("Ingrese el numero de alumnos: "))
                                num_notas = int(input("Ingrese el numero de notas: "))
                                break
                            except ValueError:
                                print("\nLos valores deben ser numeros enteros...\n")
                                
                        print("")
                        alumnos = crearLista(num_alumnos, num_notas)
                        lista = True
                        validar_lista = True
                    else:
                        
                        while decision not in ["si", "no"]:
                            decision = input("Ya existe una lista... ¿Desea crearla nuevamente? (si / no): ")
                            
                            if decision == "no":
                                validar_lista = True
                                os.system("cls")
                            elif decision == "si":
                                lista = False
                                os.system("cls")
                            else:
                                print("La opcion ingresada no es valida...\n")
                                time.sleep(3)
            
            #Si la opcion es 2, se procede a editar una nota de la lista siempre y cuando la lista ya exista.                    
            elif opcion == "2":
                
                if lista:
                    alumnos = editarLista(alumnos, num_notas)
                    os.system("cls")
                else:
                    print("No se ha creado una lista de alumnos aun...")
                    time.sleep(3)
                    os.system("cls")
            
            #Si la opcion es 3, se muestra la lista.
            elif opcion == "3":
                
                if lista:
                    mostrarLista(alumnos)
                    print("Presione [Enter] para regresar...")
                    seguir = getch()
                    os.system("cls")
                else:
                    print("No se ha creado una lista de alumnos aun...")
                    time.sleep(3)
                    os.system("cls")
            
            #Salir del menu.        
            elif opcion == "4":
                validar_menu = True
                
menu()
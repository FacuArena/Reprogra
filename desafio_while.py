#DESAFIO 1 _ WHILE. "UNA ENCUESTA TECNOLOGICA EN UTN TECHNOLOGIES"

'UTN Thechnologies, una reconocida' #Software Factory, 
'está en busqueda de idesa para su proximo desarrollo'
'en' #Python
'con el objetivo de revolucionar el mercado'

'Las tecnologias en evalucaion son:'
#Inteligencia Artificial  (IA)
#Realidad virtual/Aumentada (RV/RA)
#Internet de las cosas (IoT)

'Para tomar una desicion informada. la empresa' 
'ha lanzado una encuesta entre sus empleados'
'con el proposito de analizar ciertas metricas'

#Recoleccion de datos
'Cada empleado encuestado debera proporcionar la siguiente informacion:'
#Nombre del empleado
#Edad
#Genero (Masculino/Femenino/Otro)
#Tecnlogia elegida (IA/RV/RA/IoT)

'El sistema debera permitir ingresar los datos de 10 empleados mediante terminal'

#Analisis de datos

'El sistema debera calcular las siguientes metricas:'
#1_ Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad 
    #esté entre 25 y 50 años (inclusive).

#2_ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    #*Su genero no sea femenino
    #*Su edad está entre los 33 y 40 años.
    
#3_ Empleado masculino de mayor edad: mostrar nombre y la tecnologia elegida.

'REQUISITOS DEL PROGRAMA:'
#1_ Los datos deben solicitarce y validarse correctamente.
#2_ Utilizar variables adecuadas para al,acenar la informacion y facilitar su analisis
#3_ Presentar los resultados de manera clara y organizada.

#Variables Acumuladores
contador = 0
contador_masculino_iot_ia = 0
contador_no_ia = 0
contador_total_33_40 = 0
edad_masculino_mayor = 0
nombre_masculino_mayor = ""
tecnologia_masculino_mayor = ""

print("\n// BIENVENIDO A LA ENCUESTA TECNOLOGICA \\\\\n")

while contador < 10:
    print(f"\n--- Empleado {contador + 1} ---")
    
    Nombre_empleado = input("Ingrese su nombre: ")
    while Nombre_empleado == "":
        print("El nombre no puede estar vacio. Por favor, ingrese su nombre nuevamente.")
        Nombre_empleado = input("Ingrese su nombre: ")
    
    Edad_empleado = int(input("Ingrese su edad: "))
    while Edad_empleado < 0 or Edad_empleado > 100:
        print("La edad debe estar entre 0 y 100. Por favor, ingrese su edad nuevamente.")
        Edad_empleado = int(input("Ingrese su edad: "))
    
    Genero_empleado = input("Ingrese su genero (Masculino/Femenino/Otro): ")
    while Genero_empleado not in ["Masculino", "Femenino", "Otro"]:
        print("Genero invalido. Por favor, ingrese su genero nuevamente.")
        Genero_empleado = input("Ingrese su genero (Masculino/Femenino/Otro): ")
    
    Tecnologia_elegida = input("Ingrese la tecnologia que eligio (IA/RV/RA/IoT): ")
    while Tecnologia_elegida not in ["IA", "RV", "RA", "IoT"]:
        print("Tecnologia invalida. Por favor, ingrese la tecnologia nuevamente.")
        Tecnologia_elegida = input("Ingrese la tecnologia que eligio (IA/RV/RA/IoT): ")
    
    #Analisis de datos
    #1_ Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
    if Genero_empleado == "Masculino" and (Tecnologia_elegida == "IoT" or Tecnologia_elegida == "IA") and (25 <= Edad_empleado <= 50):
        contador_masculino_iot_ia += 1
    
    #2_ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    #*Su genero no sea femenino
    #*Su edad está entre los 33 y 40 años.
    if Genero_empleado != "Femenino" and (33 <= Edad_empleado <= 40):
        contador_total_33_40 += 1
        if Tecnologia_elegida != "IA":
            contador_no_ia += 1    
        
    #3_ Empleado masculino de mayor edad: mostrar nombre y la tecnologia elegida.
    if Genero_empleado == "Masculino" and Edad_empleado > edad_masculino_mayor:
        nombre_masculino_mayor = Nombre_empleado
        tecnologia_masculino_mayor = Tecnologia_elegida
        edad_masculino_mayor = Edad_empleado

    contador += 1    

#Output
print("\n=== RESULTADOS DE LA ENCUESTA ===")
print(f"\n1_ Cantidad de empleados masculinos entre 25-50 años que votaron IoT o IA: {contador_masculino_iot_ia}")

if contador_total_33_40 > 0:
    porcentaje_distinto_ia = (contador_no_ia / contador_total_33_40) * 100
    print(f"\n2_ Porcentaje de empleados no femeninos entre 33-40 años que NO votaron IA: {int(porcentaje_distinto_ia)}%")
else:
    print("\n2_ No hay empleados que cumplan con los criterios de edad y género especificados")

if nombre_masculino_mayor:
    print(f"\n3_ Empleado masculino de mayor edad: {nombre_masculino_mayor} - {tecnologia_masculino_mayor}")
else:
    print("\n3_ No hay empleados masculinos registrados")

    


















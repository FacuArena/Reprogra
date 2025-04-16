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

    


#EXPLICACION DE GIT

"""
=========================================
    Git y GitHub - GUÍA PRÁCTICA en Python
=========================================

Este archivo explica en comentarios cómo subir archivos a GitHub
desde cero, usando GIT.

-----------------------------------------
Escenario 1️⃣ - Primera vez (con "git push --set-upstream origin master")
-----------------------------------------

Cuando estás trabajando en un proyecto nuevo y nunca hiciste un push
antes, GIT no sabe a dónde enviar tus archivos.

Por eso el primer `push` necesita indicar:

    git push --set-upstream origin master

✅ ¿Qué significa esto?
- "origin" es el nombre del repositorio remoto (en este caso GitHub).
- "master" es la rama principal del proyecto.

👉 Este comando establece una relación fija entre:
- Tu rama local (`master`) y
- La rama remota (`origin/master`).

Una vez configurado, en adelante sólo necesitás hacer:

    git push

...y Git enviará los cambios automáticamente al repositorio.

-----------------------------------------
Escenario 2️⃣ - Proyecto ya configurado (solo usando "git push")
-----------------------------------------

Cuando ya hiciste el `git push --set-upstream` por primera vez, Git
recuerda la dirección remota.

El flujo normal es:

    git add archivo.py
    git commit -m "Agrego archivo"
    git push

Con eso tus cambios suben a GitHub sin repetir la configuración.

-----------------------------------------
Escenario 3️⃣ - Sin configurar tu usuario de Git (global config)
-----------------------------------------

Si es la primera vez que usás Git en tu máquina, Git te va a pedir
que configures tu identidad.

Sin esto no podés hacer commits.

Para configurarlo:

    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_correo@example.com"

Esto queda guardado en tu computadora, y cada vez que hagas un commit
Git usará esos datos para registrar quién hizo el cambio.

👉 Si no hacés esto, Git mostrará un error tipo:
    "Please tell me who you are."

Una vez configurado, ya podés usar:

    git add archivo.py
    git commit -m "Mensaje"
    git push

-----------------------------------------
💡 RESUMEN:

1️⃣ Proyecto nuevo -> usar:
    git push --set-upstream origin master

2️⃣ Proyecto ya vinculado -> solo:
    git push

3️⃣ Primera vez usando Git en la PC -> configurar:
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_correo@example.com"

¡Y listo! 😎 Así es como se suben archivos a GitHub.
"""

print("¡Git explicado! Leé los comentarios de este archivo para entender cada situación.")


















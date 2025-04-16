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

print("¡Git re versionado ha sido agregado a esta version guia git v2.")

print("prueba 3")
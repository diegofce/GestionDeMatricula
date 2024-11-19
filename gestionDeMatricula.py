estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

#Funciones para matricular

def matricular():
    nombre = input("Ingrese el nombre del estudiante: ")
    print("Seleccione el curso:")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    cursoSeleccionado = int(input('Ingrese el número correspondiente al curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {
            'nombre': nombre,
            'curso': curso
        }
        estudiantes.append(estudiante)

        print(f'Estudiante: {nombre}, matriculado en el curso {curso}correctamente')
    else:
        print(f'Opcion no valida, por favor ingrese un numero entre {len(cursos)}')

#funcion para asignar un docente a un curso

def asignarDocente():
    print("Seleccione el curso al que desee asignar un docente:")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    cursoSeleccionado = int(input('Ingrese el número correspondiente al curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]

        nombreDocente = input("Ingrese el nombre del docente: ")
        docente = {'nombre': nombreDocente, 'curso': curso}
        docentes.append(docente)

        print(f'Docente: {nombreDocente}, asignado al curso {curso} correctamente')
    else:
        print(f'Opcion no valida, por favor ingrese un numero entre {len(cursos)}')

#Funcion para asignar un horario a un curso

def asignarHorario():
    print("Seleccione el curso al que desee asignar un horario:")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")

    cursoSeleccionado = int(input('Ingrese el número correspondiente al curso: '))

    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]

        dias = input('Ingrese los dias de clase (Ejemplo: Martes y Jueves)')

        hora = input('Ingrese la hora de clase (Ejemplo: 10:00 a 12:00)')

        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)

        print(f'Horario asignado al curso {curso}: {dias} a las {hora}')
    else:
        print(f'Opcion no valida, recuerde que solo existe: {len(cursos)}')

def mostrarEstudiantes():
    if estudiantes:
        print("Estudiantes matriculados:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Curso: {estudiante['curso']}")
    else:
        print("No hay estudiantes matriculados.")

def mostrarDocentes():
    if docentes:
        print("Docentes asignados:")
        for docente in docentes:
            print(f"Nombre: {docente['nombre']}, Curso: {docente['curso']}")
    else:
        print("No hay docentes asignados.")

def mostrarHorarios():
    if horarios:
        print("\nHorarios asignados:")
        for horario in horarios:
            print(f"Curso: {horario['curso']}, Dias: {horario['dias']}, Hora: {horario['hora']}")
    else:
        print("No hay horarios asignados.")

while True:
        print("-------|||||||||----------")
        print("\nMenú de opciones:")
        print("1. Matricular estudiante")
        print("2. Asignar docente")
        print("3. Asignar horario")
        print("4. Mostrar estudiantes matriculados")
        print("5. Mostrar docentes asignados")
        print("6. Mostrar horarios asignados")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            matricular()
        elif opcion == "2":
            asignarDocente()
        elif opcion == "3":
            asignarHorario()
        elif opcion == "4":
            mostrarEstudiantes()
        elif opcion == "5":
            mostrarDocentes()
        elif opcion == "6":
            mostrarHorarios()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")    
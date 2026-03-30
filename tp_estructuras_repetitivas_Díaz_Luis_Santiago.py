#Trabajo Práctico Integrador

#Ejercicio 1: Caja de Kiosko

#1. Solicito el nombre al cliente (debe contener solo letras y no tener vacíos)
nombre = input("Cliente: ")
while not nombre.isalpha():
  nombre = input("Cliente (solo letras, sin espacios): ")

#2. Pedir la cantidad de productos a comprar (que sea un número entero, positivo y mayor a 0)
cantidad_str = input("Cantidad de productos: ")
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
  cantidad_str = input("Cantidad de productos (número entero mayor a 0): ")
cantidad = int(cantidad_str)

#3. Aplico bucle for para buscar descuentos por productos (si los hay)
total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
  #Pido el precio del producto
  precio_str = input(f"Producto {i} - Precio:")
  while not precio_str.isdigit():
    precio_str = input(f"Producto {i} - Precio (número entero positivo): ")
  precio = int(precio_str)

  #Pido el descuento S/N
  descuento_resp = input("Descuento S/N: ")
  while descuento_resp.lower() not in ("s", "n"):
    descuento_resp = input("Descuento (S/N): ")

  #Acumulo los totales (productos con y sin descuento)
  total_sin_descuento += precio
  if descuento_resp.lower() == "s":
    total_con_descuento += precio * 0.90
  else:
    total_con_descuento += precio

  #4. Cálculos y resultados
  ahorro = total_sin_descuento - total_con_descuento
  promedio = total_con_descuento / cantidad

  print(f"\nTotal sin descuentos: ${total_sin_descuento}")
  print(f"Total con descuentos: ${total_con_descuento:.2f}")
  print(f"Ahorro: ${ahorro:.2f}")
  print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2: Acceso al Campus y Menú Seguro

#1. Defino las credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

#2. Configuración del login (3 intentos máximo permitido)
intentos = 0
acceso = False
while intentos < 3:
  print(f"Intento {intentos + 1}/3")
  usuario = input("Usuario: ")
  clave = input("Clave: ")

  if usuario == usuario_correcto and clave == clave_correcta:
    acceso = True
    break
  else:
    intentos += 1
    restantes = 3 - intentos
    if restantes > 0:
      print(f"Credenciales incorrectas. Intentos restantes: {restantes}")

if not acceso:
  print("Cuenta bloqueada.")
else:
  print("Acceso concedido. Bienvenido al Campus")
  clave_actual = clave_correcta

#Configuración del menú principal (while repetitivo)
while True:
        print("\nMenú del Campus")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

#Validación del menú (debe ser número y estar entre 1 y 4)
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Opción inválida. Ingrese un número del 1 al 4.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            print("Estado de inscripción: INSCRIPTO")

        elif opcion == 2:
            #Opción de cambio de clave
            while True:
                nueva = input("Nueva clave (mínimo 6 caracteres): ")
                if len(nueva) < 6:
                    print("Incorrecto. La clave debe tener al menos 6 caracteres. ")
                    continue
                confirmacion = input("Confirma la nueva clave: ")
                if nueva != confirmacion:
                    print("Las claves no coinciden. Intentelo de nuevo.")
                else:
                    clave_actual = nueva
                    print("Clave actualizada correctamente.")
                    break
                
        elif opcion == 3:
            print("Frase motivacional: 'La programación no se trata de lo que sabes, sino de lo que puedes descubrir. Chris Pine, Aprende a programar.'")

        elif opcion == 4:
            print("Cerrando sesión...")
            break   

#Ejercicio 3: Agenda de turnos con nombres (sin utilizar listas)
#Variables de turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

#1) Pido el nombre al operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
  operador = input("Ingrese el nombre solo con letras y sin espacios: ")

print(f"\nBienvenido, {operador}. Sistema de turnos iniciado.")

#2) Establecemos el menú (menú repetitivo hasta salir)
opcion = ""
while opcion != "5":
  print(f"\nAgenda de Turnos (Operador: {operador})")
  print("1. Reservar turno")
  print("2. Cancelar turno")
  print("3. Ver agenda del día")
  print("4. Ver resumen general")
  print("5. Cerrar sistema")
  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    # Opción 1: Reservar
    dia_seleccionado = input("Dia (1=Lunes, 2=Martes):")
    if dia_seleccionado == "1" or dia_seleccionado == "2":
      nombre_paciente = input("Nombre del paciente: ")
      while not nombre_paciente.isalpha():
        nombre_paciente = input("Error. Ingrese solo letras: ")

      if dia_seleccionado == "1":
        if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
          print("El paciente ya tiene turno este día.")
        elif lunes1 == "": lunes1 = nombre_paciente
        elif lunes2 == "": lunes2 = nombre_paciente
        elif lunes3 == "": lunes3 = nombre_paciente
        elif lunes4 == "": lunes4 = nombre_paciente
        else:
          print("Agenda llena. No hay turnos disponibles para el Lunes.")
      else:
        if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
          print("El paciente ya tiene turno este día.")
        elif martes1 == "": martes1 = nombre_paciente
        elif martes2 == "": martes2 = nombre_paciente
        elif martes3 == "": martes3 = nombre_paciente
        else:
          print("Agenda llena. No hay turnos disponibles para el Martes.")
    else:
      print("Día no válido.")

  elif opcion == "2":
    # Cancelación del turno
    dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
    nombre_paciente = input("Nombre del paciente a cancelar: ")

    if dia_seleccionado == "1":
        if lunes1 == nombre_paciente: lunes1 = ""
        elif lunes2 == nombre_paciente: lunes2 = ""
        elif lunes3 == nombre_paciente: lunes3 = ""
        elif lunes4 == nombre_paciente: lunes4 = ""
        else:
          print("El paciente no tiene turno este día.")
    elif dia_seleccionado == "2":
        if martes1 == nombre_paciente: martes1 = ""
        elif martes2 == nombre_paciente: martes2 = ""
        elif martes3 == nombre_paciente: martes3 = ""
        else:
          print("El paciente no tiene turno este día.")
    else:
      print("Día no válido.")

  elif opcion == "3":
    # Ver agenda del día
    dia_seleccionado = input("Ver agenda de (1=Lunes, 2=Martes): ")
    if dia_seleccionado == "1":
      print("Agenda del día Lunes")
      #Turno 1
      if lunes1 != "":
        print("1. " + lunes1)
      else:
        print("1. (Libre)")

      #Turno 2
      if lunes2 != "":
        print("2. " + lunes2)
      else:
        print("2. (Libre)")

      #Turno 3
      if lunes3 != "":
        print("3. " + lunes3)
      else:
        print("3. (Libre)")

      #Turno 4
      if lunes4 != "":
        print("4. " + lunes4)
      else:
        print("4. (Libre)") # Added else for consistency

    elif dia_seleccionado == "2":
      print("Agenda del día Martes")
      #Turno 1
      if martes1 != "":
        print("1. " + martes1)
      else:
        print("1. (Libre)")

      #Turno 2
      if martes2 != "":
        print("2. " + martes2)
      else:
        print("2. (Libre)")

      #Turno 3
      if martes3 != "":
        print("3. " + martes3)
      else:
        print("3. (Libre)")

    else:
      print("Día no válido.")

  elif opcion == "4":
    #RESUMEN GENERAL
    #Conteo manual de turnos ocupados - turnos disponibles por día - días con más turnos (o que empataron)

    #Primero: conteo de los turnos del día lunes
    ocupados_lunes = 0
    if lunes1 != "":
      ocupados_lunes = ocupados_lunes + 1
    if lunes2 != "":
      ocupados_lunes = ocupados_lunes + 1
    if lunes3 != "":
      ocupados_lunes = ocupados_lunes + 1
    if lunes4 != "":
      ocupados_lunes = ocupados_lunes + 1

    #Segundo: conteo de los turnos del día martes
    ocupados_martes = 0
    if martes1 != "":
      ocupados_martes = ocupados_martes + 1
    if martes2 != "":
      ocupados_martes = ocupados_martes + 1
    if martes3 != "":
      ocupados_martes = ocupados_martes + 1

    #Tercero: calculo de los espacios libres
    libres_lunes = 4 - ocupados_lunes
    libres_martes = 3 - ocupados_martes

    #Cuarto: Mostrar el informe por pantalla
    print("\nResumen General de la Agenda")
    print("Lunes: " + str(ocupados_lunes) + " ocupados / " + str(libres_lunes) + " libres.")
    print("Martes: " + str(ocupados_martes) + " ocupados / " + str(libres_martes) + " libres.")

    #Quinto: Comparación para determinar que día tiene más turnos (lunes o martes)
    if ocupados_lunes > ocupados_martes:
      print("Resultado: El lunes tiene más turnos ocupados.")
    else:
      if ocupados_martes > ocupados_lunes:
        print("Resultado: El martes tiene más turnos ocupados.")
      else:
        print("Resultado: Ambos días tienen la misma cantidad (¡Es un empate!)")

  elif opcion == "5":
    print(f"Sistema cerrado. Hasta pronto {operador}.")
  else:
    print("Opción inválida. Por favor, seleccione un número del 1 al 5.")


#Ejercicio 4: Escape Room: La Bóveda

#Variables Iniciales (No se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

#Nombre del agente
print("ESCAPE ROOM: LA BÓVEDA")
agente = input("Nombre del agente: ")
while not agente.isalpha():
  agente = input("Solo letras, sin espacios: ")

print(f"\nBienvenido, agente {agente}. Tienes energia={energia}, tiempo={tiempo} y 3 cerraduras que abrir.")

#Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <=3):

    print(f"\nESTADO")
    print(f" Energía: {energia}/100")
    print(f"Tiempo restante: {tiempo}")
    print(f"Cerraduras : {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Apagada'}")
    print(f"Código parcial: {codigo_parcial} (len={len(codigo_parcial)})")

    print("\n 1. Forzar cerradura (-20 energia, -2 tiempo)")
    print(" 2. Hackear panel (-10 energía, -3 tiempo)")
    print(" 3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Ingrese 1, 2 o 3: ")
    opcion = int(opcion)

    # OPCIÓN 1-Forzar cerradura
    if opcion == 1:
            energia -= 20
            tiempo -= 2
            forzar_seguidas += 1
            if forzar_seguidas >= 3:
                alarma = True
                forzar_seguidas = 0
                print("¡La cerradura se trabó! La alarma se activó automáticamente.")
            else:
                if energia < 40:
                    print(f"Riesgo de alarma: energía baja ({energia}). Elegí un número:")
                    riesgo = input("Número del 1 al 3: ")
                    while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                        riesgo = input("Ingrese 1, 2 o 3: ")
                    if int(riesgo) == 3:
                        alarma = True
                        print("¡Alarma activada! Mala suerte, agente.")
                    else:
                        cerraduras_abiertas += 1
                        print(f"Cerradura {cerraduras_abiertas} abierta. Bien hecho.")
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura {cerraduras_abiertas} abierta con éxito.")

        # OPCIÓN 2-Hackear panel
    elif opcion == 2:
            forzar_seguidas = 0
            energia -= 10
            tiempo -= 3
            print("Hackeando panel....")
            for paso in range(1, 5):
                codigo_parcial += "A"
                print(f"Paso {paso}/4 - código parcial: '{codigo_parcial}'")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f"Código completo. Cerradura {cerraduras_abiertas} abierta.")

        # OPCIÓN 3-Descansar (AHORA ALINEADA CON EL IF INICIAL)
    elif opcion == 3:
            forzar_seguidas = 0
            energia += 15
            tiempo -= 1
            if alarma:
                energia -= 10
                print("Descanso interrumpido por la alarma.")
            if energia > 100:
                energia = 100
            print(f"Descansaste. Su energia ahora es: {energia}.")

        # --- CHEQUEO DE BLOQUEO (DENTRO DEL WHILE) ---
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡BLOQUEO! La alarma se activó por el poco tiempo restante. Bóveda sellada.")
        break


#Condiciones de Fin
if cerraduras_abiertas == 3:
  print(f"VICTORIA - La bóveda está abierta, agente {agente}. MISIÓN CUMPLIDA.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
  print(f"DERROTA - BLOQUEO: La alarma activa con poco tiempo. Se selló la bóveda.")
elif energia <= 0:
  print(f"DERROTA - Agotamiento. El agente {agente} no puede continuar.")
elif tiempo <= 0:
  print(f"DERROTA - Tiempo agotado. Los refuerzos han llegado.")

print(f"ESTADO FINAL: Energia={energia} | Tiempo={tiempo} | Cerraduras={cerraduras_abiertas}/3")
print("="*30)


#Ejercicio 5: ESCAPE ROOM - La Arena del Gladiador
#PASO 1: Configuración del personaje
print("---LA ARENA DEL GLADIADOR---")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

#PASO 2: Inicialización de estadísticas (iniciarlas sin preguntar al usuario)
vida_jugador: int = 100
vida_enemigo: int = 100
pociones_de_vida: int = 3
daño_ataque_pesado: int = 15
daño_enemigo: int = 12
turno_gladiador: bool = True #Turno del jugador

print(f"\n¡La arena te da la bienvenida, {nombre}! ¡Que comience el combate!")

#PASO 3: El Ciclo de Combate
while vida_jugador > 0 and vida_enemigo > 0:

    #Se muestra el estado de los combatientes
    print("-" * 30)
    print(f"ESTADO: {nombre} (vida jugador: {vida_jugador}) | Vida enemigo: {vida_enemigo}")
    print(f"Pociones de vida: {pociones_de_vida}")
    print("-" * 30)

    #Menú de opciones para el usuario
    print("1. Ataque pesado")
    print("2. Ráfaga veloz (for)")
    print("3. Curar")

    opcion = input("Seleccione una opción: ")

    #Validación del menú (teniendo en cuenta isdigit() y rango 1-3)
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido (1, 2, o 3).")
        opcion = input("Seleccione su acción:")

    #Convertir la "opción" a entero para que siga la lógica de acciones
    opcion = int(opcion)

        #Lógica de las acciones del jugador
    if opcion == 1:
        #Acción A: Ataque pesado con golpe crítico
        daño_final = float(daño_ataque_pesado)
        if vida_enemigo < 20:
            daño_final = daño_ataque_pesado * 1.5 #Multiplicación float
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(daño_final)
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
    elif opcion == 2:
        #Acción B: Ráfaga Veloz
        print(f"{nombre} lanza una ráfaga de golpes: ")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        #Acción C: Curar
        if pociones_de_vida > 0:
            vida_jugador += 30
            pociones_de_vida -= 1
            if vida_jugador > 100:
                vida_jugador = 100 #Límite de vida
            print(f"¡Te has curado! Vida actual: {vida_jugador}")
        else:
            print("¡No te quedan pociones! Has perdido el turno intentando buscar una.")

#Turno del enemigo de atacar
#Solo ataca si el enemigo sigue vivo después del turno del jugador
    if vida_enemigo > 0:
        vida_jugador -= daño_enemigo
        print(f"¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

#PASO 4: FIN DEL JUEGO
print("\n" + "="*30)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ¡has ganado la batalla!")
else:
    print("DERROTA. Has caído en combate.")
print("="*30)


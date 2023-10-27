#python 3.7.1
import random, time, sys

#--INICIALIZACIÓN--

mi_mano = []
mano_enemigo = [] 
opciones = ["Reina(7)", "Principe(5)", "Caballero(3)", "Campesino(1)"]

#--FUNCIONES--
  
def mostrar_mano(mi_mano):
  print("--TU MANO--")
  cartas = 0
  while cartas < len(mi_mano):
    print(mi_mano[cartas])
    cartas += 1

def mostrar_campo(mi_campo, campo_enemigo):
  print("\n--TU CAMPO--")
  cartas = 0
  while cartas < len(mi_campo):
    print(mi_campo[cartas])
    cartas += 1
  print("\n--CAMPO ENEMIGO--")
  cartas = 0
  while cartas < len(campo_enemigo):
    print(campo_enemigo[cartas])
    cartas += 1

def mostrar_puntos(mi_punto, puntos_enemigos):
  print("\n--INFORMACIÓN DEL JUEGO--")
  print("Tus puntos ->", mi_punto)
  print("Puntos enemigos ->", puntos_enemigos)

  
def juego():
  #--INICIALIZACIÓN DE VARIABLES DENTRO DE LA FUNCIÓN--
  cartas = 0
  ronda = 0
  mi_campo = []
  campo_enemigo = []
  mi_punto = 0
  puntos_enemigos = 0
  mis_kills = 6
  kills_enemigas = 6
  
  #--GENERANDO MANOS--
  while cartas < 3:
    mi_mano.append(random.choice(opciones))
    mano_enemigo.append(random.choice(opciones))
    cartas += 1
  mostrar_mano(mi_mano)
  
  #--EMPEZANDO BUCLE DEL JUEGO--
  while ronda <= 15:
    print("--------------------------")
    opc = input("Quieres lanzar carta(1) o matar carta(2) >> ")
    print("--------------------------")
    
    if opc == "1" and len(mi_campo) < 6:
      print("Elige tu carta a lanzar... ")
      lanzar_micarta = str(input(">> "))
      if lanzar_micarta == "campesino":
        mi_punto += 1
        jugar_mano(mi_mano, mano_enemigo, "Campesino(1)", mi_punto, ronda, mi_campo, campo_enemigo, puntos_enemigos)
      elif lanzar_micarta == "caballero":
        mi_punto += 3
        jugar_mano(mi_mano, mano_enemigo, "Caballero(3)", mi_punto, ronda, mi_campo, campo_enemigo, puntos_enemigos)
      elif lanzar_micarta == "principe":
        mi_punto += 5
        jugar_mano(mi_mano, mano_enemigo, "Principe(5)", mi_punto, ronda, mi_campo, campo_enemigo, puntos_enemigos)
      elif lanzar_micarta == "reina":
        mi_punto += 7
        jugar_mano(mi_mano, mano_enemigo, "Reina(7)", mi_punto, ronda, mi_campo, campo_enemigo, puntos_enemigos)
    
    elif opc == "2":
      mis_kills -= 1
      print("Elige una carta para matar...")
      matar_carta = str(input(">> "))
      print("Elige una carta para sacrificar...") 
      sacrificar_carta = str(input(">> "))
      if sacrificar_carta.lower() == "reina":
        mi_punto -= 7

        if matar_carta == "reina":
          puntos_enemigos -= 7
          matar_carta = "Reina(7)"
        elif matar_carta == "principe":
          puntos_enemigos -= 5
          matar_carta = "Principe(5)"
        elif matar_carta == "caballero":
          puntos_enemigos -= 3
          matar_carta = "Caballero(3)"
        elif matar_carta == "campesino":
          puntos_enemigos -= 1
          matar_carta = "Campesino(1)"
        else:
           print("\nERROR - Esta carta no se puede elegir - SOLO PUEDES ELEGIR LAS CARTAS CON RANGO IGUAL O INFERIOR")
        
        for i in range(len(campo_enemigo)):
          if campo_enemigo[i] == matar_carta:
            campo_enemigo.pop(i)
            break
        for j in range(len(mi_campo)):
          if mi_campo[j] == "Reina(7)":
            mi_campo.pop(j)
            break

      elif sacrificar_carta.lower() == "principe" and matar_carta.lower() != "reina":
       mi_punto -= 5
       if matar_carta == "principe":
          puntos_enemigos -= 5
          matar_carta = "Principe(5)"
       elif matar_carta == "caballero":
          puntos_enemigos -= 3
          matar_carta = "Caballero(3)"
       elif matar_carta == "campesino":
          puntos_enemigos -= 1
          matar_carta = "Campesino(1)"
       else:
           print("\nERROR - Esta carta no se puede elegir - SOLO PUEDES ELEGIR LAS CARTAS CON RANGO IGUAL O INFERIOR")
           
        
       for i in range(len(campo_enemigo)):
          if campo_enemigo[i] == matar_carta:
            campo_enemigo.pop(i)
            break
       for j in range(len(mi_campo)):
          if mi_campo[j] == "Principe(5)":
            mi_campo.pop(j)
            break
      
      elif sacrificar_carta.lower() == "caballero" and matar_carta.lower() != "reina" and matar_carta.lower() != "principe":
        mi_punto -= 3

        if matar_carta == "caballero":
          puntos_enemigos -= 3
          matar_carta = "Caballero(3)"
        elif matar_carta == "campesino":
          puntos_enemigos -= 1
          matar_carta == "Campesino(1)"
        else:
           print("\nERROR - Esta carta no se puede elegir - SOLO PUEDES ELEGIR LAS CARTAS CON RANGO IGUAL O INFERIOR")
        
        for i in range(len(campo_enemigo)):
          if campo_enemigo[i] == matar_carta:
            campo_enemigo.pop(i)
            break
        for j in range(len(mi_campo)):
          if mi_campo[j] == "Caballero(3)":
            mi_campo.pop(j)
            break
      elif sacrificar_carta.lower() == "campesino" and matar_carta.lower() == "campesino":
        mi_punto -= 1
        puntos_enemigos -= 1
        
        if sacrificar_carta.lower() != "campesino" or matar_carta.lower() != "campesino":
            print("ERROR - Esta carta no se puede elegir - LEER REGLAS")

        for i in range(len(campo_enemigo)):
          if campo_enemigo[i] == "Campesino(1)":
            campo_enemigo.pop(i)
            break
        for j in range(len(mi_campo)):
          if mi_campo[j] == "Campesino(1)":
            mi_campo.pop(j)
            break
      else:
           print("\nERROR - Esta carta no se puede elegir - SOLO PUEDES ELEGIR LAS CARTAS CON RANGO IGUAL O INFERIOR")
         
      
    #--TURNO ENEMIGO(IA)--
    carta_lanzada = False
    if len(campo_enemigo) < 6 and len(mi_campo) > 0:
      print("\n=====================") 
      print("TURNO ENEMIGO")
      print("=====================\n") 
      
      #--ANALIZA LA MANO Y SACA SU CARTA MAS ALTA
      time.sleep(1.5)
      for i in range(len(mano_enemigo)):
        if mano_enemigo[i] == "Reina(7)":
          campo_enemigo.append(mano_enemigo[i])
          mano_enemigo.pop(i)
          puntos_enemigos += 7
          carta_lanzada = True
          break
      if carta_lanzada == False:
        for i in range(len(mano_enemigo)):
          if mano_enemigo[i] == "Principe(5)":
            campo_enemigo.append(mano_enemigo[i])
            mano_enemigo.pop(i)
            puntos_enemigos += 5
            carta_lanzada = True
            break
        if carta_lanzada == False:
          for i in range(len(mano_enemigo)):
            if mano_enemigo[i] == "Caballero(3)":
              campo_enemigo.append(mano_enemigo[i])
              mano_enemigo.pop(i)
              puntos_enemigos += 3
              carta_lanzada = True
              break
          if carta_lanzada == False:
            for i in range(len(mano_enemigo)):
              if mano_enemigo[i] == "Campesino(1)":
                campo_enemigo.append(mano_enemigo[i])
                mano_enemigo.pop(i)
                puntos_enemigos += 1
                carta_lanzada = True
                break
    else:
      #--SI SU CAMPO ESTA LLENO Y EN MI CAMPO HAY ALGUNA CARTA--
      #--POR CADA BUCLE COMPRUEBA QUE PUEDE MATAR UNA CARTA A CAMBIO DE SACRIFICAR UNA SUYA, SI TENEMOS LAS CARTAS NECESARIAS EJECUTARÁ LA ACCIÓN
      carta_sacrificada = False
      kills_enemigas -= 1
      for elemento in range(len(campo_enemigo)):
          if campo_enemigo[elemento] == "Campesino(1)":
              for mi_elemento in range(len(mi_campo)):
                  if mi_campo[mi_elemento] == "Campesino(1)":
                      mi_campo.pop(mi_elemento)
                      mi_punto -= 1
                      campo_enemigo.pop(elemento)
                      puntos_enemigos -= 1
                      carta_sacrificada = True
                      break
              break
      if carta_sacrificada == False:    
        for elemento in range(len(campo_enemigo)):
            if campo_enemigo[elemento] == "Caballero(3)":
                for mi_elemento in range(len(mi_campo)):
                    if mi_campo[mi_elemento] == "Campesino(1)":
                        mi_campo.pop(mi_elemento)
                        mi_punto -= 1
                        campo_enemigo.pop(elemento)
                        puntos_enemigos -= 3
                        carta_sacrificada = True
                        break
                    elif mi_campo[mi_elemento] == "Caballero(3)":
                        mi_campo.pop(mi_elemento)
                        mi_punto -= 3
                        campo_enemigo.pop(elemento)
                        puntos_enemigos -= 3
                        carta_sacrificada = True
                        break
                break
        if carta_sacrificada == False:  
          for elemento in range(len(campo_enemigo)):
              if campo_enemigo[elemento] == "Principe(5)":
                  for mi_elemento in range(len(mi_campo)):
                      if mi_campo[mi_elemento] == "Campesino(1)":
                          mi_campo.pop(mi_elemento)
                          mi_punto -= 1
                          campo_enemigo.pop(elemento)
                          puntos_enemigos -= 5
                          carta_sacrificada = True
                          break
                      elif mi_campo[mi_elemento] == "Caballero(3)":
                          mi_campo.pop(mi_elemento)
                          mi_punto -= 3
                          campo_enemigo.pop(elemento)
                          puntos_enemigos -= 5
                          carta_sacrificada = True
                          break
                      elif mi_campo[mi_elemento] == "Principe(5)":
                          mi_campo.pop(mi_elemento)
                          mi_punto -= 5
                          campo_enemigo.pop(elemento)
                          puntos_enemigos -= 5
                          carta_sacrificada = True
                          break
                  break
          if carta_sacrificada == False:
            for elemento in range(len(campo_enemigo)):
                if campo_enemigo[elemento] == "Reina(7)":
                    for mi_elemento in range(len(mi_campo)):
                        if mi_campo[mi_elemento] == "Campesino(1)":
                            mi_campo.pop(mi_elemento)
                            mi_punto -= 1
                            campo_enemigo.pop(elemento)
                            puntos_enemigos -= 7
                            carta_sacrificada = True
                            break
                        elif mi_campo[mi_elemento] == "Caballero(3)":
                            mi_campo.pop(mi_elemento)
                            mi_punto -= 3
                            campo_enemigo.pop(elemento)
                            puntos_enemigos -= 7
                            carta_sacrificada = True
                            break
                        elif mi_campo[mi_elemento] == "Principe(5)":
                            mi_campo.pop(mi_elemento)
                            mi_punto -= 5
                            campo_enemigo.pop(elemento)
                            puntos_enemigos -= 7
                            carta_sacrificada = True
                            break
                        elif mi_campo[mi_elemento] == "Reina(7)":
                            mi_campo.pop(mi_elemento)
                            mi_punto -= 7
                            campo_enemigo.pop(elemento)
                            puntos_enemigos -= 7
                            carta_sacrificada = True
                            break
                    break

    #--SE MUESTRA LA INFORMACIÓN AL FINAL DE CADA RONDA SOLO SI SE ELIJE UNA OPCIÓN CORRECTA--
    if opc == "1" or opc == "2": 
      mostrar_mano(mi_mano)
      mostrar_campo(mi_campo, campo_enemigo)  
      mostrar_puntos(mi_punto, puntos_enemigos)
      print("Puedes matar a", mis_kills, "cartas enemigas")         
      print("El enemigo puede matar a", kills_enemigas, "cartas aliadas")         
      print("RONDA", ronda)   
      print("=====================\n")

      ronda += 1
      if len(mi_mano) < 3 and ronda < 15:
        carta_robada = random.choice(opciones)
        mi_mano.append(carta_robada)
        print("--------------------------")
        print("CARTA ROBADA ESTE TURNO -->", carta_robada)
      elif len(mi_mano) >= 3 and ronda < 15:
          print("--------------------------")
          print("MANO LLENA")
      if len(mano_enemigo) < 3 and ronda < 15:
        mano_enemigo.append(random.choice(opciones))
        time.sleep(1)
      elif len(mano_enemigo) >= 3 and ronda < 15:
          print("--------------------------")
          print("EL ENEMIGO TIENE LA MANO LLENA")
      ganador(puntos_enemigos, mi_punto, ronda)
    
#--COMPRUEBA QUIEN ES EL GANADOR--
def ganador(puntos_enemigos, mi_punto, ronda):
    if ronda >= 16:
        if mi_punto > puntos_enemigos:
            print("\n\n ¡¡¡GANASTE!!!")
        elif puntos_enemigos > mi_punto:
            print("\n\n PERDISTE :C")
        else:
            print("EMPATE...")
    else:
        pass

#--LANZAS LA CARTA DE TU MANO--
def jugar_mano(mi_mano, mano_enemigo, nom, mi_punto, ronda, mi_campo, campo_enemigo, puntos_enemigos):
  
  for index in range(len(mi_mano)):
    if mi_mano[index] == nom:    
      mi_campo.append(mi_mano[index])
      mi_mano.pop(index)
      break
     
def menu():
  print(""" 
  + - - - - - +
  |    MENÚ   |
  + - - - - - +
  
  1) Jugar
  2) Como jugar
  3) Salir
  """)
 
menu()
opc = int(input(">> "))


#--OPCIONES--

if opc == 1:
  juego()
  
elif opc == 2:
  print("""
  Cuando acabe el juego, quien tenga más puntos ganará, 
  los puntos se consiguen lanzando las cartas de tu mano, 
  empiezas con 6 cartas y hay 4 tipos de cartas, 
  reina, príncipe, caballero, campesino (estan ordenadas de mayor a menor rango)
 
  1) Hay 15 rondas
  2) Al empezar el juego cada jugador tiene 3 cartas en mano
  3) Reina(7pts) príncipe(5pts) caballero(3pts) campesino(1pt)
  4) Cada turno robas una carta
  5) Puedes tener hasta un tope de 3 cartas en mano y 6 cartas en tu campo 
  6) Puedes sacrificar cartas lanzadas para matar cartas lanzadas del enemigo
  7) Las cartas que puedes matar tiene que ser del mismo rango o inferior
  8) Puedes matar cartas enemigas sacrificando tus cartas hasta un tope de 6 veces
  
  """)
else:
  pass

# Tu implementacion va aqui
import random

def tirar_dados(cantidad):
    tirada = []
    for i in range(cantidad):
        dado = random.randint(1, 6)
        tirada.append(dado)
    return tirada

def calcular_puntos(categoria, dados, tiro):
    # Categorias de numeros
    if categoria == "1":
        return dados.count(1) * 1
    elif categoria == "2":
        return dados.count(2) * 2
    elif categoria == "3":
        return dados.count(3) * 3
    elif categoria == "4":
        return dados.count(4) * 4
    elif categoria == "5":
        return dados.count(5) * 5
    elif categoria == "6":
        return dados.count(6) * 6
    
    # Generala (5 iguales)
    elif categoria == "G":
        if dados.count(dados[0]) == 5:
            return 50
        return 0
    
    # Generala Doble
    elif categoria == "GD":
        if dados.count(dados[0]) == 5:
            return 60
        return 0
        
    # Poker (4 iguales)
    elif categoria == "P":
        for dado in dados:
            if dados.count(dado) >= 4:
                puntos = 40
                if tiro == 1:
                    puntos = puntos + 5 # Bonificacion
                return puntos
        return 0
        
    # Full (3 y 2)
    elif categoria == "F":
        hay_tres = False
        hay_dos = False
        for dado in dados:
            if dados.count(dado) == 3:
                hay_tres = True
            if dados.count(dado) == 2:
                hay_dos = True
        
        if hay_tres == True and hay_dos == True:
            puntos = 30
            if tiro == 1:
                puntos = puntos + 5
            return puntos
        return 0
        
    # Escalera
    elif categoria == "E":
        tiene_1 = dados.count(1) >= 1
        tiene_2 = dados.count(2) >= 1
        tiene_3 = dados.count(3) >= 1
        tiene_4 = dados.count(4) >= 1
        tiene_5 = dados.count(5) >= 1
        tiene_6 = dados.count(6) >= 1
        
        escalera_baja = tiene_1 and tiene_2 and tiene_3 and tiene_4 and tiene_5
        escalera_alta = tiene_2 and tiene_3 and tiene_4 and tiene_5 and tiene_6
        escalera_al_rincon = tiene_1 and tiene_3 and tiene_4 and tiene_5 and tiene_6
        
        if escalera_baja == True or escalera_alta == True or escalera_al_rincon == True:
            puntos = 20
            if tiro == 1:
                puntos = puntos + 5
            return puntos
        return 0
        
    # Si eligio la categoria y no armo nada, tacha con cero
    return 0

def guardar_csv(planilla_j1, planilla_j2):

    archivo = open('jugadas.csv', 'w')
    archivo.write("jugada,j1,j2\n")
    
    categorias = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G", "GD"]
    for cat in categorias:
        puntos_1 = planilla_j1[cat]
        if puntos_1 == None:
            puntos_1 = 0
            
        puntos_2 = planilla_j2[cat]
        if puntos_2 == None:
            puntos_2 = 0
            
        linea = cat + "," + str(puntos_1) + "," + str(puntos_2) + "\n"
        archivo.write(linea)
    
    archivo.close()

def turno_jugador(nombre):
    print("\n--- Turno de", nombre, "---")
    dados_guardados = []
    
    for tiro in range(1, 4):
        cantidad = 5 - len(dados_guardados)
        if cantidad > 0:
            dados_nuevos = tirar_dados(cantidad)
        else:
            dados_nuevos = []
            
        mesa = dados_guardados + dados_nuevos
        print("Tiro", tiro, ":", mesa)
        
        # Generala Real (gana el juego)
        if tiro == 1 and mesa.count(mesa[0]) == 5:
            print("¡Generala Real servida!")
            return mesa, tiro, True 
            
        if tiro == 3:
            return mesa, tiro, False
            
        respuesta = input("¿Te plantas con estos dados? (si/no): ")
        if respuesta == "si" or respuesta == "SI":
            return mesa, tiro, False
        
        print("Para elegir qué dados guardar:")
        cuantos = int(input("¿Cuántos dados te querés guardar? (0 a 5): "))
        dados_guardados = []
        
        if cuantos > 0:
            for i in range(cuantos):
                valor = int(input("Ingresá el valor de un dado que querés guardar: "))
                dados_guardados.append(valor)
                
    return mesa, 3, False

def main():
    print("¡Arranca la Generala!")
    
    planilla_j1 = {"1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "E": None, "F": None, "P": None, "G": None, "GD": None}
    planilla_j2 = {"1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "E": None, "F": None, "P": None, "G": None, "GD": None}
    
    for ronda in range(11):
        print("\n*** RONDA", ronda + 1, "***")
        
        # --- JUGADOR 1 ---
        mesa_j1, tiro_j1, gano_j1 = turno_jugador("Jugador 1")
        if gano_j1 == True:
            planilla_j1["G"] = 80
            guardar_csv(planilla_j1, planilla_j2)
            print("¡JUGADOR 1 GANA AUTOMATICAMENTE!")
            return
            
        while True:
            print("Tus dados finales:", mesa_j1)
            print("Tu Planilla:", planilla_j1)
            eleccion = input("Jugador 1, elige categoria en MAYUSCULAS (ej: E, F, P, 1): ")
            
            if eleccion in planilla_j1 and planilla_j1[eleccion] == None:
                puntos = calcular_puntos(eleccion, mesa_j1, tiro_j1)
                planilla_j1[eleccion] = puntos
                print("Anotaste", puntos, "puntos.")
                break
            else:
                print("Error: Escribiste mal o ya usaste esa categoria.")
        
        guardar_csv(planilla_j1, planilla_j2)
        
        # --- JUGADOR 2 ---
        mesa_j2, tiro_j2, gano_j2 = turno_jugador("Jugador 2")
        if gano_j2 == True:
            planilla_j2["G"] = 80
            guardar_csv(planilla_j1, planilla_j2)
            print("¡JUGADOR 2 GANA AUTOMATICAMENTE!")
            return
            
        while True:
            print("Tus dados finales:", mesa_j2)
            print("Tu Planilla:", planilla_j2)
            eleccion = input("Jugador 2, elige categoria en MAYUSCULAS (ej: E, F, P, 1): ")
            
            if eleccion in planilla_j2 and planilla_j2[eleccion] == None:
                puntos = calcular_puntos(eleccion, mesa_j2, tiro_j2)
                planilla_j2[eleccion] = puntos
                print("Anotaste", puntos, "puntos.")
                break
            else:
                print("Error: Escribiste mal o ya usaste esa categoria.")
                
        guardar_csv(planilla_j1, planilla_j2)
        
    # Sumar puntos al final
    print("\n--- FIN DEL JUEGO ---")
    total_1 = 0
    for p in planilla_j1.values():
        if p != None:
            total_1 = total_1 + p
            
    total_2 = 0
    for p in planilla_j2.values():
        if p != None:
            total_2 = total_2 + p
            
    print("Puntos J1:", total_1)
    print("Puntos J2:", total_2)
    
    if total_1 > total_2:
        print("GANA EL JUGADOR 1")
    elif total_2 > total_1:
        print("GANA EL JUGADOR 2")
    else:
        print("EMPATE")

if __name__ == "__main__":
    main()
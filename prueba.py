# Tu implementacion va aqui
import random

def hola_mundo():
    return "hola_mundo"


def main():
    # Aqui ejecutas tus soluciones

    planilla_j1 = {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
        "E": None, "F": None, "P": None, "G": None
    }
    planilla_j2 = {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
        "E": None, "F": None, "P": None, "G": None
    }

def turnos_jugador():
    dados_guardados = []
    cantidad_a_tirar = 5 - len(dados_guardados)
    for tiro in range(3):
        tirar_dados(5)

    return
        
    

def tirar_dados(cantidad):
    tirada = []
    for i in range (cantidad):
        dado = random.randint(1, 6)
        tirada.append(dado)
    return tirada


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

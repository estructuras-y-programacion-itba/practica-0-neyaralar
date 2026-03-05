# Tu implementacion va aqui
import random

def hola_mundo():
    return "hola_mundo"


def main():
    # Aqui ejecutas tus soluciones
    print(tirar_dados(5))

def tirar_dados(cantidad):
    tirada = []
    for i in range (cantidad):
        dado = random.randint(1, 6)
        tirada.append(dado)
    return tirada



# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

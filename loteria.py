1#Realizar un juego de loteria donde digitara una puesta con un saldo de 500 el cual se restara a su saldo actual y lo iras sumando//
#Si el numero de la loteria es mayor a 50 ganas y si es menor perderas. Cuando estes en 0 perderas y en 1000 ganaras// 
import random

def jugar_loteria(saldo):
    apuesta = int(input("Ingresa el monto que deseas apostar: "))
    
    if apuesta > saldo:
        print("No tienes suficiente saldo disponible")
        return saldo
    
    numero_loteria = random.randint(1, 100)
    saldo -= apuesta
    
    if numero_loteria > 50:
        saldo += apuesta * 2
        print("¡Felicidades! Ganaste el doble de tu apuesta. Tu saldo actual es de", saldo)
    else:
        print("Lo siento, perdiste. Tu saldo actual es de", saldo)
    
    return saldo

def control():
    saldo = 500
    
    while saldo > 0 and saldo < 1000:
        saldo = jugar_loteria(saldo)
    
    if saldo == 0:
        print("Perdiste.")
    elif saldo == 1000:
        print("¡Felicidades! Ganaste el juego.")
    
    print("Fin del juego. Tu saldo final es de", saldo)

if __name__ == '__main__':
    control()

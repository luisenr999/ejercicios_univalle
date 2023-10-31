import os
import random
import msvcrt
import time

class tragamonedas:
    _tablero_ini = {"Cereza":0,
                   "Manzana":0, 
                   "Naranja":0, 
                   "Campana":0, 
                   "Melon":0, 
                   "Sandia":0, 
                   "Estrellas":0,
                   "77":0,
                   "Bar":0,
                   "Bar/Bar":0}
    
    _tablero = {}
    
    def __init__(self, credits) -> None:
        self._credits = credits
        if self._credits > 999:
            self._credits = 999
        elif self._credits < 0:
            self._credits = 0
        self._tablero = self._tablero_ini
    
    def get_tablero (self, win):
        print("")
        for i in range (0, 50):
            print("*", end="")
        print(f"\n\t\tCREDITOS: {self.get_credits()}{win}")
        for i in range (0, 50):
            print("*", end="")
        
        print("\n\nOpciones\t\tCreditos apostados")    
        for i in range(0, 50):
            print("-", end="")
        print("")
        cont = 0
        for key, item in self._tablero.items():
            if (key == "77"):
                print(f"({cont}){key}\t\t\t|\t{item}")
            elif (key == "Bar"):
                print(f"({cont}){key}\t\t\t|\t{item}")
            else:
                print(f"({cont}){key}\t\t|\t{item}")
            for i in range(0, 50):
                print("-", end="")
            print("")
            cont += 1

    def set_tablero(self, apuesta):
        if self._credits != 0:
            if self._tablero[f"{(list(self._tablero.keys())[apuesta])}"] < 9:
                self._tablero[f"{(list(self._tablero.keys())[apuesta])}"] += 1
                self.set_credits(-1)
            

    def set_credits(self,credits):
        self._credits += credits
        if self._credits > 999:
            self._credits = 999
        elif self._credits < 0:
            self._credits = 0
        
    def get_credits(self):
        return self._credits
    
    def confirm_bet(self)->bool:
        x = False
        for values in self._tablero.values():
            if values != 0:
                x = True
        return x
    
    def cobrar(self):
        os.system("cls")
        self.get_tablero(f"\n\t    ¡¡HAS COBRADO {self._credits} MONEDAS...!!")
        self._credits = 0
        time.sleep(4)
        os.system("cls")
        
    def get_manual():
        print("\tREGLAS DEL JUEGO Y TABLA DE PREMIOS\n\n")
        print("1. Para iniciar selecciona la opcion '1' con la misma tecla en el menu principal.\n")
        print("2. Ingrese el numero de monedas entre 1 y 999 para obtener creditos de juego.\n")
        print("3. Seleccione la opcion a la que desea añadir un credito apostado (hasta 9 por opcion).\n")
        print("4. Oprima la tecla 'Enter' para activar la ruleta o la tecla 'Esc' para cobrar los creditos en monedas (Solo si no hay apuestas vigentes.)\n")
        print("5. En caso de ganar, el valor del premio se multiplica segun lo apostado en esa opcion ganadora.\n")
        print("\tPREMIOS")
        print("\nCereza\t\t2\nManzana\t\t5\nNaranja\t\t10\nCampana\t\t15\nMelon\t\t20\nSandia\t\t25\nEstrellas\t30\n77\t\t40\nBar\t\t50\nBar/Bar\t\t100")
        print("\n\nPulse cualquier tecla para continuar...")
        x = msvcrt.getch()
    
    def roulette(self):
        x = random.randrange(1, 23,1)
        if x <= 7:
            if self._tablero["Cereza"] != 0:
                self.get_tablero(f"Sale Cereza... HAS GANADO {self._tablero['Cereza']*2} CREDITOS")
                self.set_credits(self._tablero['Cereza']*2)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Cereza... PIERDES")
                time.sleep(4)
        elif x <= 11:
            if self._tablero["Manzana"] != 0:
                self.get_tablero(f"\n\t    Sale Manzana... HAS GANADO {self._tablero['Manzana']*5} CREDITOS")
                self.set_credits(self._tablero['Manzana']*5)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Manzana... PIERDES")
                time.sleep(4)
        elif x <= 13:
            if self._tablero["Naranja"] != 0:
                self.get_tablero(f"\n\t    Sale Naranja... HAS GANADO {self._tablero['Naranja']*10} CREDITOS")
                self.set_credits(self._tablero['Naranja']*10)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Naranja... PIERDES")
                time.sleep(4)
        elif x <= 15:
            if self._tablero["Campana"] != 0:
                self.get_tablero(f"\n\t    Sale Campana... HAS GANADO {self._tablero['Campana']*15} CREDITOS")
                self.set_credits(self._tablero['Campana']*15)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Campana... PIERDES")
                time.sleep(4)
        elif x <= 17:
            if self._tablero["Melon"] != 0:
                self.get_tablero(f"\n\t    Sale Melon... HAS GANADO {self._tablero['Melon']*20} CREDITOS")
                self.set_credits(self._tablero['Melon']*20)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Melon... PIERDES")
                time.sleep(4)
        elif x == 18:
            if self._tablero["Sandia"] != 0:
                self.get_tablero(f"\n\t    Sale Sandia... HAS GANADO {self._tablero['Sandia']*25} CREDITOS")
                self.set_credits(self._tablero['Sandia']*25)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Sandia... PIERDES")
                time.sleep(4)
        elif x == 19:
            if self._tablero["Estrellas"] != 0:
                self.get_tablero(f"\n\t    Sale Estrellas... HAS GANADO {self._tablero['Estrellas']*30} CREDITOS")
                self.set_credits(self._tablero['Melon']*30)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Estrellas... PIERDES")
                time.sleep(4)
        elif x == 20:
            if self._tablero["77"] != 0:
                self.get_tablero(f"\n\t    Sale 77... HAS GANADO {self._tablero['77']*40} CREDITOS")
                self.set_credits(self._tablero['77']*40)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale 77... PIERDES")
                time.sleep(4)
        elif x == 21:
            if self._tablero["Bar"] != 0:
                self.get_tablero(f"\n\t    Sale Bar... HAS GANADO {self._tablero['Bar']*50} CREDITOS")
                self.set_credits(self._tablero['Melon']*50)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Bar... PIERDES")
                time.sleep(4)
        else:
            if self._tablero["Bar/Bar"] != 0:
                self.get_tablero(f"\n\t    Sale Bar/Bar... HAS GANADO {self._tablero['Bar/Bar']*100} CREDITOS")
                self.set_credits(self._tablero['Melon']*100)
                time.sleep(4)
            else:
                self.get_tablero("\n\t    Sale Bar/Bar... PIERDES")
                time.sleep(4)
        


def game ():
    while True:    
        print("\nBIENVENIDO AL JUEGO DE TRAGAMONEDAS\n")
        print("Elija una opcion:\n\n1. Jugar\n2. Leer instrucciones\n3. Salir\n")
        opc = msvcrt.getch()
        if opc == b'1':
            os.system("cls")
            credits = int(input("¿Cuantas monedas va a ingresar? (1-999) "))
            if isinstance(credits, int) and credits > 0:
                player = tragamonedas(credits)
                while True:
                    os.system("cls")
                    if player._credits != 0:
                        player.get_tablero("")
                    elif player._credits == 0 and player.confirm_bet():
                        player.get_tablero("\n\t    ¡¡¡NO POSEE CREDITOS!!!")
                    elif player._credits == 0 and not player.confirm_bet():
                        player.get_tablero("\n\t    ¡¡¡HA TERMINADO EL JUEGO!!!")
                        time.sleep(4)
                        os.system("cls")
                        break                      
                    print("Pulse los valores que quiere apostar (0-9), pulse 'enter' para iniciar o 'esc' para cobrar y salir...")
                    apuesta = msvcrt.getch()
                    if (str(apuesta))[2].isdigit():
                        player.set_tablero(int(str(apuesta)[2]))
                    elif(apuesta == b'\r'):
                        player.roulette()
                        os.system("cls")
                        for key in player._tablero.keys():
                            player._tablero[key] = 0
                    elif(apuesta == b'\x1b'):
                        if player.confirm_bet(): 
                            player.get_tablero("\n\t    HAY UN JUEGO EN CURSO")
                            time.sleep(4)
                        else:
                            player.cobrar()
                            break
            else:
                print("Cantidad de monedas no valida...")
                time.sleep(3)
                os.system("cls")
        elif opc == b'2': 
            os.system("cls")               
            tragamonedas.get_manual()
            os.system("cls") 
        elif opc == b'3':
            break                
                     
game()

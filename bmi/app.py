import os
import platform
from imc import Imc
import sys
from pprint import pprint

def clear_screem():
    operation_system = platform.system()
    if operation_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def data_input():
    try:
        weight = float(input('Peso(kg)....:').replace(',','.'))
        height = float(input('Altura(cm)..:').replace(',','.'))
    except:
        clear_screem()
        print('Insira apenas números!')
        sys.exit()
    return weight,height
    

if __name__ == '__main__':
    clear_screem()
    print('Calculo IMC')
    print(20* '-')
    weight, height = data_input()
    imc = Imc(weight, height)
    
    result = imc.calculate_bmi()
   
    clear_screem()
    print(50* '-')
    print(f"IMC: {round(result['bmi'],1)} | Classificação: {result['classification'].capitalize()}")
    print(50* '-')
    
    
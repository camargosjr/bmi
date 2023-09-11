import os
import platform
import sys

from imc import Imc


def clear_screem():
    frutas = [
        'laranja',
        'abacaxi',
        'maçã',
        'melancia',
        'pera',
        'uva',
        'mexirica',
    ]

    operation_system = platform.system()
    if operation_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        print(frutas)


def data_input():
    try:
        weight = float(input('Peso(kg)....:').replace(',', '.'))
        height = float(input('Altura(cm)..:').replace(',', '.'))
    except Exception as err:
        clear_screem()
        print('Insira apenas números!', err)
        sys.exit()
    return weight, height


if __name__ == '__main__':
    clear_screem()
    print('Calculo IMC')
    print(20 * '-')
    weight, height = data_input()
    imc = Imc(weight, height)

    result = imc.calculate_bmi()

    clear_screem()
    print(50 * '-')
    print(
        f"IMC: {round(result['bmi'],1)} | "
        f"Classificação: {result['classification'].capitalize()} |"
    )
    print(50 * '-')

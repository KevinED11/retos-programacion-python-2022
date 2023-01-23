'''
* Crea una función que reciba un String de cualquier tipo y se encargue de
* poner en mayúscula la primera letra de cada palabra.
'''

from string import punctuation


def mayuscula(string: str) -> str:
    string = string.lower().split()

    words = [palabra.strip(punctuation).replace(
        palabra[0], palabra[0].upper()) for palabra in string]

    return ' '.join(words)


if __name__ == '__main__':
    print(mayuscula('Hola? mundo COMO estas__'))

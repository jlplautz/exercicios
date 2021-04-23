from time import time
from functools import wraps


def envolver(funcao_envolvida):
    def editar_metadados(funcao_envoltoria):
        funcao_envoltoria.__name__ = funcao_envolvida.__name__
        funcao_envoltoria.__doc__ = funcao_envolvida.__doc__
        return funcao_envoltoria

    return editar_metadados


def modificar(funcao):
    print('Trocar função original por outra')

    @wraps(funcao)
    def funcao_envoltoria(*arg, **kwargs):
        """"
        Funcao envoltoria
        """
        tempo_inicial = time()
        resultado = funcao(*arg, **kwargs)
        tempo_final = time()
        print(tempo_final - tempo_inicial)
        return resultado

    return funcao_envoltoria


@modificar
def soma(a, b):
    """"
    função soma
    """
    return a+b


print(soma(1, 2))
print(soma(1000000000, 2*1000))
print(soma.__name__)


def modulo(a, b):
    if a > b:
        return a - b
    return b - a


print(modulo(1, 2))
print(modulo(2, 1))

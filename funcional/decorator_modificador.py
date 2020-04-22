from time import time


def modificar(funcao):
    print('Trocar função original por outra')

    def funcao_modificada(*arg, **kwargs):
        tempo_inicial = time()
        resultado = funcao(*arg, **kwargs)
        tempo_final = time()
        print(tempo_final - tempo_inicial)
        return resultado
    return funcao_modificada


@modificar
def soma(a, b):
    return a+b


print(soma(1, 2))
print(soma(1000000000, 2*1000))
print(soma.__name__)

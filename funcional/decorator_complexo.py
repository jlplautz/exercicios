from functools import wraps
from time import strftime

# * define que o argunto deve ser por nome
def logar_datahora(*, formato):
    # função decoradora que receber outra função
    def decoradora(função):
        @wraps(função)
        def envoltoria(*arg, **kwargs):
            print(strftime(formato))
            return função(*arg, **kwargs)
        return envoltoria


    return decoradora

@logar_datahora(formato='%H:%m:%s')
def soma(a, b):
    """"
    função soma
    """
    return a+b

print(soma(1, 2))
print(soma(2, 3))
print(soma.__doc__)
print(soma.__name__)
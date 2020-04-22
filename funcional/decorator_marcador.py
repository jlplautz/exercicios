_funcoes_marcadas = []


def marcar(funcao):
    _funcoes_marcadas.append(funcao)
    return funcao


@marcar
def f():
    pass


# f = marcar(f)


def g():
    pass


g = marcar(g)

# list comprehension para imprimir todas as funçoes marcadas
print([f.__name__ for f in _funcoes_marcadas])
print(id(f))
print(id(g))

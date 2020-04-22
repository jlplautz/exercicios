# para transforma as fruntas em lista
frutas = 'caqui jaca uva  kiwi manga abacaxi jaboticaba mangaba'.split()


frutas.sort()
print(frutas)


# ordenar de traz para frente (criterio reverso)
# função sort é uma função de alta ordem e podemos usar uma key.


frutas = 'caqui jaca uva kiwI manga abacaxi jaboticaBA mangaba'.split()


def reverter(fruta: str):
    # print(fruta)
    fruta_reversa = ''.join(reversed(fruta)).lower()
    print(fruta_reversa)
    return fruta_reversa


frutas.sort(key=reverter)
print(frutas)

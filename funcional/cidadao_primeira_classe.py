def f():
    """
    a função é um objecto qualquer que implementa o metodo __call__
    0 metodo __call__ é usando com os print(type(f))
    :return:
    """
    pass


# anonima = lambda: 'Ola Mundo'

if __name__ == '__main__':
    print(type(f))
    # quais os atributos da função f
    print(dir(f))
    # print o nome da funçãp
    print(f.__name__)
    print(id(f))
    print(help(f))
#   print(anonima.__name__)

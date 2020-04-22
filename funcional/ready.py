def ready(funcao):
    print('Pagina carregada')
    print(funcao())
    print('Pagina Termina funcao')


# uma função anonima esta sendo passada como parametro para a função ready
# quando o evento de carregamento da tela é executada ele vai pegar todas as
# funções que foram passadas como parametro e executar.
ready(lambda: 'Ola Mundo')

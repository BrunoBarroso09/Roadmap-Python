def info(apelido, *nomes):
    print(apelido)
    print('Tipo', type(nomes))
    print(nomes[1])
    print(nomes)

info('Barroso', 'Bruno', 'Pedro', 'Carlos')
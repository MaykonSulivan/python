import os
lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indece_str = input('Escolja o índice para apagar:')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possivel apagar esse índice.')
        except IndexError:
            print('Índice não existe na lista')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('por favor digite uma das letras acima!!')
            

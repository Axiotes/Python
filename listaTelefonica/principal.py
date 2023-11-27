import listaTelefonica
dbLista = listaTelefonica.ListaTelefones(cursor = None,
                                         nome = None,
                                         numero = None)

dbLista.conectarDB()

op = 0

while op != 4:
    print('Digite 1: VER CONTATOS\n',
          'Digite 2: ADICIONAR CONTATOS\n',
          'Digite 3: REMOVER CONTATO\n',
          'Digite 4: SAIR')
    op = int(input())

    match op:
        case 1: # VER CONTATOS
            opContatos = 0

            while opContatos != 3:
                print('Digite 1: VER CONTATOS EM ORDEM ALFABETICA\n',
                      'Digite 2: VER CONTATOS RECENTES\n',
                      'Digite 3: VOLTAR')
                opContatos = int(input())

                match opContatos:
                    case 1: # ORDEM ALFABETICA
                        print(dbLista.verConatosAfabetico())

                        break
                    # Fim case 1 ORDEM ALFABETICA

                    case 2: # RECENTES
                        print(dbLista.verConatosRecente())

                        break
                    # Fim case 2 RECENTES

                    case 3: # VOLTAR
                        break
                    # VOLTAR

                    case _:
                        print('Opção inválida!')
                # Fim match opContatos
            # Fim while opContatos != 3

            break
        # Fim case 1 VER CONTATOS

        case 2: # ADICIONAR
            dbLista.nome = str(input('Digite o nome: '))
            dbLista.nome = dbLista.nome.lower()

            dbLista.numero = int(input('Digite o número: '))

            dbLista.addContato(dbLista.nome, dbLista.numero)

            print('Contato adicionado')

            break
        # Fim case 2 ADICIONAR

        case 3: # REMOVER
            dbLista.nome = str(input('Digite o nome: '))
            dbLista.nome = dbLista.nome.lower()

            dbLista.removerContato(dbLista.nome)

            print('Contato removido')

            break
        # Fim case 3 REMOVER

        case 4: # FINALIZAR PROGRAMA
            print('Programa finalizado')

            break
        # Fim case 4 FINALIZAR PROGRAMA

        case _: # OPÇÃO INVÁLIDA
            print('Opção inválida! Tente novamente')
    # Fim match op
# Fim while op != 4
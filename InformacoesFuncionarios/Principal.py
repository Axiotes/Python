import ConexaoBD

# Instância da classe BancoDeDados
bd = ConexaoBD.BancoDeDados()

# Conexão com o banco de dados
bd.conectar()

while True:
    print('Digite 1: VER TODOS OS FUNCIONÁRIOS\n',
          'Digite 2: VER FUNCIONÁRIOS DO ADMINISTRATIVO\n',
          'Digite 3: VER FUNCIONÁRIOS VENDEDORES\n',
          'Digite 4: CADASTRAR NOVO FUNCIONARIO')
    op = int(input()) # Selecionar opção

    if op == 1: # VER TODOS OS FUNCIONÁRIOS
        for x in bd.verFuncionarios():
            print(x)
    # Fim if VER TODOS OS FUNCIONÁRIOS

    if op == 2: # VER FUNCIONÁRIOS DO ADMINISTRATIVO
        for x in bd.verAdministrativo():
            print(x)
    # Fim if VER FUNCIONÁRIOS DO ADMINISTRATIVO

    if op == 3: # VER FUNCIONÁRIOS VENDEDORES
        for x in bd.verVendedores():
            print(x)
    # Fim if VER FUNCIONÁRIOS VENDEDORES

    if op == 4: # CADASTRAR FUNCIONÁRIOS
        # Informar dados do funcionário
        bd.nome = input('Digite o nome: ')
        bd.cpf = int(input('Digite o CPF: '))
        bd.gmail = input('Digite o gmail: ')

        opFuncao = 0
        
        while True: # Loop para selecionar função
            print('Digite 1: Função administrativa\n',
                'Digite 2: Função vendas')
            opFuncao = int(input())

            if opFuncao == 1:
                bd.funcao = 'ADM'
                break
            if opFuncao == 2:
                bd.funcao = 'VENDAS'
                break
            if opFuncao < 1 or opFuncao > 2:
                print('Opção inválida! Tente novamente')

        bd.salarioBase = float(input('Digite o salário base: '))

        # Calculo do imposto, inss e salário liquido
        bd.calcImposto(bd.salarioBase)
        bd.calcInss(bd.salarioBase)
        bd.calcSalarioLiquido(bd.salarioBase, bd.imposto, bd.inss)

        print(f'Salário liquido: {bd.salarioLiquido}\n',
              f'Imposto: {bd.imposto}\n',
              f'INSS: {bd.inss}\n',
              'Digite 1: CONFIRMAR CADASTRO\n',
              'Digite 2: CANCELAR CADASTRO')
        confirmar = int(input()) # Confirmar ou cancelar cadastro

        if confirmar == 1: # CONFIRMAR CADASTRO
            bd.addFuncionarios() # Adicionar informações ao banco de dados
            print('Cadastro finalizado!')
        else: # CANCELAR CADASTRO
            print('Cadastro cancelado')

    if op < 1 or op > 4: # OPÇÃO INVÁLIDA
        print('Opção inválida! Tente novamente')
# Fim while True
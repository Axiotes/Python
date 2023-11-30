import pyodbc
from Funcionarios import InfoFuncionarios

class BancoDeDados(InfoFuncionarios): # Classe BancoDeDados com herança da classe InfoFuncionarios
    # Método construtor
    def __init_subclass__(cls, cursor=None):
        cls.cursor = cursor
        return super().__init_subclass__()
    # Fim def __init_subclass__(cls, cursor=None)
    
    # Conexão com o banco de dados
    def conectar(cls):
        # Informações do banco de dados
        dados_conexao = (
            'Driver=SQL Server;'
            'Server=ARTHUR-AXIOTES;'
            'Database=funcionarios;'
        )

        # Conexão com o banco de dados
        conexao = pyodbc.connect(dados_conexao)

        cls.cursor = conexao.cursor()
    # Fim def conectar()

    # Mostrar todos os funcionários
    def verFuncionarios(cls):
        # Comando SQL
        comando = "select * from informacoes"

        return cls.cursor.execute(comando).fetchall()
    # Fim def verFuncionarios(cls)
    
    # Mostrar funcionários do administrativo
    def verAdministrativo(cls):
        # Comando SQL
        comando = """select * from informacoes
        where funcao = 'ADM'"""

        return cls.cursor.execute(comando).fetchall()
    # Fim def verAdministrativo(cls)
    
    # Mostrar funcionários vendedores
    def verVendedores(cls):
        # Comando SQL
        comando = """select * from informacoes
        where funcao = 'VENDAS'"""

        return cls.cursor.execute(comando).fetchall()
    # Fim def verVendedores(cls)
    
    # Cadastrar informações do funcionário
    def addFuncionarios(cls):
        # Comando SQL
        comando = f"""insert into informacoes
        (nome, cpf, gmail, funcao, salario_base, salario_liquido, imposto, inss)
        values
        ('{cls.nome}', {cls.cpf}, '{cls.gmail}', '{cls.funcao}', {cls.salarioBase}, {cls.salarioLiquido}, {cls.imposto}, {cls.inss})"""

        cls.cursor.execute(comando)
        cls.cursor.commit()
    # Fim def addFuncionarios(cls)

# Fim class ConectarBancoDeDados
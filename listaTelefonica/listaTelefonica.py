import pyodbc

class ListaTelefones:

    def __init__(self, cursor, nome, numero):
        self.cursor = cursor
        self.nome = nome
        self.numero = numero
    # Fim def __init__(self, cursor)

    def conectarDB(self):
        dados_conexao = (
            'Driver=SQL Server;'
            'Server=ARTHUR-AXIOTES;'
            'Database=lista_telefonica;'
        )

        conexao = pyodbc.connect(dados_conexao)

        self.cursor = conexao.cursor()
    # Fim def conectarDB(self)

    def verConatosRecente(self):
        verR = """select nome, numero from lista"""

        return self.cursor.execute(verR).fetchall()
    # Fim def verConatosRecente(self)

    def verConatosAfabetico(self):
        verA = """select nome, numero from lista
        order by nome asc"""

        return self.cursor.execute(verA).fetchall()
    # Fim def verConatosAlfabetico(self)

    def addContato(self, nome, numero):
        add = f"""insert into lista
        (nome, numero)
        values
        ('{self.nome}', {self.numero})"""

        self.cursor.execute(add)
        self.cursor.commit()
    # Fim def addContato(self)

    def removerContato(self, nome):
        remover = f"""delete from lista
        where nome = '{self.nome}'"""

        self.cursor.execute(remover)
        self.cursor.commit()
    # Fim def removerContato(self)
# Fim class ListaTelefones
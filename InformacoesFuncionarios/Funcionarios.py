class InfoFuncionarios:
    # Método construtor
    def __init__(self, nome=None, cpf=None, gmail=None, funcao=None, salarioBase=None, salarioLiquido=None, imposto=None, inss=None):
        self.nome = nome
        self.cpf = cpf
        self.gmail = gmail
        self.funcao = funcao
        self.salarioBase = salarioBase
        self.salarioLiquido = salarioLiquido
        self.imposto = imposto
        self.inss = inss
    # Fim def __init__(self, nome=None, cpf=None, gmail=None, funcao=None, salarioBase=None, salarioLiquido=None, imposto=None, inss=None):

    # Calculo do imposto
    def calcImposto(self, salarioBase):
        if self.salarioBase >= 2500:
            porcentagem = 0.15
        if self.salarioBase >= 1500:
            porcentagem = 0.10
        if self.salarioBase >= 900:
            porcentagem = 0.05
        if self.salarioBase < 900:
            porcentagem = 0

        self.imposto = porcentagem * self.salarioBase

        return self.imposto
    # Fim def calcImposto(self, salarioBase):
    
    # Calculo do INSS
    def calcInss(self, salarioBase):
        self.inss = 0.10 * self.salarioBase

        return self.inss
    # Fim def calcInss(self, salarioBase)
    
    # Calculo do salário liquido
    def calcSalarioLiquido(self, salarioBase, imposto, inss):
        self.salarioLiquido = self.salarioBase - (self.imposto + self.inss)

        return self.salarioLiquido
    # Fim def calcSalarioLiquido(self, salarioBase, imposto, inss)
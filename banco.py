# saque, depósito, extrato, traferência.
# conta: saldo, numero da conta, titular, cpf

class Conta:

    def __init__(self,numeroConta,titular, cpf, saldo=0):
        # this/self 
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.titular = titular
        self.cpf = cpf

    def saque(self,valor):
        if valor <= 0:
            print('Valor informado incompativel com a acao')
        elif self.saldo >= valor:
            self.saldo = self.saldo - valor
            print('Saque realizado com sucesso')
        else:
            print('saldo insuficiente')

    def deposito(self, conta, valor):
        if valor <=0:
            print('Insira um valor valido para realizar o deposito')
        else:
            conta.saldo =  conta.saldo + valor
            print('Valor depositado com sucesso')

    def transferencia(self, destino, valor):
        self.saque(valor)
        self.deposito(destino, valor)
        print('tranferencia realizada com sucesso')

conta1 = Conta('1111', 'Renan', '05794884703', 100)
conta2 = Conta('2222', 'Fernada', '0583458003', 30)
conta1.transferencia(conta2,30)
print('Saldo depois da transferencia conta 1:', conta1.saldo)
print('Saldo depois da tranferecia da conta 2', conta2.saldo)

#print(conta1.titular, conta1.saldo)
#conta1.deposito(conta2, 30)
#print(conta2.titular, conta2.saldo)



#conta1.saque(30)
#conta1.saque(int(input('Digit o valor a ser sacado: ')))
#print(conta1.titular, conta1.saldo)


        
import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO - {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO - {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(
            f'Seu limite é {-self.limite:.2f} | SAQUE DISPONÍVEL {-self.limite - self.saldo:.2f}')
        self.detalhes(f'(SAQUE NEGADO - {valor})')
        return self.saldo


if __name__ == '__main__':
    print('TESTE POUPANÇA ^^^')
    conta_poupança1 = ContaPoupanca(111, 222)
    conta_poupança1.sacar(1)
    conta_poupança1.depositar(100)
    conta_poupança1.sacar(99)
    print('###############')
    conta_corrente1 = ContaCorrente(111, 222, 0, 100)
    conta_corrente1.sacar(1)
    conta_corrente1.depositar(100.99)
    conta_corrente1.sacar(102.46)
    conta_corrente1.sacar(3)
    conta_corrente1.sacar(5)
    conta_corrente1.sacar(70)
    conta_corrente1.sacar(17.37)
    conta_corrente1.sacar(20.37)

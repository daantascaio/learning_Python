import contas
import pessoas


class Banco:
    def __init__(
            self, agencias: list[int] | None =None, 
            clientes: list[pessoas.Pessoa] | None =None,
            contas: list[contas.Conta] | None =None
        ) -> None:
            self.agencias = agencias or []
            self.clientes = clientes or []
            self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False


    def autenticar(self, cliente, conta):
        ...
        return True
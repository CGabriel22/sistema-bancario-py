from banco import cliente


class Adm(cliente.Cliente):
    def __init__(self, id: int, nome: str, dataAniversario: str, cpf: str, telefone: str, nCadastro: str):
        self.__nCadastro = nCadastro
        super().__init__(id, nome, dataAniversario, cpf, telefone)

        @property
        def nCadastro(self) -> str:
            return self.__nCadastro

        @nCadastro.setter
        def nCadastro(self, nCadastro: str) -> None:
            self.__nCadastro = nCadastro

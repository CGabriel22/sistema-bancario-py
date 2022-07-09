from banco import conta


class Cliente(conta.Conta):
    def __init__(self, id: int, nome: str, dataAniversario: str, cpf: str, telefone: str):
        self.__id = id
        self.__nome = nome
        self.__dataAniversario = dataAniversario
        self.__cpf = cpf
        self.__telefone = telefone
        super().__init__(1, id, 0.00)

    @property
    def telefone(self) -> float:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        try:
            if len(telefone) < 8:
                raise ValueError('Telefone não pode ser menor que 8 digitos')
            self.__telefone = telefone
        except ValueError as err:
            print(f"Erro: {err}")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def dataAniversario(self) -> str:
        return self.__dataAniversario

    @property
    def cpf(self) -> str:
        return self.__cpf

    def verifica(self, idDigitada: int) -> bool:
        if self.__id != idDigitada:
            return False
        else:
            return True

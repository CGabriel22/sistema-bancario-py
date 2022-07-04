from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
  def __init__(self, idConta: int = 0, clienteId: int = 0, __saldo: float = 0.00):
    self.idConta = idConta
    self.clienteId = clienteId
    self.__saldo = __saldo

  @property.setter
  @abstractmethod
  def setSaldo(self, saldo: float) -> None:
    self.__saldo = saldo

  @property
  @abstractmethod
  def getSaldo(self) -> float:
    return self.__saldo
  
  @abstractmethod
  def deposita(self, valorDeposito: float) -> None:
    self.__saldo += valorDeposito
  
  @abstractmethod
  def saca(self, valorSaque: float) -> None:
    while self.__saldo - valorSaque < 0:
      valorSaque = float(input("Saldo indisponivel! Digite o valor de saque novamente: "))
    self.__saldo -= valorSaque

if __name__ == "__main__":
  teste = Conta()
from abc import ABC, abstractmethod

class Conta:
  def __init__(self, idConta: int, clienteId: int, __saldo: float):
    self.idConta = idConta
    self.clienteId = clienteId
    self.__saldo = __saldo
  
  def setSaldo(self, saldo: float) -> None:
    self.__saldo = saldo

  def getSaldo(self) -> float:
    return self.__saldo
  
  def deposita(self, valorDeposito: float) -> None:
    self.__saldo += valorDeposito
  
  def saca(self, valorSaque: float) -> None:
    while self.__saldo - valorSaque < 0:
      valorSaque = float(input("Saldo indisponivel! Digite o valor de saque novamente: "))
    self.__saldo -= valorSaque

from banco import conta

teste = conta.Conta(1, 2, 0.00)

if __name__ == "__main__":
  teste.setSaldo(23.40)
  print(teste.getSaldo())
  teste.saca(40.00)
  print(teste.getSaldo())

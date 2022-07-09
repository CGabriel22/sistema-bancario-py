from banco import adm

teste = adm.Adm(2, 'carlos gabriel', '22/05',
                '145.197.704-24', '87981713642', '1234')

if __name__ == "__main__":
    print(teste.saldo)
    teste.saldo = 23.40
    print(teste.saldo)
    teste.saca(40.00)
    print(teste.saldo)
    teste.telefone = '8798171'
    teste.nCadastro = '98765'
    print(teste.nCadastro)

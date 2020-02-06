class Endereco:
    def __init__(self, logradouro, bairro, uf, cep):
        self.logradouro = logradouro
        self.bairro = bairro
        self.uf = uf
        self.cep = cep

    def Show(self):
        print(f'Logradouro: {self.logradouro}\n Bairro: {self.bairro}\n UF: {self.uf}\n CEP: {self.cep}')

    def GetObjectText(self):
        return f'Logradouro: {self.logradouro} - Bairro: {self.bairro} - UF: {self.uf} - CEP: {self.cep}'

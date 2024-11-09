class cadastro_de_veiculo:

    def __init__(self, p, m, mod, a, c = 'Não especificado', pro = 'Não especificado', km = 'Não especificado'):
        self.placa = p
        self.marca = m
        self.modelo = mod
        self.ano = a
        self.cor = c
        self.proprietario = pro
        self.quilometragem = km

    def __str__(self):
        if self.placa == '':
            self.placa ='Não especificado'
        if self.marca == '':
            self.marca ='Não especificado'
        if self.modelo == '':
            self.modelo ='Não especificado'
        if self.ano == '':
            self.ano ='Não especificado'
        if self.cor == '':
            self.cor ='Não especificado'
        if self.proprietario == '':
            self.proprietario ='Não especificado'
        if self.quilometragem == '':
            self.quilometragem ='Não especificado'
        r1 = f'A placa do carro: {self.placa}'
        r2 = f'\nA marca do carro: {self.marca}'
        r3 = f'\nO modelo do carro: {self.modelo}'
        r4 = f'\nO ano do carro: {self.ano}'
        r5 = f'\nA cor do carro: {self.cor}'
        r6 = f'\nO proprietario do carro: {self.proprietario}'
        r7 = f'\nA quilometragem do carro: {self.quilometragem}'
        return r1 + r2 + r3 + r4 + r5 + r6 + r7

def main():
    print('Cadastre seu veículo')
    while True:
        result = cadastro_de_veiculo(p = input('Digite a placa do carro: '), m = input('Digite a marca do carro: '), mod = input('Digite o modelo do carro: '), a = int(input('Digite o ano do carro: ')), c = input('Digite a cor do carro: '), pro = input('Digite o proprietario do carro: '), km = int(input('Digite a quilometragem do carro: ')),)
        print(result)
        break
if __name__ == '__main__':
    main()
    
#2. Melhore a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e
#calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela e calibrar_pneus para
#permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0). Execução: Criar pelo menos 2 objetos,
#imprimir seus estados iniciais, executar os métodos e imprimir seus estados finais.

class Bicicleta:
    def __init__(self, veloc_atual=0, altura_cela=0, calibragem_pneus=0):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus

    def regular_cela(self, nova_altura):
        if self.veloc_atual == 0:
            self.altura_cela = max(60, min(nova_altura, 120))
        else:
            print("A bicicleta está em movimento. Pare a bicicleta para ajustar a altura da cela.")

    def calibrar_pneus(self, nova_calibragem):
        if self.veloc_atual == 0:
            self.calibragem_pneus = max(0, min(nova_calibragem, 100))
        else:
            print("A bicicleta está em movimento. Pare a bicicleta para calibrar os pneus.")


bicicleta1 = Bicicleta()
bicicleta2 = Bicicleta()

print("Estado inicial da bicicleta 1:")
print("Velocidade atual:", bicicleta1.veloc_atual)
print("Altura da cela:", bicicleta1.altura_cela)
print("Calibragem dos pneus:", bicicleta1.calibragem_pneus)

print("\nEstado inicial da bicicleta 2:")
print("Velocidade atual:", bicicleta2.veloc_atual)
print("Altura da cela:", bicicleta2.altura_cela)
print("Calibragem dos pneus:", bicicleta2.calibragem_pneus)

bicicleta1.regular_cela(100)
bicicleta1.calibrar_pneus(50)

bicicleta2.regular_cela(110)
bicicleta2.calibrar_pneus(60)

print("\nEstado final da bicicleta 1:")
print("Velocidade atual:", bicicleta1.veloc_atual)
print("Altura da cela:", bicicleta1.altura_cela)
print("Calibragem dos pneus:", bicicleta1.calibragem_pneus)

print("\nEstado final da bicicleta 2:")
print("Velocidade atual:", bicicleta2.veloc_atual)
print("Altura da cela:", bicicleta2.altura_cela)
print("Calibragem dos pneus:", bicicleta2.calibragem_pneus)

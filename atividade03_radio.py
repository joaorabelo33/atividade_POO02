#Exercitando o processo de abstração, modele uma classe Rádio com seus estados e comportamentos. Crie a
#respectiva classe em python e depois crie 2 objetos, imprima os valores de seus atributos e execute os métodos
#criados e imprima os estados finais destes objetos. Recomendação: criar estados que possam ter seus valores
#alterados por seus métodos.

class Radio:
    def __init__(self):
        self.status = False
        self.volume = 0
        self.bateria = 100

    def ligar(self):
        self.status = True

    def desligar(self):
        self.status = False

    def mudar_volume(self, novo_volume):
        if self.status:
            self.volume = novo_volume

    def bateria_atual(self, nivel):
        if self.status:
            self.bateria -= nivel
            if self.bateria < 0:
                self.bateria = 0

radio01 = Radio()
radio02 = Radio()

print("Radio 01 - Estado Inicial:")
print("Ligado:", radio01.status)
print("Volume:", radio01.volume)
print("Bateria:", radio01.bateria)

print("Radio 02 - Estado Inicial:")
print("Ligado:", radio02.status)
print("Volume:", radio02.volume)
print("Bateria:", radio02.bateria)

radio01.ligar()
radio01.mudar_volume(11)
radio01.bateria_atual(76)

radio02.ligar()
radio02.mudar_volume(22)
radio02.bateria_atual(66)

print('\nRadio 01 - Estado Atual:')
print('Ligado:', radio01.status)
print('Volume:', radio01.volume)
print('Bateria:', radio01.bateria)

print('\nRadio 02 - Estado Atual:')
print('Ligado:', radio02.status)
print('Volume:', radio02.volume)
print('Bateria:', radio02.bateria)

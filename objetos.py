# Criando classes - usa-se o nome em pascal case
class NovaClasseVazia:
    pass # o pass cria um bloco vazio se necessário

# Classe com métodos
# Método privado - o _ no nome indica que o método é privado (o python nao tem indicadores de private)
class NovaClasse:
    def __init__(self, nome, valor):  # Define o construtor self é parecido com o this
        self.nome = nome
        self.valor = valor

    def aumentar_valor(self, valor):  # Cria função da classe
        self.valor += valor

    def __str__(self): # metodo que returna uma string quando se dá print no objet
        return f' nome: {objeto.nome} - saldo: {objeto.valor}'


# Instanciar um novo objeto
objeto = NovaClasse("Vinicius", 10000)
# Usar método
objeto.aumentar_valor(5000)
print(f' nome: {objeto.nome} - saldo: {objeto.valor}')
print(objeto)


# Decorator (pesquisar)


# Controle de acesso - getter and setter
class Conta:
    def __init__(self, saldo):
        self._numero = 0
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero


conta = Conta(1000)
conta.set_numero(10444)
conta.sacar(200)


# Controle de acesso com decorator - getter and setter
class Conta:
    def __init__(self, saldo):
        self._numero = 0
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero


conta = Conta(1000)
conta.numero = 10444
print(conta.numero)
conta.sacar(200)


#Herança
class Animal:  # superclasse que vai ser herdada
    def __init__(self, cor, tamanho, peso):
        self.cor = ''
        self.tamanho = ''
        self.peso = ''

    def correr(self):
        print("correr")

    def dormir(self):
        print("dormir")


class Cao(Animal):  # entre parenteses a classe que é herdada
    def __init__(self, cor, tamanho, peso, raca):  # se houver atributos obrigatorios, deve-se colocar entre parenteses
        super().__init__(cor, tamanho, peso)  # como na classe pai e chamar pela função super
        self.raca = raca  # Este atributo é exclusivo do cao

    def latir(self):
        print("latir")

    # sobreescrita de metodo -> override
    def correr(self):
        print("correr como um cao")

    # Executa as ações da classe pai + as específicas da classe filha
    def dormir(self):
        super().dormir()
        print("como um cao")


class Passaro(Animal):  # entre parenteses a classe que é herdada
    def __init__(self, cor, tamanho, peso):  # se houver atributos obrigatorios, deve-se colocar entre parenteses
        super().__init__(cor, tamanho, peso)  # como na classe pai e chamar pela função super

    def voar(self):
        print("voar")


class Papagaio(Passaro, Cao):  # Herança múltipla - Herda tanto de Passaro e Cao
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)

    def falar(self):
        print("falar")


cao = Cao("verde", "50cm", "5kg", "Golden")
cao.dormir()


# Atributos e metodos de classe
class ClasseComAtributo():
    atributo = "Um atributo"

    @classmethod
    def exibir_atributo(cls):  # metodo executavel sem instancia
        print(f'Atributo: {cls.atributo}')

    @staticmethod
    def metodo_estatico():  # Metodo estático que nao tem acesso a atributos da classe
        print("Metodo estatico")


ClasseComAtributo.exibir_atributo()
print(ClasseComAtributo.atributo)  # Atributo acessado sem instancia
ClasseComAtributo.metodo_estatico()


# Classe abstrata - exemplo: metodo que e obrigatorio em uma classe que o herda
from abc import ABC, abstractmethod


class Ser(ABC): # Herda da classe abstrata
    def correr(self):
        print("correr")

    @abstractmethod  # metodo obrigatorio em suas instancias e em classes que o herdam
    def respirar(self):
        print("respirar")


class Humano(Ser):
    def respirar(self):
        print("respirar")


humano = Humano()
humano.respirar()
humano.correr()


"""
Relação de Associação -> É uma das relações mais comuns
entre dois objetos, acontece quando um objeto "utiliza"
outro, porém, sem que eles dependam um do outro
"""


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.video_game = None

    def andar(self):
        print(f'Jogador({self.nome}) andando')


class VideoGame:
    def __init__(self, nome):
        self.nome = nome

    def rodar_jogo(self):
        print(f'Rodar jogo no {self.nome}')


pessoa = Pessoa('Vinicius')

#videogame = VideoGame('Xbox')

#pessoa.video_game = videogame
#pessoa.video_game.rodar_jogo()

pessoa.andar()

class Carro(object):

  def __init__(self, marca, cor, velocidade=0):

      self._marca = marca
      self.cor = cor
      self._velocidade = velocidade

  @property
  def marca(self):
      """ Proprieda somente para leitura """
      return self._marca

  @property
  def velocidade(self):
      """ Proprieda somente para leitura """
      return self._velocidade

  @property
  def cor(self):
      return self._cor

  @cor.setter
  def cor(self, cor):
      """ Essa propriedade suporta escrita """
      self._cor = cor


if __name__=='__main__':
    fusca = Carro('BMW', 'Preta')
    print(fusca.velocidade) # Posso acessar a property como um atributo

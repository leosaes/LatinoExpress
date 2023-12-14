# Criar uma classe chamada Prato.
class Prato:
  nome = str
  preco = float
  descricao = str
  categoria = str
  adicionais = str

  def __init__(self, nome, preco, descricao, categoria):
    self.nome = nome
    self.preco = preco
    self.descricao = descricao
    self.categoria = categoria

    


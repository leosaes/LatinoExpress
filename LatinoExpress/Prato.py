# Criar uma classe chamada Prato.
class Prato:
  nome = str
  preco = float
  descricao = str
  categoria = str
  adicionais = str

  def __init__(self, nome, preco, descricao, categoria, adicionais):
    self.nome = nome
    self.preco = preco
    self.descricao = descricao
    self.categoria = categoria
    self.adicionais = adicionais


#print(Administrador.cadastrar_prato())
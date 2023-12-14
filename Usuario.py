from abc import ABC, abstractmethod

# Criar uma classe chamada Usuario.
class Usuario(ABC):
  name = str
  email = str
  senha = str

  @abstractmethod
  def __init__(self, name, email, senha):
    self.name = name
    self.email = email
    self.senha = senha
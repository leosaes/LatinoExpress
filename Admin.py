from Usuario import Usuario
from Prato import Prato
import os


# Criar uma classe chamada Administrador que herda de Usuario.
class Administrador(Usuario):

  def __init__(self, name, email, senha):
    super().__init__(name, email, senha)

  # Método para cadastrar um prato
  def cadastrar_prato():

    print("Cadastrar Prato")
    # Obter os dados do prato.
    continuar = True
    while continuar == True:
      nome = input("Digite o nome do prato: ")
      preco = input("Digite o preço do prato: ")
      descricao = input("Digite a descrição do prato: ")
      categoria = input("Digite a categoria do prato: ")
  
      # Atribuir os dados do prato na variável prato
      prato = Prato(nome, preco, descricao, categoria)
  
      # Salvar os dados do prato no arquivo txt.
      with open("dados_pratos.txt", "a") as file:
        file.write(
            f"{prato.nome}, {prato.preco},  {prato.descricao}, {prato.categoria}\n"
        )
  
      print("Prato cadastrado com sucesso")

      # Verificar se admin deseja adicionar mais pratos
      
      decisao = input("Você deseja adicionar um novo prato? (Sim ou Não): ")
      if decisao.upper() == "SIM":
        continuar = True
      elif decisao.upper() == "NÃO":
        print("Operação cancelada. Nenhum novo prato adicionado.")
        continuar = False
      else:
        print("Opção inválida. Operação cancelada.")
        continuar = False

#----------------------------------------------------------


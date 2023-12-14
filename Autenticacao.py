from Cliente import Cliente
import getpass

class Autenticacao:

  def __init__(self) -> None:
    pass

  # Função para autenticar o cliente
  @staticmethod
  def autenticarCliente():
    print("LOGIN")
    verifica = True
    while verifica == True:
      email = input("Digite seu E-mail: ")
      senha = getpass.getpass(prompt="Digite sua Senha: ")

      with open("dados_cliente.txt", "r") as file:
        lines = file.readlines()
         # Extrair dados do cliente da linha encontrada
        for line in lines:
          if f"E-mail: {email}" in line and f"Senha: {senha}" in line:
            cliente_linha = line.split(", ")
            name = cliente_linha[0].split(": ")[1]
            email = cliente_linha[1].split(": ")[1]
            senha = cliente_linha[2].split(": ")[1]
            CPF = cliente_linha[3].split(": ")[1]
            telefone = cliente_linha[4].split(": ")[1]
            endereco = cliente_linha[5].split(": ")[1]
            # Criar objeto Cliente com os dados
            cliente = Cliente(name, email, senha, CPF, telefone, endereco)
            print("Login realizado com sucesso!")
            verifica = False
            return cliente
        if verifica == True:
          print("E-mail ou senha incorretos.")
          pergunta = input("Deseja tentar novamente? (S/N): ")
          if pergunta == "S":
            verifica = True
          elif pergunta == "N":
            print("Operação finalizada.")
            verifica = False
            break
          else:
            print("Opção inválida.")
  #----------------------------------------------------------
  
  #Função para autenticar administrador
  @staticmethod
  def autenticarAdm():
    print("LOGIN")
    verifica = True
    while verifica == True:
        nome = input("Digite o seu Nome: ").strip()
        email = input("Digite o seu E-mail: ").strip()
        senha = getpass.getpass(prompt="Senha: ").strip()
  
        with open("dados_adm.txt", "r") as file:
          lines = file.readlines()
        for line in lines:
          if f"Nome: {nome}" in line and f"E-mail: {email}" in line and f"Senha: {senha}" in line:
            print("Login realizado com sucesso!")
            verifica = False
            return True
        if verifica == True:
          print("Nome, E-mail ou senha incorretos.")
          pergunta = input("Deseja tentar novamente? (S/N): ")
          if pergunta == "S":
            verifica = True
          elif pergunta == "N":
            print("Operação finalizada.")
            verifica = False
            break
          else:
            print("Opção inválida.")


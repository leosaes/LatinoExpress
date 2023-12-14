from Autenticacao import Autenticacao
from Cliente import Cliente
from Admin import Administrador
from Entrega import Entrega
import os

# Criar uma classe chamada SistemaRestaurante
class SistemaRestaurante():
  
  def __init__() -> None:
    pass
   # Método estático para juntar dados de vários arquivos em um único arquivo
  @staticmethod
  def juntar_arquivo(nome_arquivo_origem, file_destino, nome_arquivo_origem_comentario):
    try:
        with open(nome_arquivo_origem, 'r') as file_origem:
            # Adicionar um comentário indicando a origem dos dado
            file_destino.write(f"# Origem: {nome_arquivo_origem_comentario}\n")

            # Ler todas as linhas do arquivo de origem
            linhas_origem = file_origem.readlines()
            # Escrever as linhas no arquivo de destino
            file_destino.writelines(linhas_origem)

            file_destino.write('\n')
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo_origem}' não encontrado.")
       # Método para juntar dados de diferentes arquivos em um único arquivo
  def juntar_dados_em_um_arquivo():
    arquivo_final = 'delivery.data' 
    with open(arquivo_final, 'w') as file_destino:
        SistemaRestaurante.juntar_arquivo('dados_adm.txt', file_destino, 'dados_adm.txt')
        SistemaRestaurante.juntar_arquivo('dados_cliente.txt', file_destino, 'dados_cliente.txt')
        SistemaRestaurante.juntar_arquivo('dados_pedido.txt', file_destino, 'dados_pedido.txt')
        SistemaRestaurante.juntar_arquivo('dados_entrega.txt', file_destino, 'dados_entrega.txt')
        SistemaRestaurante.juntar_arquivo('dados_pratos.txt', file_destino, 'dados_pratos.txt')

#----------------------------------------------------------------------------------

  #Função para cadastrar o cliente

  def cadastrar_cliente():
    print("Cadastrar Cliente")
    #Obter os dados do cliente.
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    CPF = input("Digite seu CPF: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")

    # Atribuir os dados do cliente na variável cliente
    cliente = Cliente(nome, email, senha, CPF, telefone, endereco)

    #Salvar os dados do cliente no arquivo txt.
    if not os.path.exists("dados_cliente.txt"):
      return True
    else:
      with open("dados_cliente.txt", "r") as file:
        # Verificar se o CPF ou e-mail já estão cadastrados
        cpfs_cadastrados = [line.split(", ")[3].split(": ")[1] for line in file.readlines()]
        emails_cadastrados = [line.split(", ")[1].split(": ")[1] for line in file.readlines()]
         # Se não estiver cadastrado, adicionar os dados do cliente ao arquivo
        if cliente.CPF in cpfs_cadastrados or cliente.email in emails_cadastrados:
          print("Cliente já cadastrado com esse CPF ou E-mail. Faça seu login:")
          return False
        else:
          with open("dados_cliente.txt", "a") as file:
            file.write(
                f"Nome: {cliente.name}, E-mail: {cliente.email}, Senha: {cliente.senha}, CPF: {cliente.CPF}, Telefone: {cliente.telefone}, Endereço: {cliente.endereco}\n"
            )
          print("Cliente cadastrado com sucesso!")
          return cliente

#----------------------------------------------------------------------------------

  #Função para cadastrar o Administrador
  def cadastrar_adm():
    print("Cadastro de Administrador")

    # Obter os dados do adm.
    nome = input("Digite o nome do Administrador: ")
    email = input("Digite o e-mail do Administrador: ")
    senha = input("Digite a senha do Adiministrador: ")

    # Atribuir os dados do administrador na variável administrador
    administrador = Administrador(nome, email, senha)

    #Salvar os dados do administrador no arquivo txt.
    if not os.path.exists("dados_adm.txt"):
      return True
    else:
      with open("dados_adm.txt", "r") as file:
         # Verificar se o e-mail já está cadastrado
        email_cadastrados = [line.split(", ")[1].split(": ")[1] for line in file.readlines()]
        if administrador.email in email_cadastrados:
          print("Já existe um administrador cadastrado com esse E-mail. Faça seu login:")
          return False
        else:
          # Se não estiver cadastrado, adicionar os dados do administrador ao arquivo
          with open("dados_adm.txt", "a") as file:
            file.write(
                f"Nome: {administrador.name}, E-mail: {administrador.email}, Senha: {administrador.senha}\n"
            )
            print("Administrador cadastrado com sucesso")
            return True


#----------------------------------------------------------------------------------

  #Função para a tela do Cliente
  def tela_cliente():
    # Autenticar o cliente
    cliente = Autenticacao.autenticarCliente()
    if cliente == None:
      return False
    else:
      # Se a autenticação for bem-sucedida, permite ao cliente realizar um pedido
      Cliente.realizarPedido(cliente)
      # Criar uma instância da classe Entrega
      entrega = Entrega()
      # Verificar o prazo de entrega
      entrega.verificar_prazo_entrega()
      # Perguntar ao cliente sobre a entrega do pedido
      entrega.perguntar_entrega_pedido()
       # Juntar todos os dados em um arquivo final
      SistemaRestaurante.juntar_dados_em_um_arquivo()
  
  #Função para a tela do Administrador
  def tela_admin():
     # Se a autenticação for bem-sucedida, permite ao administrador cadastrar um prato
    if Autenticacao.autenticarAdm() == True:
      Administrador.cadastrar_prato()

#----------------------------------------------------------------------------------

  
  def Sistema():
    print("Bem vindo ao LatinoExpress! Seu restaurante de comidas Latino-Americanas favorito \U0001F606	")
    escolha = input("Você é Cliente ou Administrador? ")
    
    if escolha.upper() == "CLIENTE":
      login = input("Desejar realizar Cadastro ou  Login? ")
      if login.upper() == "CADASTRO":
        # Se o cliente escolher cadastrar, chama a função de cadastro de cliente
        SistemaRestaurante.cadastrar_cliente() 
        SistemaRestaurante.tela_cliente()
      elif login.upper() == "LOGIN":
         # Se o cliente escolher fazer login, chama a tela do cliente diretamente
        SistemaRestaurante.tela_cliente() 
      else:
        print("Opção inválida. Volte para o menu inicial.")
    
    elif escolha.upper() == "ADMINISTRADOR":
      login = input("Desejar realizar Cadastro ou  Login? ")
      if login.upper() == "CADASTRO":
        # Se o administrador escolher cadastrar, chama a função de cadastro de administrador
        SistemaRestaurante.cadastrar_adm()
         # Após o cadastro, chama a tela do administrador
        SistemaRestaurante.tela_admin()       
      elif login.upper() == "LOGIN":
         # Se o administrador escolher fazer login, chama a tela do administrador diretamente
        SistemaRestaurante.tela_admin()
      else:
        print("Opção inválida. Volte para o menu inicial.")
    else:
      print("Opção inválida. Volte para o menu inicial.")


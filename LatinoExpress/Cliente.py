class Cliente(Usuario): 
  CPF = str
  telefone = str
  endereco = str

  def init(self, name, email, senha, CPF, telefone, endereco):
    super().init(name, email, senha)
    self.CPF = CPF
    self.telefone = telefone
    self.endereco = endereco


  def cadastrar_cliente():
    print("Cadastrar Cliente")
    #Obter os dados do cliente.
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    senha = input("Digite a senha do cliente: ")
    CPF = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")

    cliente = Cliente(nome, email, senha, CPF, telefone, endereco)


    def salvar_cliente(cliente):
      if not os.path.exists("Cadastro.Cliente.txt"):
          with open("Cadastro.Cliente.txt", "w") as file:
              file.write(f"Nome: {cliente.name}, E-mail: {cliente.email}, CPF: {cliente.CPF}, Telefone: {cliente.telefone}, Endereço: {cliente.endereco}\n")
          print("Cliente cadastrado com sucesso")
          return True
      else:
          with open("Cadastro.Cliente.txt", "r") as file:
              cpfs_cadastrados = [line.split(", ")[2].split(": ")[1] for line in file.readlines()]
              if cliente.CPF in cpfs_cadastrados:
                  print("Cliente já cadastrado com esse CPF")
                  return False
              else:
                  with open("Cadastro.Cliente.txt", "a") as file:
                      file.write(f"Nome: {cliente.name}, E-mail: {cliente.email}, CPF: {cliente.CPF}, Telefone: {cliente.telefone}, Endereço: {cliente.endereco}\n")
                  print("Cliente cadastrado com sucesso")
                  return True
    salvar_cliente(cliente)
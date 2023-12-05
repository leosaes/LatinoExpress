class Administrador(Usuario): 
  def init(self, name, email, senha):
    super().init(name, email, senha)


  def cadastrar_administrador():
    print("Cadastro de Administrador")
    #Obter os dados do cliente.
    nome = input("Digite o nome do Administrador: ")
    email = input("Digite o e-mail do Administrador: ")
    senha = input("Digite a senha do Adiministrador: ")

    administrador = Administrador(nome, email, senha)
    with open("dados.adm.txt" , "a") as arquivo:
      arquivo.write(f"{administrador.name},{administrador.email},{administrador.senha}\n")
from Usuario import Usuario
from Pedido import obter_ultimo_numero_pedido
from prettytable import PrettyTable
from datetime import datetime


class Cliente(Usuario):
  CPF = str
  telefone = str
  endereco = str

  def __init__(self, name, email, senha, CPF, telefone, endereco):
    super().__init__(name, email, senha)
    self.CPF = CPF
    self.telefone = telefone
    self.endereco = endereco
    self.numero_pedido = obter_ultimo_numero_pedido()
    self.pedidos = []

  

#------------------------------------------------------------
  
# Função para o cliente realizar o pedido
  def realizarPedido(self):
    self.numero_pedido = obter_ultimo_numero_pedido() + 1
    pedidos = {}
    valor_prato = 0
    total_pedido = 0
    
    print("Fazer Pedido!")


    tabela = PrettyTable()
    tabela.field_names = ["Prato", "Valor"]
    
    tabela1 = PrettyTable()
    tabela1.field_names = ["Nome", "Preço", "Descrição", "Categoria"]

    #Visualização dos pratos disponíveis

    print("Lista dos pratos disponiveis:")
    with open("dados_pratos.txt", 'r') as file:
      pratos = file.readlines()
      for prato_str in pratos:
        prato_info = prato_str.strip().split(", ")

        if len(prato_info) >= 4:
          tabela1.add_row([
              prato_info[0], f"R${prato_info[1]}", prato_info[2],
              prato_info[3]
          ])
    print(tabela1)

    #Loop para adicionar os pratos ao pedido

    continuar_pedido = True
    while continuar_pedido:
      escolhe_prato = input("Digite o nome do prato que deseja (ou 'sair' para encerrar o pedido): ").capitalize()
      
      if escolhe_prato.lower() == 'sair':
        continuar_pedido = False
        continue
      else:
        if self.numero_pedido not in pedidos:
          pedidos[self.numero_pedido] = []
        
        with open("dados_pratos.txt", 'r+') as file:
            pratos = file.readlines()
            for prato_str in pratos:
              prato_info = prato_str.strip().split(", ")
              if prato_info[0] == escolhe_prato:
                valor_prato = float(prato_info[1])
                total_pedido += valor_prato           

        pedido_atual = {
          'Prato': escolhe_prato,
          'Valor': valor_prato,
          'Hora do Pedido': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        pedidos[self.numero_pedido].append(pedido_atual)

      with open("dados_pedido.txt", 'a') as file:
          file.write(f"Número: {self.numero_pedido}, Cliente: {self.name}, Pedidos: ")

          # Adicionar os itens do pedido ao arquivo
          for pedido in pedidos[self.numero_pedido]:
              file.write(f"[{pedido['Prato']} - R${pedido['Valor']:.2f}], ")

          file.write(f"Total do Pedido: R${total_pedido:.2f}, Hora do Pedido: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

      print(f"Pedido de {escolhe_prato} feito!")
        
      
      if self.name not in pedidos:
        pedidos[self.name] = []
           
  
    print(f"\nItens do pedido Nº {self.numero_pedido} para {self.name}:")
    for pedido in pedidos[self.numero_pedido]:
      tabela.add_row([pedido['Prato'], f"R${pedido['Valor']:.2f}"])
      
    print(tabela)  
    print(f"Total do Pedido: R${total_pedido:.2f}")
    print("Pedido realizado com sucesso! \U0001F60E \U0001F973")
    self.numero_pedido += 1  # Incrementa o número do pedido
    self.status_entrega = False

#------------------------------------------------------------



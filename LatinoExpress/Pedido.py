# Criar uma classe chamada Pedido.
class Pedido:
  Cliente = str
  Itens = []
  EstadoPedido = str
  Status = str
  
  def __init__(self, Cliente, Itens, EstadoPedido, Status):
    self.Cliente = Cliente
    self.Itens = Itens
    self.EstadoPedido = EstadoPedido
    self.Hora = datetime.now().strftime("%Y:%m-%d %H:%M:%S")
    self.Status = Status


prato1 = Prato("Rato frito", "R$ 50,00", "buxo de rato", "Salgado" , 'bacon')
               
cliente_nome = "Samuel Okuur"
itens_pedido = [prato1]
estado_pedido = "Pendente"
status_pedido = "Preparando"

pedido = Pedido(cliente_nome, itens_pedido, estado_pedido, status_pedido)

print("Pedido feito às:", pedido.Hora)
print("Pedido feito por:", pedido.Cliente)
for item in pedido.Itens:
  print("-Nome:", item.nome)
  print("-Preço:", item.preco)
  print('Itens:')
  print('     Descrição:' , item.descricao)
  print('     Categoria:', item.categoria)
  print("     Adicionais" , item.adicionais)
print('Status do pedido:', pedido.Status)

#Criar uma classe chamada Entrega.
#class Entrega:
 # horaEntrega = str
  #idPedido = int

  #ef __init__(self, horaEntrega, idPedido):
    #self.horaEntrega = 
    #self.idPedido = idPedido

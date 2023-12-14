# Criar uma classe chamada Pedido.
class Pedido:
  itens = []
  def __init__(self, numero, cliente, itens, data_hora, tempo_estimado, status):
      self.numero = numero
      self.cliente = cliente
      self.itens = itens
      self.data_hora = data_hora
      self.tempo_estimado = tempo_estimado
      self.status = status
      
#--------------------------------------------------------------------------------------

#Função para não reptir o numero do pedido
def obter_ultimo_numero_pedido():
  try:
    # Tenta abrir o arquivo para leitura
      with open("dados_pedido.txt", 'r') as file:
        # Lê as linhas do arquivo em ordem reversa
          for line in reversed(file.readlines()):
            # Divide a linha em informações do pedido
              pedido_info = line.strip().split(", ")
            # Extrai o número do pedido
              numero = int(pedido_info[0].split(": ")[1])
            # Retorna o número do pedido mais alto encontrado
              return numero
  except FileNotFoundError:
      return 0 # Retorna 0 se o arquivo não existir (caso seja o primeiro pedido)
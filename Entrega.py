from datetime import datetime, timedelta
from Pedido import Pedido
from Cliente import Cliente
import json

class Entrega:
  def __init__(self):
    # Inicializa a classe de entrega
    self.pedidos = self.carregar_pedidos_do_arquivo()
    self.status_entrega = False
    

#Função para carregar os pedidos em self.pedidos
  def carregar_pedidos_do_arquivo(self):
    # Lista para armazenar os objetos Pedido
    pedidos = []
    try:
      with open('dados_pedido.txt', "r") as file:
          for line in file:
              pedido_info = line.strip().split(", ")
             # Verifica se a linha contém informações suficientes
              if len(pedido_info) >= 5:
                # Extrai informações específicas da linha para criar um objeto Pedido
                numero = int(pedido_info[0].split(": ")[1])
                cliente = pedido_info[1].split(": ")[1]
                itens = ", ".join(pedido_info[2:4])
                data_hora = datetime.strptime(pedido_info[-1].split(": ")[1], "%Y-%m-%d %H:%M:%S")
                tempo_estimado = 5  # Altere isso para o valor desejado
                status = "Em andamento"
                # Cria um objeto Pedido e o adiciona à lista de pedidos
                pedido = Pedido(numero, cliente, itens, data_hora, tempo_estimado, status)
                pedidos.append(pedido)
    except FileNotFoundError:
      print("Arquivo 'dados_pedido.txt' não encontrado.")
    return pedidos

  
#------------------------------------------------------------------

      
#Função para formatar o tempo de atraso em Horas, minutos e segundos
  def formatar_tempo_atraso(self, atraso):
      minutos_atraso = atraso.total_seconds() // 60
      horas_atraso = minutos_atraso // 60
      minutos_atraso %= 60
      segundos_atraso = atraso.total_seconds() % 60
      return f"{int(horas_atraso)} horas, {int(minutos_atraso)} minutos e {int(segundos_atraso)} segundos"

#Função para verificar o prazo da entrega
  def verificar_prazo_entrega(self):
    resposta = input("Deseja conferir se o pedido está no prazo de entrega? (Sim/Não): ").lower()
    if resposta == "sim":
      now = datetime.now()
      ultimo_numero_pedido = self.pedidos[-1].numero if self.pedidos else None
      if ultimo_numero_pedido is not None:
        for pedido in self.pedidos:
            if pedido.numero == ultimo_numero_pedido:
              prazo_entrega = pedido.data_hora + timedelta(seconds=pedido.tempo_estimado)
              if now <= prazo_entrega:
                  print(f"Pedido {pedido.numero} dentro do prazo de entrega.")
              else:
                  atraso = now - prazo_entrega
                  tempo_formatado = self.formatar_tempo_atraso(atraso)
                  print(f"Pedido {pedido.numero} está atrasado. Tempo de atraso: {tempo_formatado}.")
      else:
        print("Nenhum pedido encontrado.")
    else:
      print("Conferência de prazo de entrega cancelada.")
#----------------------------------------------------------------------------

  def perguntar_entrega_pedido(self):
    # Obtém o número do último pedido, se existir
      ultimo_numero_pedido = self.pedidos[-1].numero if self.pedidos else None
       # Itera sobre os pedidos
      for pedido in self.pedidos:
        # Verifica se existe um último número de pedido e se o pedido atual é o último
        if ultimo_numero_pedido is not None and pedido.numero == ultimo_numero_pedido:
          # Verifica o status do pedido
            if pedido.status == "entregue":
               # Se o pedido já foi entregue, exibe uma mensagem informando isso
                print(f"O pedido {pedido.numero} já foi marcado como entregue.")
               # Se o pedido não foi entregue, pergunta ao cliente se ele confirma a entrega
            else:
                resposta = input(f"Você confirma a entrega do pedido {pedido.numero}? (Sim/Não): ").lower()
                if resposta == "sim":
                   # Se a confirmação for "sim", atualiza o status do pedido para "Entregue"
                    pedido.status = "Entregue"
                    print(f"Pedido {pedido.numero} marcado como entregue.")
                    print("Obrigado por comprar conosco! Aproveite \U0001F60B")
                   # Registra a informação no arquivo 'dados_entrega.txt'
                    with open('dados_entrega.txt', 'a') as file:
                      file.write(f"Número: {pedido.numero}, Status de Entrega: {pedido.status}, Data de Entrega: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                else:
                  # Se a confirmação for "não", atualiza o status do pedido para "Não entregue"
                    pedido.status = "Não entregue"
                    print(f"Entrega do pedido {pedido.numero} não confirmada.")
                    with open('dados_entrega.txt', 'a') as file:
                      # Registra a informação no arquivo 'dados_entrega.txt'
                      file.write(f"Número: {pedido.numero}, Status de Entrega: {pedido.status}\n")
                break  
              # Sai do loop após tratar o último pedido
      else:
        # Executado se o loop for concluído sem interrupção
          print("Todos os pedidos foram entregues.")






  

import mysql.connector
import time
from datetime import datetime

try:
  conexao = mysql.connector.connect(
    host="db4free.net",
    user="leoabsaes",
    password="ffeb3a1c",
    database= "aula10_11"
  )
  mycursor = conexao.cursor()
except mysql.connector.Error as err:
  print("Error occurred:", err)


# Criar uma classe chamada Usuario.
class Usuario:
  name = str
  email= str
  senha = str
  
  def __init__(self, name, email, senha):
     self.name = name
     self.email = email
     self.senha = senha
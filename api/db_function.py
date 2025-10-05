import sqlite3

db = sqlite3.connect('dados.db')
cursor = db.cursor()

cursor.execute(
  """CREATE TABLE IF NOT EXISTS dados(
  TimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  x REAL, 
  y REAL, 
  z REAL
  )"""
)

db.commit()
db.close()

print('Banco de dados criado com sucesso!!')
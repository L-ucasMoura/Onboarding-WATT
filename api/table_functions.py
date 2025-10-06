import sqlite3
from flask import jsonify

buffer = []

def create_table():
  db = sqlite3.connect('dados.db')
  cursor = db.cursor()

  cursor.execute(
    """CREATE TABLE IF NOT EXISTS tabela(
    TimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    X REAL,
    Y REAL,
    Z REAL
    )"""
  )

  db.commit()
  db.close()

  return print("Tabela criada com sucesso")

def drop_table():
  db = sqlite3.connect('dados.db')
  c = db.cursor()

  c.execute(
    """DROP TABLE IF EXISTS tabela"""
  )
  db.commit()
  db.close()
  
  print("Tabela deletada!")

def to_the_table(data):
  global buffer
  buffer.append((data['x'], data['y'], data['z']))

  if len(buffer) >= 100:
    db = sqlite3.connect("dados.db")
    c = db.cursor()

    c.executemany(
      """
      INSERT INTO dados (x,y,z) VALUES (?, ?, ?)
      """
      ,buffer
    )
    
    db.commit()
    db.close()
    buffer.clear()

  return jsonify({"status": "ok", "Message": f"Buffer em {len(buffer)}"})

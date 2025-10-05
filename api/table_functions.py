import sqlite3
from flask import jsonify

def to_the_table(data):
  db = sqlite3.connect("dados.db")
  c = db.cursor()

  c.execute(
    """
    INSERT INTO dados (x,y,z) VALUES (?, ?, ?)
    """
    ,(data['x'], data['y'], data['z'])
   )
  print(data)
  db.commit()
  db.close()
  
  return jsonify({"status": "ok", "Message": "Chegou"})

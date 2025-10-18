import sqlite3, socket
from flask import jsonify
from datetime import datetime, timezone

def get_ipv4():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('8.8.8.8', 80))
  ip = s.getsockname()[0]
  s.close()
  return ip



def to_the_table(data):

  hora_local = datetime.now(timezone.utc).astimezone()
  hora_local_str = hora_local.strftime("%d-%m-%Y %H:%M:%S")
  
  db = sqlite3.connect("dados.db")
  c = db.cursor()

  c.execute(
    """
    INSERT INTO tabela (TimeStamp,x,y,z,angle,direction) VALUES (?, ?, ?, ?, ?, ?)
    """
    ,(hora_local_str, round(data['x'], 4),round(data['y'], 4),round(data['z'], 4),int(round(data['angle'])),data['direction'])
  )
  
  db.commit()
  db.close()
  

  return jsonify({"status": "ok", "Message": "Dados inseridos na tabela"})


def send_to_esp(direction):
  if direction == 'UP':
    return 23
  elif direction == 'DOWN':
    return 22
  elif direction == 'LEFT':
    return 4
  elif direction == 'RIGHT':
    return 2
  else:
    return 0

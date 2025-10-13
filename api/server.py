from flask import Flask, request, jsonify
import table_functions
import atexit
import serial, requests

#esp = serial.Serial('COM10', 9600, timeout=1)
buffer = []
destinations = ['http://10.7.240.9:5000/server/toEsp']

# Aqui cria-se o servidor web via Flask
app = Flask(__name__)


@app.route('/listener', methods=['POST'])
def listener():
  data = request.get_json()
  results = []
  for url in destinations:
    try:
      ans = requests.post(url, json=data)
      results.append({
        'rota':url,
        'status': ans.status_code,
        'resposta': ans.json() if ans.ok else None
      })

    except Exception as e:
      results.append({
        'rota': url,
        'erro': str(e)
      })

  return jsonify({'status':'OK', 'dado':f'{results}'})



@app.route('/server/gotodb', methods=["POST"])
def insert_in_table():
  data = request.get_json()
  return table_functions.to_the_table(data)

@app.route("/server/toEsp", methods=['POST'])
def go_to_esp():
  direction = request.get_json()['direction']
  esp.write(f'{table_functions.send_to_esp(direction)}\n'.encode())
  print(table_functions.send_to_esp(direction))
  return jsonify({'status': 'ok', 'direção':f'{direction}', 'pino': f'{table_functions.send_to_esp(direction)}'})


# Isso aqui é executado ao fechar o server via terminal (Ctrl + C)
@atexit.register
def cleanup():
   return table_functions.drop_table()

# __name__ é uma variável especial em Python que indica se o script está sendo executado diretamente ou importado como um módulo.
# Se o script estiver sendo executado diretamente, o servidor Flask será iniciado.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import table_functions
import atexit, threading
import serial, time


esp = None
esp_lock = threading.Lock()  # para evitar conflitos entre threads

def manage_esp_connection():
    global esp
    while True:
        if esp is None or not esp.is_open:
            try:
                esp_conn = serial.Serial('COM10', 9600, timeout=1)
                with esp_lock:
                    esp = esp_conn
                print("ESP32 conectada!")
            except serial.SerialException:
                print("Não foi possível conectar à ESP32. Tentando novamente em 3s...")
                time.sleep(3)
        else:
            # ESP conectada, espera um pouco antes de checar de novo
            time.sleep(1)

threading.Thread(target=manage_esp_connection, daemon=True).start()

# Aqui cria-se o servidor web via Flask
app = Flask(__name__)


@app.route('/server/gotodb', methods=["POST"])
def insert_in_table():
  global esp
  with esp_lock:
    if esp and esp.is_open:
      data = request.get_json()
      return table_functions.to_the_table(data)
    else:
        return jsonify({'status':'null', 'message':'Dados não inseridos. Sem conexão com a ESP'})

@app.route("/server/toEsp", methods=['POST'])
def go_to_esp():
    global esp
    with esp_lock:
        if esp and esp.is_open:
            direction = request.get_json()['direction']
            angle = request.get_json()['angle']
            print(f'Ângulo: {angle}, Tipo: {type(angle)}')
            pino = table_functions.send_to_esp(direction)
            try:
                esp.write(f'{angle}\n'.encode())
                return jsonify({'status': 'ok', 'direção': direction, 'angulo': angle})
            except serial.SerialException:
                # ESP caiu no meio da operação
                esp.close()  # fecha a conexão antiga
                esp = None    # força a thread de reconexão a tentar de novo
                return jsonify({'status': 'error', 'message': 'ESP desconectada durante envio'})
        else:
            return jsonify({'status': 'error', 'message': 'ESP não conectada'})


# Isso aqui é executado ao fechar o server via terminal (Ctrl + C)
#@atexit.register

# __name__ é uma variável especial em Python que indica se o script está sendo executado diretamente ou importado como um módulo.
# Se o script estiver sendo executado diretamente, o servidor Flask será iniciado.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
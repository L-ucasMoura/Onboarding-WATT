from flask import Flask, jsonify, request
import table_functions
import atexit

buffer = []


# Aqui cria-se o servidor web via Flask
app = Flask(__name__)

@app.route('/gotodb', methods=["POST"])
def insert_in_table():
  data = request.get_json()
  #table_functions.create_table()
  return table_functions.to_the_table(data)

# Isso aqui é executado ao fechar o server via terminal (Ctrl + C)
@atexit.register
def cleanup():
   return table_functions.drop_table()

# __name__ é uma variável especial em Python que indica se o script está sendo executado diretamente ou importado como um módulo.
# Se o script estiver sendo executado diretamente, o servidor Flask será iniciado.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
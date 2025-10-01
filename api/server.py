from flask import Flask, jsonify, request

dados = []


# Aqui cria-se o servidor web via Flask
app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def receber_dados():
    conteudo = request.json
    dados.append(conteudo)
    return jsonify({"status": "OK", "Mensagem": "Dados recebidos com sucesso!"})

@app.route('/listar', methods=['GET'])
def listar_dados():
    return jsonify(dados)

# __name__ é uma variável especial em Python que indica se o script está sendo executado diretamente ou importado como um módulo.
# Se o script estiver sendo executado diretamente, o servidor Flask será iniciado.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
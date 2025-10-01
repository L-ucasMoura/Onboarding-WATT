from flask import Flask

# Aqui cria-se o servidor web via Flask
app = Flask(__name__)

# Aqui define-se uma rota simples, que retorna "Hello, World!" quando acessada
# No navegador, a rota é acessada via http://localhost:5000/
@app.route('/')
def hello():
    return "Hello, World!"

# Já essa rota é acessada via http://localhost:5000/sobre
@app.route('/sobre')
def sobre():
    return "Esta é a página sobre."

# __name__ é uma variável especial em Python que indica se o script está sendo executado diretamente ou importado como um módulo.
# Se o script estiver sendo executado diretamente, o servidor Flask será iniciado.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
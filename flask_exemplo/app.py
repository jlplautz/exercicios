from flask import Flask, request

dados = {"canal": "LinuxTips", "msg": "Vaiii!!"}  # dict

# para criar uma aplicação flask criamos uma app
# e informamos o nome da aplicação
app = Flask("app")

# apartir deste objeto app podemos fazer muitas coisas
# podemos mexer na configuração do flask
# podemos inicializar extensões

# podemos ligar função com rotas que serão chamadas pelo navegador
@app.route("/")
def linuxtips():  # Callable
    return dados


@app.route("/hello/<nome>/")
def hello(nome):
    return f"<h1>Hello {nome} - {request.args['msg']}</h1)"

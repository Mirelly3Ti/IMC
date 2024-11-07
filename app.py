from flask import Flask, render_template
import sqlite3
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

# Conectar banco de dados
conn = sqlite3.connect('IMC.db')
cursor = conn.cursor()

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', results=results)

def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

# Dados inseridos
def inserir_dados(nome, peso, altura):
    IMC = calcular_IMC(peso, altura)
    cursor.execute('''
        INSERT INTO IMC (nome, peso, altura, IMC)
        VALUES (?, ?, ?, ?)
    ''', (nome, peso, altura, IMC))
    conn.commit()

# Rota resultados

@app.route("/results", methods=['GET', 'POST'])
def results(IMC):
    if IMC < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= IMC < 24.9:
        return "Peso normal"
    elif 25 <= IMC < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Fim da conexão do banco de dados
conn.close()
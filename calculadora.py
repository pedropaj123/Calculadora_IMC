from flask import Flask, render_template, request
import os
import cx_Oracle

app = Flask(__name__)

# String de conexão
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")

# Conectar com SYS como SYSDBA
connection = cx_Oracle.connect(user="SYS", password="457912", dsn=dsn_tns, mode=cx_Oracle.SYSDBA)

# Testar se a conexão foi bem-sucedida
print("Conectado ao banco de dados com SYSDBA")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])

        if altura == 0:
            return "Erro: Altura não pode ser zero!", 400

        # Cálculo do IMC
        imc = peso / (altura ** 2)

        # Classificação do IMC
        if imc <= 18.5:
            classificacao = "Abaixo do normal"
        elif imc <= 24.9:
            classificacao = "Normal"
        elif imc <= 29.9:
            classificacao = "Sobrepeso"
        elif imc <= 34.9:
            classificacao = "Obesidade grau 1"
        elif imc <= 39.9:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        # Renderiza a página de resultado com a opção de salvar os dados
        return render_template(
            'resultado.html',
            imc=imc,
            classificacao=classificacao
        )
    except Exception as e:
        return f"Erro: {e}", 500

@app.route('/salvar', methods=['GET', 'POST'])
def salvar():
    if request.method == 'POST':
        try:
            # Dados recebidos do formulário
            nome = request.form['nome']
            imc = float(request.form['imc'])
            classificacao = request.form['classificacao']

            # Insere os dados no banco de dados
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO calculo_imc (nome, imc, classificacao) VALUES (:1, :2, :3)",
                (nome, imc, classificacao)
            )
            connection.commit()
            cursor.close()

            return f"Dados de {nome} salvos com sucesso no banco de dados!"
        except Exception as e:
            return f"Erro ao salvar os dados: {e}", 500
    else:
        # Quando o método for GET, mostra o formulário de salvar dados
        imc = request.args.get('imc')
        classificacao = request.args.get('classificacao')
        return render_template(
            'salvar.html',
            imc=imc,
            classificacao=classificacao
        )

if __name__ == '__main__':
    # Usando a variável de ambiente PORT fornecida pelo Render ou 5000 por padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

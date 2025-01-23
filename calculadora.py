from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        if altura == 0  :
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
        
        # Renderiza a página de resultado
        return render_template('resultado.html', imc=imc, classificacao=classificacao)
    except Exception as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)

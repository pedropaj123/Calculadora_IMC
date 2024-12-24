<h1 align="center">Calculadora de IMC 🧮💪</h1>

<p align="center">
    Uma calculadora simples de <strong>Índice de Massa Corporal (IMC)</strong> desenvolvida em Python. 
    Este projeto permite calcular o IMC rapidamente e fornece a classificação do resultado com base nos parâmetros da 
    <strong>Organização Mundial da Saúde (OMS)</strong>.
</p>

<h2>🚀 Funcionalidades</h2>
<ul>
    <li>Solicita ao usuário o peso (em kg) e a altura (em metros).</li>
    <li>Calcula o IMC utilizando a fórmula:</li>
</ul>
<blockquote>
    <strong>IMC = peso (kg) / altura (m)<sup>2</sup></strong>
</blockquote>
<ul>
    <li>Classifica o IMC de acordo com os intervalos oficiais:</li>
    <ul>
        <li><strong>Abaixo de 18.5</strong>: Abaixo do peso</li>
        <li><strong>18.5 – 24.9</strong>: Peso normal</li>
        <li><strong>25.0 – 29.9</strong>: Sobrepeso</li>
        <li><strong>30.0 – 34.9</strong>: Obesidade Grau 1</li>
        <li><strong>35.0 – 39.9</strong>: Obesidade Grau 2</li>
        <li><strong>Acima de 40.0</strong>: Obesidade Grau 3</li>
    </ul>
</ul>

<h2>📋 Pré-requisitos</h2>
<ul>
    <li>Python 3.7 ou superior instalado na máquina.</li>
</ul>

<h2>🛠️ Como usar</h2>
<ol>
    <li>Clone o repositório:</li>
    <pre>
        <code>git clone https://github.com/seu-usuario/calculadora-imc.git</code>
    </pre>
    <li>Navegue até o diretório do projeto:</li>
    <pre>
        <code>cd calculadora-imc</code>
    </pre>
    <li>Execute o script:</li>
    <pre>
        <code>python calculadora_imc.py</code>
    </pre>
</ol>

<h2>💡 Exemplo de uso</h2>
<p><strong>Entrada:</strong></p>
<pre>
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
</pre>
<p><strong>Saída:</strong></p>
<pre>
Seu IMC é 22.86. Classificação: Peso normal
</pre>

<h2>🔧 Melhorias futuras</h2>
<ul>
    <li>Adicionar uma interface gráfica usando <strong>Tkinter</strong> ou um frontend com <strong>Flask</strong>.</li>
    <li>Salvar os resultados em um arquivo ou banco de dados.</li>
    <li>Implementar uma versão web responsiva para acesso em qualquer dispositivo.</li>
    <li>Tratar erros como entradas inválidas de forma mais robusta.</li>
</ul>

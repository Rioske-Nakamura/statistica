from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    # Carregar os dados do Excel
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    # Calcular a correlação
    correlacao = np.corrcoef(df['União Europeia'], df['Índia'])[0, 1]

    # Classificar o tipo de correlação
    if abs(correlacao) > 0.6:
        intensidade = "Moderada" if abs(correlacao) <= 0.8 else "Forte"
    else:
        intensidade = "Fraca"

    sinal = "Positiva" if correlacao > 0 else "Negativa"

    # Passar os resultados para o template
    return render_template('index.html', correlacao=correlacao, intensidade=intensidade, sinal=sinal)

if __name__ == '__main__':
    app.run(debug=True)

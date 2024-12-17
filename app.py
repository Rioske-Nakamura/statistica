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

    # Passar os resultados para o template principal
    return render_template(
        'index.html',
        correlacao=correlacao,
        intensidade=intensidade,
        sinal=sinal
    )

@app.route('/media')
def media():
    # Carregar os dados do Excel
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    # Calcular a média
    media_ue = df['União Europeia'].mean()
    media_india = df['Índia'].mean()

    # Passar as médias para o template de média
    return render_template(
        'media.html',
        media_ue=media_ue,
        media_india=media_india
    )

@app.route('/mediana')
def mediana():
    # Carregar os dados do Excel
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    # Calcular a mediana
    mediana_ue = df['União Europeia'].median()
    mediana_india = df['Índia'].median()

    # Passar as medianas para o template de mediana
    return render_template(
        'mediana.html',
        mediana_ue=mediana_ue,
        mediana_india=mediana_india
    )

@app.route('/moda')
def moda():
    # Carregar os dados do Excel
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    # Calcular a moda
    moda_ue = df['União Europeia'].mode().iloc[0]
    moda_india = df['Índia'].mode().iloc[0]

    # Passar as modas para o template de moda
    return render_template(
        'moda.html',
        moda_ue=moda_ue,
        moda_india=moda_india
    )

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import matplotlib

# Configurar Matplotlib para evitar problemas de thread
matplotlib.use('Agg')

app = Flask(__name__)

def criar_grafico(x, y, titulo, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-')
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.grid()

    # Converter o gráfico para base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    return f"data:image/png;base64,{graph_url}"

@app.route('/')
def index():
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    correlacao = np.corrcoef(df['União Europeia'], df['Índia'])[0, 1]

    if abs(correlacao) > 0.6:
        intensidade = "Moderada" if abs(correlacao) <= 0.8 else "Forte"
    else:
        intensidade = "Fraca"

    sinal = "Positiva" if correlacao > 0 else "Negativa"

    # Criar gráfico de dispersão para a correlação
    grafico = criar_grafico(
        df['União Europeia'], df['Índia'],
        "Correlação: União Europeia vs Índia",
        "União Europeia", "Índia"
    )

    return render_template(
        'index.html',
        correlacao=correlacao,
        intensidade=intensidade,
        sinal=sinal,
        grafico=grafico
    )
@app.route('/media')
def media():
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    media_ue = df['União Europeia'].mean()
    media_india = df['Índia'].mean()

    grafico = criar_grafico(
        ["União Europeia", "Índia"],
        [media_ue, media_india],
        "Média dos Valores",
        "Região", "Média"
    )
  
    return render_template(
        'media.html',
        media_ue=media_ue,
        media_india=media_india,
        grafico=grafico,
    )

@app.route('/mediana')
def mediana():
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    mediana_ue = df['União Europeia'].median()
    mediana_india = df['Índia'].median()

    grafico = criar_grafico(
        ["União Europeia", "Índia"],
        [mediana_ue, mediana_india],
        "Mediana dos Valores",
        "Região", "Mediana"
    )

    return render_template(
        'mediana.html',
        mediana_ue=mediana_ue,
        mediana_india=mediana_india,
        grafico=grafico,

    )

@app.route('/moda')
def moda():
    arquivo_excel = "data.xlsx"
    df = pd.read_excel(arquivo_excel)

    moda_ue = df['União Europeia'].mode().iloc[0]
    moda_india = df['Índia'].mode().iloc[0]


    grafico = criar_grafico(
        ["União Europeia", "Índia"],
        [moda_ue, moda_india],
        "Moda dos Valores",
        "Região", "Moda"
    )


    return render_template(
        'moda.html',
        moda_ue=moda_ue,
        moda_india=moda_india,
        grafico=grafico,
    )

if __name__ == '__main__':
    app.run(debug=True)

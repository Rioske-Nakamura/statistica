import matplotlib.pyplot as plt

# Dados
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
temp_min = [18, 20, 19, 17, 21, 22, 20]
temp_max = [28, 30, 29, 27, 31, 32, 30]

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(dias, temp_min, marker='o', label='Temperatura Mínima (°C)', color='blue')
plt.plot(dias, temp_max, marker='o', label='Temperatura Máxima (°C)', color='red')

# Títulos e legendas
plt.title("Temperatura Mínima e Máxima Durante uma Semana", fontsize=14)
plt.xlabel("Dias da Semana", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Exibição
plt.show()

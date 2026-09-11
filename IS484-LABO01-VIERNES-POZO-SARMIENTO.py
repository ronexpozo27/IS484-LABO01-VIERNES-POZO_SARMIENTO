# Importar librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fijar resultados aleatorios
np.random.seed(42)

# Número de transacciones
n = 300

# Generar horas aleatorias
hora = np.random.randint(0, 24, n)

# Generar montos aleatorios
monto = np.random.exponential(scale=150, size=n) + 10

# Calcular probabilidad de fraude
prob_fraude = 0.03 + 0.35 * ((hora <= 5) | (hora >= 23)) + 0.25 * (monto > 400)

# Limitar probabilidad al 90%
prob_fraude = np.clip(prob_fraude, 0, 0.9)

# Clasificar transacciones
es_fraude = (np.random.rand(n) < prob_fraude).astype(int)

# Crear tabla de transacciones
transacciones = pd.DataFrame({
    "hora": hora,
    "monto": monto,
    "es_fraude": es_fraude
})

# Definir colores y etiquetas
colores = {0: "#0ca30c", 1: "#d03b3b"}
etiquetas = {0: "Legitima", 1: "Fraude"}

# Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6), facecolor="#fcfcfb")
ax.set_facecolor("#fcfcfb")

# Graficar transacciones
for valor in [0, 1]:
    subset = transacciones[transacciones["es_fraude"] == valor]

    ax.scatter(
        subset["hora"], subset["monto"],
        s=70, alpha=0.75,
        c=colores[valor],
        edgecolors="white", linewidths=0.6,
        label=etiquetas[valor],
    )

# Configurar título y ejes
ax.set_title("Transacciones por hora y monto", fontsize=15, color="#0b0b0b", pad=14)
ax.set_xlabel("Hora del dia", fontsize=11, color="#52514e")
ax.set_ylabel("Monto (S/)", fontsize=11, color="#52514e")

# Configurar horas del eje X
ax.set_xticks(range(0, 24, 2))

# Mostrar cuadrícula
ax.grid(True, color="#e1e0d9", linewidth=0.8)

# Ocultar bordes superior y derecho
ax.spines[["top", "right"]].set_visible(False)

# Mostrar leyenda
ax.legend(title="Tipo de transaccion", frameon=False, loc="upper right")

# Ajustar el gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar cantidad de transacciones y fraudes
print(
    "Total transacciones:", len(transacciones),
    "| Fraudes:", transacciones["es_fraude"].sum()
)
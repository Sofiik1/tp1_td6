import pandas as pd

# Cargar el dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00529/diabetes_binary_5050split_health_indicators_BRFSS2015.csv"
data = pd.read_csv(url)

# Configurar la semilla para la reproducibilidad
seed = 42

# Realizar el muestreo aleatorio para reducir a 50,000 observaciones
data_reduced = data.sample(n=50000, random_state=seed)

# Guardar el dataset reducido
data_reduced.to_csv("diabetes_health_indicators_reduced.csv", index=False)
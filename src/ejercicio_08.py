
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}  
df = pd.DataFrame(data).set_index("empleado_id")

def clasificar_salario(salario):
    if salario < 50000:
        return "Bajo"
    elif salario < 90000:
        return "Medio"
    else:
        return "Alto"

def ejercicio_08():
    df["categoria_salario"] = df["salario"].apply(clasificar_salario)

    print("\nEmpleados con salario superior al promedio")
    promedio = df["salario"].mean()
    print(df.loc[df["salario"] > promedio].head())

    print("\nEmpleados con salario en el percentil 75")
    p75 = df["salario"].quantile(0.75)
    print(df.loc[df["salario"] >= p75].head())

    print("\n Distribución de categorías salariales")
    print(df["categoria_salario"].value_counts())

ejercicio_08()

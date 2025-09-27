# src/ejercicio_09.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}  
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_09():
    print("\nActivos, IT o Finanzas, salario > 60000 y edad < 45")
    filtro1 = df.loc[(df["activo"]) &
                     (df["departamento"].isin(["IT", "Finanzas"])) &
                     (df["salario"] > 60000) &
                     (df["edad"] < 45)]
    print(filtro1.head())

    print("\nEmpleados de Bogotá o Cali con experiencia > 10 años")
    filtro2 = df.loc[(df["ciudad"].isin(["Bogotá", "Cali"])) &
                     (df["experiencia_años"] > 10)]
    print(filtro2.head())

    print("\n Resumen estadístico de los filtrados")
    print(filtro1.describe())
    print(filtro2.describe())

ejercicio_09()

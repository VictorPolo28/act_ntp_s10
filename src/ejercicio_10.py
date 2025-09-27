
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}  
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_10():
    print("\nVista: empleados activos con salario alto")
    print(df.loc[(df["activo"]) & (df["salario"] > 90000)].head())

    print("\nMétricas por departamento")
    print(df.groupby("departamento")["salario"].mean())

    print("\nMétricas por ciudad")
    print(df.groupby("ciudad")["experiencia_años"].mean())

    print("\n Top 5 empleados con más salario")
    print(df.sort_values("salario", ascending=False).head())

    print("\n Empleados recientes (último año)")
    recientes = df.loc[df["fecha_ingreso"] >= datetime.now() - timedelta(days=365)]
    print(recientes.head())

ejercicio_10()

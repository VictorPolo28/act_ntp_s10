
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')


def ejercicio_03():
    print("IT con salario > 70,000")
    it_salario = df.loc[(df["departamento"] == "IT") & (df["salario"] > 70000)]
    print(it_salario.describe(), "\n")

    print("Ventas o Marketing")
    ventas_mark = df.loc[df["departamento"].isin(["Ventas", "Marketing"])]
    print(ventas_mark["departamento"].value_counts(), "\n")

    print("Activos con +5 años de experiencia")
    exp = df.loc[(df["activo"]) & (df["experiencia_años"] > 5)]
    print(exp[["edad", "experiencia_años"]].describe())


if __name__ == "__main__":
    ejercicio_03()

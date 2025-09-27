
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}  
df = pd.DataFrame(data).set_index('empleado_id')


def ejercicio_02():
    print("Empleados mayores de 40 años")
    filtro1 = df.loc[df["edad"] > 40]
    print(filtro1, "\nTotal:", len(filtro1), "\n")

    print("Empleados del departamento IT")
    filtro2 = df.loc[df["departamento"] == "IT"]
    print(filtro2, "\nTotal:", len(filtro2), "\n")

    print("Empleados con salario > 80,000")
    filtro3 = df.loc[df["salario"] > 80000]
    print(filtro3, "\nTotal:", len(filtro3))


if __name__ == "__main__":
    ejercicio_02()

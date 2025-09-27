
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')


def ejercicio_04():
    print("Nombre y salario:")
    print(df.loc[:, ["nombre", "salario"]].head(10), "\n")

    print("Desde nombre hasta departamento:")
    print(df.loc[:, "nombre":"departamento"].head(10), "\n")

    print("Mayores de 50 años (nombre, edad, salario):")
    print(df.loc[df["edad"] > 50, ["nombre", "edad", "salario"]].head(10))


if __name__ == "__main__":
    ejercicio_04()


import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')


def ejercicio_05():
    print("Antes:")
    print(df.head(), "\n")

  
    df.loc[df["departamento"] == "IT", "salario"] *= 1.1

    
    df.loc[df["edad"] > 60, "activo"] = False

    df.loc[df["departamento"] == "RRHH", "ciudad"] = "Bogotá"

    print("Después:")
    print(df.head())


if __name__ == "__main__":
    ejercicio_05()

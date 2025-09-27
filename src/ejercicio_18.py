# src/ejercicio_18.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_18():
    indices = df[df["edad"] > 50].index[:5]
    print(df.loc[indices])
    posiciones = df[df["salario"] > 100000].index[:5]
    print(df.loc[posiciones])
    p90 = int(len(df) * 0.9)
    print(df.iloc[p90:])

ejercicio_18()

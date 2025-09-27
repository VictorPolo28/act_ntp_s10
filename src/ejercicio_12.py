# Ejercicio 12: Selección con Rangos
# Implementa aquí tu solución
# src/ejercicio_12.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_12():
    print(df.iloc[9:20])
    print(df.iloc[-10:])
    print(df.iloc[::2].head())
    print(df.iloc[::3].head())

ejercicio_12()

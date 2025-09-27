# src/ejercicio_13.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_13():
    print(df.iloc[[0, 5, 10, 20]])
    print(df.sample(5))
    posiciones = [0, 2, 4, 10, 50]
    print(df.iloc[posiciones])

ejercicio_13()

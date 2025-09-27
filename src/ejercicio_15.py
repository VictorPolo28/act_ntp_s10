# src/ejercicio_15.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_15():
    df.iloc[0, 2] = 99
    df.iloc[1:3, 3] = 75000
    df.iloc[4:6, [2, 3]] = [[40, 80000], [41, 82000]]
    print(df.head(10))

ejercicio_15()

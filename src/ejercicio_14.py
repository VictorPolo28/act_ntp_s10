# src/ejercicio_14.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_14():
    print(df.iloc[:, :3].head())
    print(df.iloc[:, [0, 3, 5]].head())
    print(df.iloc[:, -1].head())
    print(df.iloc[0:5, 0:4])

ejercicio_14()

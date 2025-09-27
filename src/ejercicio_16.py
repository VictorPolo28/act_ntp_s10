# src/ejercicio_16.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_16():
    print(df.iloc[::2].head())
    print(df.iloc[::-1].head())
    print(df.iloc[2::5].head())
    print(df.iloc[::3, ::2].head())

ejercicio_16()

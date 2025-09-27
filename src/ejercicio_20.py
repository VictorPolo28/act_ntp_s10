# src/ejercicio_20.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_20():
    print(df.iloc[:10])
    print(df.sample(10))
    print(df.iloc[::15])
    print(df.iloc[:20].mean(numeric_only=True))
    print(df.sample(20).describe())

ejercicio_20()

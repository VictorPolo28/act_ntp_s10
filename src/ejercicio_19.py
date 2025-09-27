# src/ejercicio_19.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_19():
    print(df.iloc[:5])
    print(df.sample(5))
    print(df.iloc[::10].head())
    print(df.sample(10).mean(numeric_only=True))

ejercicio_19()

# src/ejercicio_17.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_17():
    print(df.iloc[0:5, 0:3])
    booleanos = [True if i % 2 == 0 else False for i in range(len(df))]
    print(df.iloc[booleanos].head())
    print(df.iloc[:10].mean(numeric_only=True))

ejercicio_17()

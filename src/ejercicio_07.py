
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


data = {...}  
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_07():
    print("\nEmpleados que ingresaron en 2022")
    en_2022 = df.loc[df["fecha_ingreso"].dt.year == 2022]
    print(en_2022.head())

    print("\nEmpleados que ingresaron en los últimos 2 años")
    ultimos_2 = df.loc[df["fecha_ingreso"] >= datetime.now() - timedelta(days=730)]
    print(ultimos_2.head())

    print("\nEmpleados que ingresaron en el primer trimestre")
    primer_trim = df.loc[df["fecha_ingreso"].dt.month.isin([1,2,3])]
    print(primer_trim.head())

    print("\n Antigüedad promedio (en días)")
    antiguedad = (datetime.now() - df["fecha_ingreso"]).dt.days.mean()
    print(f"Antigüedad promedio: {antiguedad:.2f} días")

ejercicio_07()

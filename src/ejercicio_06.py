

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = {
    'empleado_id': range(1, 101),
    'nombre': [f'Empleado_{i}' for i in range(1, 101)],
    'apellido': [f'Apellido_{i}' for i in range(1, 101)],
    'edad': np.random.randint(22, 65, 100),
    'departamento': np.random.choice(['Ventas', 'Marketing', 'IT', 'RRHH', 'Finanzas'], 100),
    'salario': np.random.randint(30000, 120000, 100),
    'fecha_ingreso': [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1460)) for _ in range(100)],
    'activo': np.random.choice([True, False], 100, p=[0.85, 0.15]),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'], 100),
    'experiencia_años': np.random.randint(1, 20, 100)
}
df = pd.DataFrame(data).set_index("empleado_id")

def ejercicio_06():
    print("\nEmpleados cuyo nombre contiene '1'")
    print(df.loc[df["nombre"].str.contains("1")].head())

    print("\n Empleados cuyo apellido termina en '5'")
    print(df.loc[df["apellido"].str.endswith("5")].head())

    print("\nEmpleados de ciudades que empiezan con 'B'")
    print(df.loc[df["ciudad"].str.startswith("B")].head())

ejercicio_06()


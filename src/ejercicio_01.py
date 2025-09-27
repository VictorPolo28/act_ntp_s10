
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
df = pd.DataFrame(data).set_index('empleado_id')


def ejercicio_01():
    print("Empleado con ID = 10")
    print(df.loc[10], "\n")

    print("Empleados con IDs [5, 20, 33]")
    print(df.loc[[5, 20, 33]], "\n")

    print("Empleados del ID 40 al 45")
    print(df.loc[40:45])


if __name__ == "__main__":
    ejercicio_01()

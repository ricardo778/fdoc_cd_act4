import pandas as pd

datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}

df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

# Guarda el dataset para ejercicios de lectura/escritura
df.to_csv('actividad_semana4.csv', index=True)
df

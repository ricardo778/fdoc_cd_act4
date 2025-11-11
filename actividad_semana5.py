import pandas as pd

datos = {
    'Nombre':  ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'Edad':    [25, 30, 22, None, 28],
    'Ciudad':  ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'Ingreso': [3000, 4500, 2800, 5000, None]
}

df = pd.DataFrame(datos)

# Guarda el dataset base para ejercicios de lectura/escritura
df.to_csv('actividad_semana5.csv', index=False)
df.head()

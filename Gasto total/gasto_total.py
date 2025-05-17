import pandas as pd

clientes = pd.DataFrame({
    'Cliente_id': [1013, 4563, 4675],
    'Nombre': ['Andres', 'Vanessa', 'Paulina'],
    'Email': ['andres@example.com', 'vanessa@example.com', 'paulina@example.com'],
    'Fecha_registro': ['2025-05-01', '2025-03-15', '2025-05-10']
})

productos = pd.DataFrame({
    'Producto_id': [1, 2, 3],
    'Nombre': ['Pan', 'Carne', 'Leche'],
    'Precio': [3000, 10000, 3500]
})

compras = pd.DataFrame({
    'Compra_Id': [1001, 1002, 1003],
    'Cliente_id': [1013, 4563, 4675],
    'Producto_id': [1, 2, 3],
    'Cantidad': [200, 150, 200],
    'Fecha_compra': ['2025-04-01', '2025-04-15', '2025-04-20']
})

compras_con_precios = compras.merge(productos, on='Producto_id')

compras_con_precios['Total'] = compras_con_precios['Cantidad'] * compras_con_precios['Precio']

gasto_por_cliente = compras_con_precios.groupby('Cliente_id')['Total'].sum().reset_index()

resultado = gasto_por_cliente.merge(clientes[['Cliente_id', 'Nombre']], on='Cliente_id')

print(resultado[['Cliente_id', 'Nombre', 'Total']])

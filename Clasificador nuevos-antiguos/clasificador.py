import pandas as pd
from datetime import datetime, timedelta

clientes=pd.DataFrame({
    'Cliente_id':[1013,4563,4675],
    'Nombre':['Andres','Vanessa','Paulina'],
    'Email': ['andres@example.com', 'vanessa@example.com', 'paulina@example.com'],
    'Fecha_registro': ['2025-05-01', '2025-03-15', '2025-05-10']
    
})

clientes['Fecha_registro']=pd.to_datetime(clientes['Fecha_registro'])
today=datetime.now()
clientes['Clasificacion']=clientes['Fecha_registro'].apply(
    lambda x:'Nuevo' if (today - x ).days <=30 else 'Antiguo'
)
print(clientes[['Cliente_id', 'Nombre', 'Fecha_registro', 'Clasificacion']])
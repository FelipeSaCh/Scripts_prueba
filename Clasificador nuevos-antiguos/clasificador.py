import pandas as pd
from datetime import datetime, timedelta

clients=pd.DataFrame({
    'Cliente_id':[1013,4563,4675],
    'Nombre':['Andres','Vanessa','Paulina'],
    'Fecha_registro': ['2025-04-20', '2025-03-01', '2025-05-10']
    
})

clients['Fecha_registro']=pd.to_datetime(clients['Fecha_registro'])
today=datetime.now()
clients['Clasificacion']=clients['Fecha_registro'].apply(
    lambda x:'Nuevo' if (today - x ).days <=30 else 'Antiguo'
)
print(clients[['Cliente_id', 'Nombre', 'Clasificacion']])

import pandas as pd
Data = pd.read_csv("Data.csv", index_col=None, header=None,  encoding='utf-8')
Camara = pd.read_csv('Camara.csv', header=None, index_col=None)


class New_Data(object):
    def __init__(self, Placas, Fecha, Hora, Longitud, Latitud, Pos):
        self.Fecha = Fecha
        self.Placas = Placas
        self.Hora = Hora
        self.Longitud = Longitud
        self.Latitud = Latitud
        self.Pos = Pos


nueva_Placa, nueva_Fecha, nueva_Hora,\
nueva_Latitud, nueva_Longitud, nueva_Pos = list(),list(),list(),list(),\
list(),list()
'''
Data[0] = Placas
Data[1] = Fecha
Data[2] = Hora
Data[3] = Pos
Camara[0] = Latitud
Camara[1] = Longitud
Camara[2] = Pos'''
# print(Data[4].str.upper())
Placas = Data[1].values
Placas = Placas[1::]
Fecha = Data[2]
Fecha = Fecha.str.split().values

Fecha = Fecha[1::]
Hora = Data[3].str.split().values
Hora = Hora[1::]
Longitud = Camara[1].values
Longitud = Longitud[1::]
Latitud = Camara[0].values
Latitud = Latitud[1::]
Data_upper = Data[4].str.upper().values
Data_upper = Data_upper[1::]
Camara_upper = Camara[2].str.upper().values
Camara_upper = Camara_upper[1::]
# print(Fecha[4][0])

# print(len(Camara_upper),Camara_upper[-1]==Data_upper[83])

for i in range(0, len(Camara_upper)):
    for j in range(0, len(Data_upper)):
        if Camara_upper[i] == Data_upper[j]:
            nueva_Placa.append(Placas[j])
            nueva_Fecha.append( Fecha[j][0])
            nueva_Hora.append(Hora[j][1])
            nueva_Latitud.append(Latitud[i])
            nueva_Longitud.append(Longitud[i])
            nueva_Pos.append(Camara_upper[i])
# Placa_df = pd.DataFrame('Placa', nueva_Placa)

Nueva_data = {'Placas':nueva_Placa, 'Fecha': nueva_Fecha, 'Hora':nueva_Hora,
            'Latitud': nueva_Latitud, 'Longitud':nueva_Longitud,
            'Posicion': nueva_Pos}
df = pd.DataFrame.from_dict(Nueva_data)


df=df.sort_values(by=['Posicion', 'Fecha', 'Hora', 'Latitud', 'Longitud', 'Placas'])
df.to_csv('Merge.csv', sep='\t', encoding='utf-8')

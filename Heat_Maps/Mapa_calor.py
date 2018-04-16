'''

'''

from flask import Flask, render_template, jsonify, request, redirect, g
from werkzeug import secure_filename
import pandas as pd
import numpy as np
import os
from flask_table import Table, Col

app = Flask(__name__, template_folder='template')

class Map_Heat():
    def __init__(self, prediccion):
        self.fecha = prediccion[0]
        self.placa = prediccion[4]
        self.long = prediccion[3]
        self.lat = prediccion[2]
        self.hora = prediccion[1]
        self.pos = prediccion[5]

class itemTable(Table):
    classes = ['table table-bordered table-hover table-striped', 'navbar navbar-default navbar-static-top']
    Fecha = Col('Fecha')
    Hora = Col('Hora')
    Placa = Col('Placa')
    Ubicacion = Col('Ubicacion')

class Item(object):
    def __init__(self, Fecha, Placa, Ubicacion, Hora):
        self.Fecha = Fecha
        self.Placa = Placa
        self.Ubicacion = Ubicacion
        self.Hora = Hora

dft = []
map_heat = list()
dicc_map = {}
ubicacion = list()
item = []
table = " "
entrenamiento=np.array(pd.read_csv('Data/Entrenamiento.csv',index_col=None ,header=None))
epoc=range(0,entrenamiento.shape[1])

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', inf=map_heat, infos=map_heat, dots=dicc_map, table=table,  entrenamiento=entrenamiento, epocasi=epoc,)
    #return render_template('basic-line.html')

@app.route('/upload', methods = ['POST'])
def upload():
    dft = []
    map_heat = list()
    dicc_map = {}
    ubicacion = list()
    item = []
    table = " "
    '''
    dft[0] = fecha
    dft[1] = Hora
    dft[2] = Lat
    dft[3] = Long
    dft[4] = Placas
    dft[5] = Pos
    Fecha, Placa, Ubicacion, Hora
    '''
    if request.method == 'POST':
        f = request.files['Subir archivo']
        dft = pd.read_csv(f,index_col=None ,header=None,dtype={\
            '0':np.dtype('U8'),'1':np.dtype('U8'), '2':np.float64, '3':np.float64,\
            '4':np.dtype('U6'), '5':np.dtype('U25')})
        for i in range(0,len(dft[0])):
            map_heat.append(Map_Heat(dft.values[i]))
        dicc_map = dft.to_dict("records")

        for k in range(0,len(dft[0])):
                item.append(Item(dft.values[k][0], dft.values[k][4],\
                dft.values[k][5], dft.values[k][1]))
        table = itemTable(item)


        # return redirect("/")
        return render_template('index.html', inf=map_heat, infos=map_heat, dots=dicc_map, table=table,  entrenamiento=entrenamiento, epocasi=epoc,)

if __name__ == '__main__':


    app.run()

from SQL import CRUD  # Importando as operações CRUD do módulo SQL
from asyncio import run  # Importando a função run para lidar com chamadas assíncronas

# Instanciando a classe CRUD
crud = CRUD()

class localize():
    def alpha(table,column):
        prod_name = []
        for i in range(len(run(crud.read(table,column)))):
            dictio = str(run(crud.read(table,column))[i])
            chase = dictio.find(": '")
            chase_end = dictio.find("'}")
            prod_name.append(dictio[chase+3:chase_end])
        return prod_name

    def number(table,column):
        prod_price = []
        for i in range(len(run(crud.read(table,column)))):
            dictio = str(run(crud.read(table,column))[i])
            chase = dictio.find("': ")
            chase_end = dictio.find("'}")
            prod_price.append(float(dictio[chase+3:chase_end]))
        return prod_price
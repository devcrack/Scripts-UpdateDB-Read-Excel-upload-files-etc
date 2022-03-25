import psycopg2
from psycopg2 import OperationalError
import pandas
import uuid
import re
import sys

def create_connection(db_name, db_user, db_password, db_endpoint):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_endpoint,
            port='5432',
        )
        print("Connection to DataBase succesful")
    except OperationalError as e:
        print(f"The error {e} occurred")
    return connection


def execute_query(connection, sql, val1, val2, val3, val4):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (val1, val2, val3, val4))
        return cursor.fetchall()
    except OperationalError as e:
        print(f"The error {e} ocurred")
        return None


def exe_query(connection, sql, val1, val2, val3, val4):
    """

    :param connection:
    :param sql: Cadena de consulta SQL
    :param val1: id
    :param val2: street
    :param val3: number
    :param val4: id HousingUnit
    :return: None
    """
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (val1, val2, val3, val4))
        connection.commit()
    except OperationalError as e:
        print(f"The error {e} ocurred")


def read_excel_as_matrix(sheet_name):
    # df = pandas.read_excel('CASETA.xlsx', usecols="B", skiprows=1, sheet_name='DANUBIO', )
    df = pandas.read_excel('DIRECCIONES.xlsx', usecols="A,B", skiprows=0, sheet_name=sheet_name, )
    return df.values


def write_houses(conection, housing_unit):
    houses = read_excel_as_matrix(housing_unit)

    id_housing_unit = 'f5ac6d40-bff7-4f4e-a583-45fdb05f7cae'
    for index in range(0, len(houses)):

        default = uuid.uuid4()
        default = str(default)
        number = str(houses[index][0])
        street = str(houses[index][1])
        street = street.strip()
        
        print(f"Calle->{street} Numero-> {number}")
        pre_sql = "INSERT INTO \"House_house\"(\"id\", \"street\", \"number\",\"idHousingUnit_id\") VALUES " \
                              "(%s,%s,%s,%s)"
        exe_query(conection, pre_sql, default, street, number, id_housing_unit)
        print(f"###{index}###")


if __name__ == '__main__':
    data_base_name = 'XXXXXX'
    data_base_user = 'XXXXXX'
    data_base_password = 'XXX-XXX-XXX'
    host = 'xXXX-XXXXXXXX'
    connect = create_connection(data_base_name, data_base_user, data_base_password, host)
    sheet_name = sys.argv[1]
    write_houses(connect, sheet_name)
    print("Cerrando Conexion")
    connect.close()

"""
"INSERT INTO "House_house" ("id", "street", "number", "idHousingUnit_id") VALUES ('DEFAULT', 'Las calabazas', '123', '2c34ad01-90f3-4540-9263-33707827cbcf');"
"""

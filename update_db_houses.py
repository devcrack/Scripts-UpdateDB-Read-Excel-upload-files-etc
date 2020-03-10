import psycopg2
from psycopg2 import OperationalError
import pandas
import uuid

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
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (val1, val2, val3, val4))
        connection.commit()
    except OperationalError as e:
        print(f"The error {e} ocurred")


def read_excel_as_matrix(sheet_name):
    # df = pandas.read_excel('CASETA.xlsx', usecols="B", skiprows=1, sheet_name='DANUBIO', )
    df = pandas.read_excel('CASETA.xlsx', usecols="B", skiprows=1, sheet_name=sheet_name, )
    return df.values


def write_houses(conection, housing_unit):
    houses = read_excel_as_matrix(housing_unit)
    index = 0
    for row in houses:
        for house in row:
            house = house.split("#")
            if len(house) != 2:
                print("ERROR")
                return
            street = house[0]
            number = house[1]
            default = uuid.uuid4()
            default = str(default)
            id_housing_unit = '2c34ad01-90f3-4540-9263-33707827cbcf'
            print(f"Creando House Data:{street} number {number} uid-> {default}")
            pre_sql = "INSERT INTO \"House_house\"(\"id\", \"street\", \"number\", \"idHousingUnit_id\") VALUES " \
                      "(%s,%s,%s,%s)"
            exe_query(conection, pre_sql, default, street, number, id_housing_unit)
        print()
        index = index + 1
        print(f"###{index}###")


if __name__ == '__main__':
    data_base_name = 'DB_NAME'
    data_base_user = 'XXXX'
    data_base_password = 'XXXX'
    host = 'XXXXX'
    connect = create_connection(data_base_name, data_base_user, data_base_password, host)

    write_houses(connect, 'TINTO')
    print("Cerrando Conexion")
    connect.close()


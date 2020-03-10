import psycopg2
from psycopg2 import OperationalError
import os

IMG_FOLDER_AVATAR = os.getcwd() + "/images/ine_atras/"


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




def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except OperationalError as e:
        print(f"The error {e} ocurred")
        return None




def update_avatar_route(connection ,route, user_name):
    cursor = connection.cursor()
    sql = "UPDATE \"Usuarios_customuser\" SET \"ine_atras\"=%s WHERE \"username\"=%s"
    cursor.execute(sql, (route, user_name))
    connection.commit()


def read_avatars_and_update(connection):
    content1 = os.listdir(IMG_FOLDER_AVATAR)
    for user_name in content1:
        content2 = IMG_FOLDER_AVATAR + user_name  # Ruta donde esta contenido el archivo
        content3 = os.listdir(content2) #Obtenemos el archivo
        upload_to = "images/" + user_name + "/" + content3[0]
        update_avatar_route(connection, upload_to, user_name)
        print(f"Avatar update to {upload_to}")



if __name__ == '__main__':
    data_base_name = 'IntrareEmpresa'
    data_base_user = 'blame711019'
    data_base_password = 'HIPIcc711019'
    host = 'intrare-freetierdb.c8dwggxf5yjq.us-east-2.rds.amazonaws.com'
    connect = create_connection(data_base_name, data_base_user, data_base_password, host)
    # update_avatar_route(connect, "images/524448431446/avatar.jpeg", "524448431446")
    read_avatars_and_update(connect)
    connect.close()
    print(connect)
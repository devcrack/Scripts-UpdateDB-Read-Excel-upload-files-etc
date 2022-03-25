import psycopg2
from psycopg2 import OperationalError
from urllib.request import urlretrieve
import os

# bucket_url = "https://intrareres.s3.amazonaws.com/static/"
bucket_url = "https://bucketeer-576c8228-7737-4878-8397-1c8403d07005.s3.amazonaws.com/"
IMG_FOLDER_AVATAR = os.getcwd() + "/images/Avatar/"
IMG_FOLDER_INE_FRENTE = os.getcwd() + "/images/ine_frente/"
IMG_FOLDER_INE_ATRAS = os.getcwd() + "/images/ine_atras/"


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


def check_folder(directory_path):
    folder = os.path.dirname(directory_path)
    if not os.path.exists(folder):
        print(f"Directory:{folder} CREATED")
        os.makedirs(folder)



def download_front_id(data):
    """
    Estructura de Directorio:
    /root/ -> /images/ -> /ine_frente/ -> /username/
    :param data:
    :return:
    """
    i = 0
    for folder, single in data:
        user_data = single
        if len(user_data) > 0:
            user_data = str(user_data)
            split_data = user_data.split("/")
            # user_directory = split_data[len(split_data) - 2]
            file_name = split_data[len(split_data) - 1]  # Nombre del archivo

            user_directory = IMG_FOLDER_INE_FRENTE + str(folder) + "/"
            check_folder(user_directory) # Si el directorio no existe se crea
            if "+" in user_data:
                user_data = user_data.replace("+", "%2B")
            elif "@" in user_data:
                user_data = user_data.replace("@", "%40")
            file_to_write = user_directory + file_name
            url_to_download = bucket_url + user_data
            urlretrieve(url_to_download, file_to_write)
            print(f"Download File ->{file_to_write}")
            i = i + 1
    print(f"Total downloaded FRONT ID = {i}")


def download_back_id(data):
    """
       Estructura de Directorio:
       /root/ -> /images/ -> /ine_atras/ -> /username/
       :param data:
       :return:
       """
    i = 0
    for folder, single in data:
        user_data = single
        if len(user_data) > 0:
            user_data = str(user_data)
            split_data = user_data.split("/")
            # user_directory = split_data[len(split_data) - 2]
            file_name = split_data[len(split_data) - 1]

            user_directory = IMG_FOLDER_INE_ATRAS + str(folder) + "/"
            check_folder(user_directory)  # Si el directorio no existe se crea
            if "+" in user_data:
                user_data = user_data.replace("+", "%2B")
            elif "@" in user_data:
                user_data = user_data.replace("@", "%40")
            file_to_write = user_directory + file_name
            url_to_download = bucket_url + user_data
            urlretrieve(url_to_download, file_to_write)
            print(f"Download File ->{file_to_write}")
            i = i + 1
    print(f"Total downloaded BACK ID = {i}")


def download_avatars(data):
    i = 0
    for folder, single_data in data:
        user_data = single_data  # Nombre del archivo
        user_data = str(user_data)
        if "images" in user_data:
            split_data = user_data.split("/")
            # user_directory = split_data[len(split_data) - 2]
            file_name = split_data[len(split_data) - 1]  # Obtenemos el Nombre del Archivo

            user_directory = IMG_FOLDER_AVATAR + str(folder) + "/"
            check_folder(user_directory)  # Si el directorio no existe se crea
            if "+" in user_data:
                user_data = user_data.replace("+", "%2B")
            elif "@" in user_data:
                user_data = user_data.replace("@", "%40")
            file_to_write = user_directory + file_name
            url_to_download = bucket_url + user_data
            print(f"File to download->{url_to_download}")
            urlretrieve(url_to_download, file_to_write)
            # print(f"Download File ->{file_to_write}")
            i = i + 1
    print(f"Total downloaded BACK ID = {i}")


if __name__ == '__main__':
    data_base_name = 'XXXXXXX'
    data_base_user = 'xXXXxxxx'
    data_base_password = 'Xxxxxxx'
    host = 'XxxxxXxxxx'
    connect = create_connection(data_base_name, data_base_user, data_base_password, host)
    print(connect)
    # query = "SELECT \"username\", \"avatar\" from \"Usuarios_customuser\" WHERE \"is_active\"=true;"
    # query = "SELECT \"username\", \"ine_frente\" from \"Usuarios_customuser\" WHERE \"is_active\"=true;"
    query = "SELECT \"username\", \"ine_atras\" from \"Usuarios_customuser\" WHERE \"is_active\"=true;"
    result = execute_query(connect, query)
    # download_avatars(result)
    # download_front_id(result)
    download_back_id(result)


    connect.close()
    print(connect)

"""
Consultar avatar de aquellos que estan activos
IntrareEmpresa=> SELECT "avatar" from "Usuarios_customuser" WHERE "is_active"=true;


"""

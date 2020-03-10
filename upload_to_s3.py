import os
import sys
import boto3
import mimetypes


IMG_FOLDER_AVATAR = os.getcwd() + "/images/Avatar/"
IMG_FOLDER_INE_FRENTE = os.getcwd() + "/images/ine_frente/"
IMG_FOLDER_INE_ATRAS = os.getcwd() + "/images/ine_atras/"

AWS_ACCESS_KEY_ID = 'XXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'xxXXXXXxxxxxXX'
AWS_STORAGE_BUCKET_NAME ='xxxxxxxxxx'


def s3_session():
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID , aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    return session


def upload_file(dir_name, file, file_mime):
    s3 = s3_session()
    s3 = s3.resource('s3')
    s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=dir_name, Body=file, ContentType=file_mime)




def read_picture(path_file):
    file = None
    try:
        file = open(path_file, "rb")
        picture = file.read()
        return picture
    except IOError as e:
        print(f"Error {e.args[0]}, {e.args[1]}")
        sys.exit(1)
    finally:
        if file:
            file.close()


def read_avatars_and_upload():
    content1 = os.listdir(IMG_FOLDER_INE_ATRAS)
    for user_name in content1:
        id = user_name  # Por convencion el ID es el nombre del directorio
        content2 = IMG_FOLDER_INE_ATRAS + user_name  # Ruta donde esta contenido el archivo
        content3 = os.listdir(content2)
        # print(content3[0])
        file = content2 + "/" + content3[0]
        print(f"Archivo{file}")
        picture = read_picture(file)  # En este punto ya tenemos cargada la imagen que queremos escribir en la base de datos
        upload_to = "images/" + id + "/" + content3[0]
        file_mime = mimetypes.guess_type(file)[0]
        upload_file(upload_to, picture, file_mime)
        print(f"Uploaded to {upload_to}")


if __name__ == '__main__':
    read_avatars_and_upload()






















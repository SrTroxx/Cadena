import boto3

s3 = boto3.client('s3')
bucket = 'mi-bucket'
archivo_local = 'ruta/al/archivo.txt'
archivo_remoto = 'carpeta/archivo.txt'

try:
    s3.upload_file(archivo_local, bucket, archivo_remoto)
    print("Archivo subido exitosamente")
except Exception as e:
    print("Error al subir el archivo:", e)

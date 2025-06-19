import boto3

s3 = boto3.client('s3')
bucket = 'mi-bucket'
archivo_remoto = 'carpeta/archivo.txt'
archivo_local = 'ruta/de/descarga/archivo.txt'

try:
    s3.download_file(bucket, archivo_remoto, archivo_local)
    print("Archivo descargado exitosamente")
except Exception as e:
    print("Error al descargar el archivo:", e)

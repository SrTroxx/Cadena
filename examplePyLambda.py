def lambda_handler(event, context):
    # Extrae un parámetro 'nombre' del evento
    nombre = event.get("nombre", "mundo")
    return {"mensaje": f"Hola, {nombre}!"}

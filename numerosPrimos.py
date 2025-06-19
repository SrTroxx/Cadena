def es_primo(n):
    """Determina si un número entero es primo."""
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un entero.")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Sólo iterar sobre impares hasta la raíz cuadrada
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def suma_primos(lista):
    """
    Recibe una lista de enteros y retorna la suma de los números primos.
    Lanza una excepción si la entrada no es una lista.
    """
    if not isinstance(lista, list):
        raise ValueError("La entrada debe ser una lista de enteros.")
    # Usar suma y generator expresion para eficiencia
    return sum(n for n in lista if isinstance(n, int) and es_primo(n))

# Ejemplo de uso:
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Suma de primos:", suma_primos(entrada))  # Salida: 17

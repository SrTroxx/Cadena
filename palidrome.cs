using System;
using System.Text.RegularExpressions;

class Program
{
    static bool EsPalindromo(string texto)
    {
        if (string.IsNullOrWhiteSpace(texto))
        {
            // Consideramos que una cadena vacía o solo espacios no es un palíndrome válido
            throw new ArgumentException("La entrada no puede estar vacía o solo contener espacios.");
        }

        // Eliminar espacios, signos de puntuación y convertir a minúsculas
        string limpio = Regex.Replace(texto.ToLower(), @"[^a-z0-9]", "");
        char[] arreglo = limpio.ToCharArray();
        Array.Reverse(arreglo);
        string reverso = new string(arreglo);
        return limpio.Equals(reverso);
    }

    static void Main()
    {
        Console.WriteLine("Ingrese una cadena:");
        string entrada = Console.ReadLine();
        try
        {
            bool resultado = EsPalindromo(entrada);
            Console.WriteLine(resultado);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

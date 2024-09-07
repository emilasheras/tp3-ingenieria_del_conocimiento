# 1. Crea un código que imprima en pantalla la expresión:
#    "Mi Primer Código En Python."
print("\n\n")
print("Mi Primer Código En Python")
print("\n")

# 2. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿Qué estás estudiando?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
response = input("¿Qué estás estudiando? (responde a continuación): ")
print(response)
print("\n")

# 3. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿En qué país vives?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
country = input("¿En qué país vives? (responde a continuación): ")
print(country)
print("\n")

# 4. Declara dos variables llamadas `nombre` y `edad`.
#    Asigna a `nombre` el valor "David Bowman" y a `edad` el valor 51.
nombre = "David Bowman"
edad = 51
print("nombre: "+nombre)
print("\n")
print("edad: "+str(edad))
print("\n")

# 5. Crea tres variables: `nombre`, `apellido`, `nombrecompleto`.
#    A `nombre` asígnale el valor "Julia" y en `apellido` el valor "Roberts".
#    Finalmente construye `nombrecompleto` concatenando las variables (recuerda sumar un espacio intermedio).
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print("nombrecompleto: "+nombrecompleto)
print("\n")

# 6. Declara la variable `materia` y asígnale el valor "Ingeniería del conocimiento".
#    Muestra en pantalla la frase: "Estás estudiando 'materia'" (concatenando).
subject = "Ingeniería del conocimiento"
print("(hardcoded) Estás estudiando " + subject)
print("\n")

# 7. Convierte el valor de `num1` (num1=35) en un int e imprime el tipo de dato que resulta.
num1 = 35
num1 = int(num1)
print("the int type is: ")
print(type(num1))
print("\n")

# 8. Imprime el nombre y número de asociado dentro de la siguiente frase:
#    "Estimado/a (nombre_asociado) su número de asociado es: (numero_asociado)".
member_name = "John Doe"
member_number = 12345
print(f"Estimado/a {member_name}, su número de asociado es: {member_number}")
print("\n")

# 9. Muestra en pantalla el cociente (división al piso) de los siguientes dos números:
#    874 dividido entre 27. Debes mostrar solo el valor numérico que resulta de esta operación.
result = 874 // 27 # <- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print(result)
print("\n")

# 10. Redondea el número 10.676767 al entero más próximo y muestra en pantalla el resultado.
rounded_number = round(10.676767)
print("rounded number is: "+str(rounded_number))
print("\n")

# 11. Gestión de inventario con tuplas:
#     Una tienda tiene un inventario de productos. Cada producto tiene un nombre, precio y cantidad disponible.
#     Representa cada producto como una tupla (nombre, precio, cantidad).
#     Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# 1. Crea un código que imprima en pantalla la expresión:
#    "Mi Primer Código En Python."
print("Mi Primer Código En Python")

# 2. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿Qué estás estudiando?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
response = input("¿Qué estás estudiando? (responde a continuación): ")
print(response)

# 3. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿En qué país vives?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
country = input("¿En qué país vives? (responde a continuación): ")
print(country)

# 4. Declara dos variables llamadas `nombre` y `edad`.
#    Asigna a `nombre` el valor "David Bowman" y a `edad` el valor 51.
name = "David Bowman"
age = 51

# 5. Crea tres variables: `nombre`, `apellido`, `nombrecompleto`.
#    A `nombre` asígnale el valor "Julia" y en `apellido` el valor "Roberts".
#    Finalmente construye `nombrecompleto` concatenando las variables (recuerda sumar un espacio intermedio).
first_name = "Julia"
last_name = "Roberts"
full_name = first_name + " " + last_name

# 6. Declara la variable `materia` y asígnale el valor "Ingeniería del conocimiento".
#    Muestra en pantalla la frase: "Estás estudiando 'materia'" (concatenando).
subject = "Ingeniería del conocimiento"
print("Estás estudiando " + subject)

# 7. Convierte el valor de `num1` (num1=35) en un int e imprime el tipo de dato que resulta.
num1 = 35
num1 = int(num1)
print("the int type is: ")
print(type(num1))

# 8. Imprime el nombre y número de asociado dentro de la siguiente frase:
#    "Estimado/a (nombre_asociado) su número de asociado es: (numero_asociado)".
member_name = "John Doe"
member_number = 12345
print(f"Estimado/a {member_name}, su número de asociado es: {member_number}")

# 9. Muestra en pantalla el cociente (división al piso) de los siguientes dos números:
#    874 dividido entre 27. Debes mostrar solo el valor numérico que resulta de esta operación.
result = 874 // 27
print(result)

# 10. Redondea el número 10.676767 al entero más próximo y muestra en pantalla el resultado.
rounded_number = round(10.676767)
print("rounded number is: ")
print(rounded_number)

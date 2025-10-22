# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


if __name__ == "__main__":
    print("=== Calculadora básica ===")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")

    op = input("Elige una operación: ").strip().lower()
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    if op == "suma":
        print("Resultado:", suma(a, b))
    elif op == "resta":
        print("Resultado:", resta(a, b))
    elif op == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif op == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida.")

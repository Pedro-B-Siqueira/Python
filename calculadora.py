# python
def variavel_conta(form):
    match form:
        case "+":
            return "+"
        case "-":
            return "-"
        case "x":
            return "*"
        case "/":
            return "/"
        case _:
            print( "Valor inválido...")

def calculadora(a, form, b):
    resultado = eval(f"{a} {form} {b}")
    return resultado

a = int(input("Num 1: "))
form = input("Qual será sua conta? (+, -, x, /): ")
b = int(input("Num 2: "))

form = variavel_conta(form)
resultado = calculadora(a, form, b)
print(f"Resposta: {resultado}")

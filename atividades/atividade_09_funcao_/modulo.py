# bibliotecas
import math

# funcoes

def primeiro_grau(a, b):
    x = -b/a 
    return x

def segundo_grau(a, b, c):
    delta = (b**2)-(4*a*c)

    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        yield f"x' = {x1}"
        yield f'x" = {x2}'
    elif delta == 0:
        x = -b/(2*a)
        yield f"Raiz única: x = {x}"
    else:
        yield f"Não há raízes reais"
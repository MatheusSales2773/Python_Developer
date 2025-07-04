# Programa que exibe a data e hora de hoje

from datetime import date
import datetime

hoje = date.today().strftime("%d/%m/%Y")
hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

print(hoje)
print(hora_atual)
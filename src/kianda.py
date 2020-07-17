from os import sys
from essencial.configuracao import Kiandavel
from editor import grafico
from editor import consola


Kianda = None

if sys.argv[1] == "-g":
    Kianda = grafico.Aplicativo
elif sys.argv[1] == "-c":
    ## Codigo para ediçao na Consola/Terminal
    pass

if Kianda != None:
    try:
        if isinstance(Kianda, Kiandavel):
            Kianda.lancar()
        else:
            raise SystemError("O objecto deve herdar da class Kiandavel")
    except SystemError as erro:
        print("Erro : O editor nao pode ser lançado ")
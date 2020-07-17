from editor import grafico
from os import sys

Editor = None

if sys.argv[1] == "g":
    Editor = grafico.Editor()
    
elif sys.argv[1] == "c":
    ## Codigo para ediçao na Consola/Terminal
    pass

if Editor != None:
    Editor.lancar()
from essencial.edicao import Editavel
import tkinter as tk
import tkinter.messagebox as msg
from .entrada_grafica import InterpretadorGrafico, Evento


class EditorAreaTexto(Editavel,tk.Text):
    interpretador = None
    def __init__(self,master, *args, **kwargs):
        Editavel.__init__(self,None)
        tk.Text.__init__(self,master, *args, **kwargs)
        self.master = master
        self.config(wrap=tk.WORD)  # CHAR NONE

        self.tag_configure('find_match', background="yellow")
        self.find_match_index = None
        self.find_search_starting_index = 1.0
        self.mapagem_comandos()

    def mapagem_comandos(self):
        eventos = [Evento('<Control-a>', self.selectionar),
                   Evento('<Control-c>', self.copiar),
                   Evento('<Control-v>', self.colar),
                   Evento('<Control-x>', self.cortar),
                   Evento('<Control-y>', self.refazer),
                   Evento('<Control-z>', self.desfazer)
                  ]
        self.interpretador = InterpretadorGrafico(eventos) 
        for evento in self.interpretador.obterComandos():
            self.bind(evento.acao,evento.reacao)
    def inserir(self,conteudo=None):
        #codigo
        pass
    
    def selectionar(self,inicio=None,fim=None):
        self.tag_add("sel", 1.0, tk.END)
        return "break"
    
    def copiar(self,inicio,fim):
        self.event_generate("<<Copy>>")
        return "break"
    
    def cortar(self,inicio=None,fim=None):
        self.event_generate("<<Cut>>")
        return "break"
    
    def colar(self,inicio =None,fim=None):
        self.event_generate("<<Paste>>")
        return "break"
    
    def desfazer(self):
        self.event_generate("<<Undo>>")
        return "break"
    
    def refazer(self):
        self.event_generate("<<Redo>>")
        return "break"
    
    def procurar(self,conteudo=None,procurador=None):
        text_to_find = conteudo
        length = tk.IntVar()
        idx = self.search(text_to_find, self.find_search_starting_index, stopindex=tk.END, count=length)

        if idx:
            self.tag_remove('find_match', 1.0, tk.END)

            end = f'{idx}+{length.get()}c'
            self.tag_add('find_match', idx, end)
            self.see(idx)

            self.find_search_starting_index = end
            self.find_match_index = idx
        else:
            if self.find_match_index != 1.0:
                if msg.askyesno("No more results", "No further matches. Repeat from the beginning?"):
                    self.find_search_starting_index = 1.0
                    self.find_match_index = None
                    return self.procurar(text_to_find)
            else:
                msg.showinfo("No Matches", "No matching text found")

    
    def substituir(self,antigoConteudo=None,novoConteudo=None,substituidor=None):
        target = antigoConteudo
        replacement = novoConteudo
        if self.find_match_index:
            current_found_index_line = str(self.find_match_index).split('.')[0]

            end = f"{self.find_match_index}+{len(target)}c"
            self.replace(self.find_match_index, end, replacement)

            self.find_search_starting_index = current_found_index_line + '.0'
 
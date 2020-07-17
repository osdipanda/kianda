from essencial.entrada import Evento,Interpretavel

class InterpretadorGrafico(Interpretavel):
    comandos = [] ## Lista de eventos
    def __init__(self,listaEventos):
        self.comandos = listaEventos

    def adicionar_comando(self,acao,reacao):
        try:
            if self.existe(acao):
                raise Exception
            self.comandos.append(Evento(acao,reacao))
        except:
            raise Exception
    
    def existe(self,acao):
        for evento in self.comandos:
            if evento.acao == acao:
                return True
        return False

    def obter_reacao(self,acao):
        ##codio para testar se um evento foi implementado, se uma açao tém uma reçao
        ## deve retornar reaçao(funçao) se a açao existe
        pass
    
    def obterComandos(self):
        return self.comandos
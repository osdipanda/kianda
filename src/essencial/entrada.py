from abc import abstractmethod, ABC

## classe que representa a mapagem/binding de uma tecla/combinaçao à uma funçao especifica
class Evento(object):
    acao= None # Tecla especifica do teclado
    reacao = None ## funçao que vai reagir
    def __init__(self,acao,reacao):
        self.acao = acao
        self.reacao = reacao
    
## classe que representa o interpretador de comandos, deve ser herdada
class Interpretavel(ABC):
    comandos = [] ## Lista de eventos
    def __init__(self,listaEventos):
        self.comandos = listaEventos

    def adicionar_comando(self,acao,reacao):
        try:
            ## Testar se a açao ainda nao existe
            self.comandos.append(Evento(acao,reacao))
        except:
            pass

    @abstractmethod
    def existe(self,acao):
        ##codio para testar se um evento foi implementado, se uma açao tém uma reçao
        ## deve retornar True/False
        pass
    
    @abstractmethod
    def obter_reacao(self,acao):
        ##codio para testar se um evento foi implementado, se uma açao tém uma reçao
        ## deve retornar reaçao(funçao) se a açao existe
        pass

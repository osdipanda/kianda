from abc import abstractmethod, ABC

## class deve ser herdada por um modulo que deseja ser extensivél, flexivél
class Extensivel(ABC):
    def __init__(self, extensao):
        self.extensao = extensao
    @abstractmethod
    def instalar(self):
        ## codigo para instalar a extensao
        pass

## class que representa os criterios de uma extensao
class Extensao(object):
    ## Precisamos definir o Conceito de extensao
    pass

## class deve ser herdada e implementada por um modulo representando
## um tipo de editor consola/grafico etc
## um modulo que se comportar como uma interface de ediçao
## pode se dizer Kiandavél
class Kiandavel(ABC):
    
    @abstractmethod
    def pre_lancamento(self):
        ## Poe teu codigo de lançamento aqui
        ## Incializaçoes etc 
        pass
    def lancar(self):
        self.pre_lancamento()
        self.instalar_extensoes()
        
    def instalar_extensoes(self):
        ## codigo
        pass




    
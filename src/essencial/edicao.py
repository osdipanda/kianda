from abc import abstractmethod, ABC
## todo modulo que executa ediçao num dado certo conteudo deve herdar esta classe

class Editavel(ABC):
    buffer_edicao = None
    def __init__(self,buffer=None,**kw):
        self.buffer_edicao = buffer

    @abstractmethod
    def inserir(self,conteudo):
        pass
    @abstractmethod
    def selectionar(self,inicio,fim):
        #codigo
        pass
    @abstractmethod
    def copiar(self,inicio,fim):
        #codigo
        pass
    @abstractmethod
    def cortar(self,inicio,fim):
        #codigo
        pass
    @abstractmethod
    def colar(self,inicio,fim):
        pass
    @abstractmethod
    def desfazer(self):
        #codigo
        pass
    @abstractmethod
    def refazer(self):
        #codigo
        pass
    @abstractmethod
    def procurar(self,conteudo,procurador=None):
        #codigo
        pass
    @abstractmethod
    def substituir(self,antigoConteudo,novoConteudo,substituidor=None):
        #codigo
        pass
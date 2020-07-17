from abc import abstractmethod,ABC
## todo modulo que deseja mostrar/apresentar num dado certo conteudo para o usuario deve herdar esta classe

class Apresentavel(ABC):
    buffer_apresentacao = None
    opcoes = {}
    def __init__(self,buffer,opcoes={}):
        # opçoes pode ser , qual pagina mostrar, apartir de qual linha etc... opcoes={'pagina':1,cursor={'linha':3,'coluna':2},}
        self.buffer_apresentacao = buffer
    @abstractmethod
    def mostrar(self):
        ## codigo
        ## filtrar o que deve ser mostrado baseando-se nas opçoes 
        pass

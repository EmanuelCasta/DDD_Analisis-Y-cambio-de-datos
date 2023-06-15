from abc import ABCMeta
from abc import abstractmethod
import pandas as pd

class IBlocNotas(metaclass=ABCMeta):

        @abstractmethod
        def agregarColumnasPersonalizables(self,**kwargs)->None:
                pass

        @abstractmethod
        def agregarLogicaParametros(self,df:pd.DataFrame)->None:
                pass

        @abstractmethod
        def obtenerDataSet(self)->pd.DataFrame:
                pass

        @abstractmethod
        def convetirYexportar(self,nombreDocumento:str,extension:str)->None:
                pass

      
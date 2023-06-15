from blocNotas.domain.repo.blocNotesrespository import IBlocNotas
from blocNotas.domain.entidades.DatoEmpresaria import DatoEmpresarial
from module.ORMPandas.PandasRepository import PandasRespository
import os


import pandas as pd

class BlocNotasImpl(IBlocNotas):
        
        def __init__(self,nombreArchivo:str) -> None:
                self._typeDfRepository : PandasRespository[DatoEmpresarial] =PandasRespository[DatoEmpresarial](DatoEmpresarial(pd.DataFrame()),nombreArchivo)
                self._typeDfRepository.df = self._typeDfRepository.read()
       
        def agregarColumnasPersonalizables(self,**kwargs)->None:
                self._typeDfRepository.df = DatoEmpresarial(self._typeDfRepository.df,change=True,**kwargs).df
                
      
        def agregarLogicaParametros(self,df:pd.DataFrame)->None:
                self._typeDfRepository.df =df
        

        def obtenerDataSet(self)->pd.DataFrame:
                return self._typeDfRepository.df

        def convetirYexportar(self,nombreDocumento:str)->None:
                self._typeDfRepository.saveExcel(nombreDocumento)
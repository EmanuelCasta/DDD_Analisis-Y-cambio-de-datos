from typing import TypeVar,Generic
import pandas as pd

T = TypeVar('T')

class PandasRespository(Generic[T]):
        def __init__(self,valor:T,nombreDocumento:str):
                self.valor = valor
                if "csv" in nombreDocumento.split("."):
                        self.df:pd.DataFrame=pd.read_csv(nombreDocumento,encoding='ISO-8859-1')
                else:
                        try:
                                self.df:pd.DataFrame=pd.read_csv(nombreDocumento,sep=";",low_memory=False)
                        except:
                                print("Intentando abrir el archivo..")
                                try:
                                        self.df:pd.DataFrame=pd.read_csv(nombreDocumento, sep=";", encoding="ISO-8859-1")
                                except:
                                        print("Por favor ingresar el archivo con separacion ;")
                                        input("Presionar Enter para cerrar el programa")
                                        exit()
                
                        
                
        
        def obtener_valor(self)->T:
                return self.valor
        
        def read(self)->pd.DataFrame:
                return self.df

        def saveExcel(self,nombre:str):
                self.df.to_excel(nombre.strip()+".xlsx") 

       
        
        

        

        
        
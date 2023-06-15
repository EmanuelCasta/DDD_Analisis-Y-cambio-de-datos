from blocNotas.domain.repo.blocNotesrespository import  IBlocNotas
from collections import *
import pandas as pd
import numpy as np
from colorama import init, Fore, Back, Style,Cursor
import re


class blocNotesImple:
    
        def __init__(self,injectBlocNotes:IBlocNotas) -> None:
                self._blocNotasRespository:IBlocNotas =  injectBlocNotes

        def obtenerTodoElDataset(self)->pd.DataFrame:
                return self._blocNotasRespository.obtenerDataSet()
        
        def agregarColumnasPersonalizables(self,**kwargs):
                dictName= {}
                for key,value  in  kwargs.items():
                        dictName[key] = str(value).upper().strip()
                self._blocNotasRespository.agregarColumnasPersonalizables(**kwargs)
        
        def agregarLogicaParametros(self,parametersCompareted:str,columnsTotal:str,countParamaeterCompareted:str)->pd.DataFrame:
                # En este caso parametersCompareted:  NPN 
                # En este caso columna total de esos pametro , columnsTotal:  TOTAL_REGISTRO
                # Reconteo del NPN que seria llamado countParamaeterCompareted : NUMERO_DE_ORDEN
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                df[parametersCompareted] = df[parametersCompareted].astype("str")

                # Calcula el conteo total para cada valor en 'parametersCompareted'
                df[columnsTotal] = df.groupby(parametersCompareted)[parametersCompareted].transform('count')

                # Calcula el conteo acumulativo para cada valor en 'parametersCompareted'
                df = df.sort_values(by=parametersCompareted).reset_index(drop=True)
                df[countParamaeterCompareted] = df.groupby(parametersCompareted).cumcount()+1
                """ 
                df[columnsTotal] = 0
                df[countParamaeterCompareted] = 0
                ## Quitar
                
                # Hacer una validador si no existe esas variables

                df[parametersCompareted] = df[parametersCompareted].astype("str")
                counters= Counter(list(df[parametersCompareted].values))

                guardado = ""
                df =df.sort_values(by=parametersCompareted).reset_index(drop=True)
                for i in range(len(df)):
                        df.loc[i,columnsTotal] = counters.get(df.loc[i,parametersCompareted])
                        if guardado == df.loc[i,parametersCompareted]:
                                df.loc[i,countParamaeterCompareted] = df.loc[i-1,countParamaeterCompareted] +1
                        else:
                                df.loc[i,countParamaeterCompareted] =   df.loc[i,countParamaeterCompareted] +1
                        guardado = df.loc[i,parametersCompareted]"""

                self._blocNotasRespository.agregarLogicaParametros(df)
        
        def ponerTodasLasColumnasMay(self)->None:
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                df.columns = df.columns.str.upper().str.strip()
                self._blocNotasRespository.agregarLogicaParametros(df)
        
        def agregarColumas(self,**kwargs)->None:
                df:pd.DataFrame =self._blocNotasRespository.obtenerDataSet()
                for key,value  in  kwargs.items():
                        df[key] = str(value).upper().strip()
                self._blocNotasRespository.agregarLogicaParametros(df)

        def obtenerNombreColumnas(self)->list:
                return self._blocNotasRespository.obtenerDataSet().columns       

        def exportarDocumento(self,nombreDocumento:str):
                try:
                        self._blocNotasRespository.convetirYexportar(nombreDocumento)
                except:
                        def clean_text(text):
                                if pd.isna(text):  # si el valor es NaN, devolver tal cual
                                        return text
                                else:  # si no, eliminar caracteres no permitidos
                                        return re.sub(r'[^\x20-\x7E]', '', str(text))
                        print(Fore.LIGHTRED_EX+"[ADVERTENCIA GRAVE]"+Style.RESET_ALL+" Hubo problemas con la exportacion ya que el documento no tiene enconding UTF-8, se tratara de solucionar el problema eliminando algunos caracteres no permitidos en excel")
                        df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                        df = df.applymap(clean_text)
                        self._blocNotasRespository.agregarLogicaParametros(df)
                        self._blocNotasRespository.convetirYexportar(nombreDocumento)
                        
     


        def seleccionarColumnas(self,**kwargs):
                self._blocNotasRespository.agregarLogicaParametros(self._blocNotasRespository.obtenerDataSet()[kwargs.values()])

        def agregarLogicaFecha(self,column:str):
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                if column in list(df.columns):
                        try:
                                try:
                                        df[column]  =pd.to_datetime(df[column], format="%d/%m/%y").dt.strftime("%Y-%m-%d")
                                except:
                                        try:
                                                df[column]  =pd.to_datetime(df[column], format="%d/%m/%y").dt.strftime("%y-%m-%d")
                                        except:
                                                try:
                                                        df[column]  =pd.to_datetime(df[column], format="%d/%m/%y").dt.strftime("%Y-%M-%D") 
                                                except: 
                                                        print("El formato no corresponde ya que su valor es "+df[column].loc[0] +" donde el formato correspondiente minimo debe estar formulado como xxxx-xx-xx")
                        except:
                                print("El formato no corresponde ya que su valor es ",df[column].loc[0] ," donde el formato correspondiente minimo debe estar formulado como xxxx-xx-xx")
                        self._blocNotasRespository.agregarLogicaParametros(df)
                else:
                        print("No existe la columna "+column)

        def rellenarFechasVacias(self,column:str,fecha:str="1900-01-01"):
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                if column in list(df.columns):
                        df[column] = np.where(df[column].isnull(),fecha,df[column])
                        self._blocNotasRespository.agregarLogicaParametros(df)
                else:
                        print("No existe la columna "+column)

        def tipoDeDato(self,column:str ,tipo:str,default:bool=True)->bool:
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                if default:
                        try:
                                df["AREATERR"]  = df["AREATERR"].str.replace(",",".").astype(float)
                                df["PK_PREDIO"]  = df["PK_PREDIO"].astype("str")
                                self._blocNotasRespository.agregarLogicaParametros(df)
                                return True
                        except:
                                input(Fore.RED+"[ERROR]"+Style.RESET_ALL+" No existe los nombres AREATERR, PK_PREDIO por ende no se puede hacer la modificacion por defecto por favor realiza una operacion manual.. Presiona ENTER para finalizar")
                                return False
                tipo_dato = ["str","float"]
                if not tipo in tipo_dato:
                        input(Fore.RED+"[ERROR]"+Style.RESET_ALL+" No existe ningun tipo de dato "+tipo+"  Presiona ENTER para finalizar")
                        return False
                try:
                        df = df.astype(str)
                        if tipo =="float":
                               
                                if "."  in df[column].values[0]:
                                        df[column]  = df[column].astype(float)
                                else:
                                        df[column]  = df[column].str.replace(",",".").astype(float)
                        if tipo =="str":
                                df[column]  = df[column].astype("str")
                        self._blocNotasRespository.agregarLogicaParametros(df)
                        return True
                except Exception :
                                print(df.columns)
                                
                                print(Fore.RED+"[ERROR]"+Style.RESET_ALL+" No existe los nombres "+column+" por ende no se puede hacer la modificacion por defecto por favor realiza una operacion manual.")
                                input(Fore.RED+"[ERROR]"+Style.RESET_ALL+" El error tambien puede ser el dato no puede ser convertido. Presiona ENTER para finalizar")
                                
                                return False
        
        def concatenar(self,column:str,columnNew:str,default=True)->bool:
                df:pd.DataFrame = self._blocNotasRespository.obtenerDataSet()
                if default:
                        try:
                                df["NOMBRE"] = (df['NOMBRE'].astype(str).str.strip()+' '+df['APELLIDOS1'].astype(str).str.strip()+' '+df['APELLIDOS2'].astype(str).str.strip()).str.strip()
                                self._blocNotasRespository.agregarLogicaParametros(df)
                                return True
                        except:
                                print("Error al concatenar")
                                return False
                else:
                        df[column] = df[column].astype(str)
                        df[columnNew] = df[columnNew].astype(str)
                        df[column] = (df[column].str.strip()+'  ' +df[columnNew].str.strip()).str.strip()
                        df.drop([columnNew], axis=1,inplace=True)
                        self._blocNotasRespository.agregarLogicaParametros(df)
                        return True

                


                


        



from blocNotas.domain.services.blocNotesserviceImpl import blocNotesImple

class BlocNotasApplication():
        def __init__(self,blocService:blocNotesImple) -> None:
                self.blocService:blocNotesImple  = blocService


        def ponerTodasEnMayuscula(self)->None:
                self.blocService.ponerTodasLasColumnasMay()

        def agregarColumnasPersonalizables(self,**kwargs)->None:
                self.blocService.agregarColumnasPersonalizables(**kwargs)
                
        def  agregarLogicaConteo(self,parametersCompareted:str,columnsTotal:str,countParamaeterCompareted:str)->bool:
                # En este caso parametersCompareted:  NPN 
                # En este caso columna total de esos pametro , columnsTotal:  TOTAL_REGISTRO
                # Reconteo del NPN que seria llamado countParamaeterCompareted : NUMERO_DE_ORDEN
                if parametersCompareted == "" or columnsTotal == "" or countParamaeterCompareted == "":
                        return False

                if parametersCompareted == None or columnsTotal == None or countParamaeterCompareted == None:
                        return False

                self.blocService.agregarLogicaParametros(parametersCompareted,columnsTotal,countParamaeterCompareted)
                return True

        def seleccionarColumnas(self,seleccionarColumnas:list)->None:
                columnasNombre:list =seleccionarColumnas
                dicColum={}
                for name in columnasNombre:
                        dicColum[name] = name
                self.blocService.seleccionarColumnas(**dicColum)
        
        def exportar(self,nombreDelArchivo:str)->None:
                self.blocService.exportarDocumento(nombreDelArchivo)

        def agregarColumnas(self,**kwargs)->None:
                self.blocService.agregarColumas(**kwargs)
        
        def obtenerNombreColumnas(self)->list:
                return self.blocService.obtenerNombreColumnas()

        def logicaFecha(self,column:str):
                
                self.blocService.agregarLogicaFecha(column)
                self.blocService.rellenarFechasVacias(column)
        
        def tipo_dato(self,column: str, tipo: str, default)->bool:
                return self.blocService.tipoDeDato(column,tipo,default)
        
        def concatenar(self,column:str,columnaqueseconcatena:str,default =True):
                self.blocService.concatenar(column,columnaqueseconcatena,default)
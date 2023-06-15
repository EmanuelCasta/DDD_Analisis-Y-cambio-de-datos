from blocNotas.domain.services.blocNotesserviceImpl import blocNotesImple
import pandas as pd

class BlocNotasApplication():
        def __init__(self,blocService:blocNotesImple) -> None:
                self.blocService:blocNotesImple  = blocService

        def obtenerDataSet(self)->pd.DataFrame:
                return self.blocService.obtenerTodoElDataset()
        
        def obtenerNombreColumnas(self)->list:
                return self.blocService.obtenerNombreColumnas()
                
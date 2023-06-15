import pandas as pd
class DatoEmpresarial:
    """Representa la tabla empresarial que tiene el bloc de nota.

    Atributos:
        DEPARTAMENTO (str) : Este dato viene por defecto el codigo 05
        MUNICIPIO (str) : [municipio] 
        NUMERO_PREDIAL (str): [codigo_predial]
        TIPO_DE_REGISTRO  (int) : Este valor viene por defecto en 1 
        NUMERO_DE_ORDEN (int) : [NUMERO_DE_ORDEN]
        TOTAL_REGISTROS (int) : [TOTAL_REGISTRO]
        Concatenar en una nueva columna, nombre, y las dos columnas apellidos, 
        Agregar ESTADO_CIVIL colocar N/A en matuYUSCULA, 
        Cambiar el nombre de la columna tipo_doc a TIPO_DOCUMENTO,
        Cambiar el nombre de la columna documento a NUMERO_DOCUMENTO, 
        Dejar quieta la columna DIRECCION, 
        Agregar COMUNA y agregar N/A, 
        Cambiar el nombre de destino a DESTINO_ECONOMICO, 
        Cambiar AREATER por AREA_TERRENO, 
        Cambiar area_const a AREA_CONSTRUIDA, 
        Dejar avaluo quieto, 
        Borrar modoaqusiciom,circulo, y matricula
        Cambiar el nombre fecha registro a VIGENCIA, 
        En todas las fechas debe tener un formato año, mes y dia separado por guiones (-), y en las fechas que tiene 
        espacios en blancos seria 1900-01-01, 
        Agregar la columna NUMERO_PEDRIAL_ANTERIOR y rellenar con N/A, 
        Cambiar npn por NUMERO_PREDIAL_NACIONAL
        Borrar derecho calidad y mejora 
    """
    
    def __init__(self,df:pd.DataFrame,change=False,**kwargs) -> None:
        self.df:pd.DataFrame = df
        """
        Se confirma si se quiere cambiar los nombres de las columnas en tal caso si es true la key en el nombre de la columna y le value el nuevo nombre
        """
        if change:
            dictName= {}
            for key,value  in  kwargs.items():
                if value in list(self.df.columns):
                    self.df.drop([value], axis=1,inplace=True)
                dictName[key] = value
            self.df.rename(columns=dictName,inplace=True)
            
    
## Ejecucion de ejemplo
if __name__ == '__main__':
    df = pd.DataFrame()
    df["PK_PREDIO"] = 0
    kwargs = {'PK_PREDIO':'NUMERO_PREDIAL'}
    dato:DatoEmpresarial = DatoEmpresarial(df,change=True,**kwargs)
    print(dato.df)
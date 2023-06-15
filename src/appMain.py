from blocNotas.domain.services.blocNotesserviceImpl import *

from blocNotas.domain.repo.blocNotesrespository import *
from blocNotas.infraestructura.blocNotesRespositoryImpl import *
from blocNotas.controller.command.mi_aplicacion import *
import os
from colorama import init, Fore, Back, Style,Cursor
import time

## Crea la independencias y la inyecta

class  AppModule:
        def __init__(self,nombreArchivo:str) -> None:
                self.repo:IBlocNotas = BlocNotasImpl(nombreArchivo)
                self.services = blocNotesImple(self.repo )


if __name__ == '__main__':
   
    init()
    print(Style.DIM+Fore.WHITE,"================= Bienvenido ================="  +Style.RESET_ALL)
    print()
    print(Fore.RED,"[ADVERTENCIA]"+Fore.WHITE+" Lee cuidadosamente los pasos a seguir ten presente los pasos que te piden")
    input(Style.BRIGHT+"Presiona enter para continuar"+Style.RESET_ALL)
    os.system('cls')
    archivo:str =""
    time.sleep(1)
    


    while True:

       archivo:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Dilegenciar el nombre del archivo .txt que se le realizara la transformacion de datos: ")
       if not "txt" in archivo.split(".") and not "csv" in archivo.split("."):
              print(Fore.RED+"[ERROR]"+Style.RESET_ALL +" El Archivo no tiene la extension .txt verifica el archivo corresponde al final con directiva txt")
              continue
       try:
             
             file = open(archivo)
             print(Fore.WHITE+"[ESTADO]"+Style.RESET_ALL+" Abriendo el archivo"+Style.RESET_ALL)
             file.close()
             os.system("cls")
       except FileNotFoundError:
             print(Fore.RED+"[ERROR]"+Style.RESET_ALL+" El Archivo con nombre "+Fore.RED+archivo+Style.RESET_ALL+" no fue encontrado por favor ingresa el archivo en el mismo directorio del ejecutable")
             continue



       break
    
    parameterCompareted:str="NPN"

    #Columna que quiere ser llamada para saber cuanta cantidad hay de cierto parametro
    columnsTotal:str = "TOTAL_REGISTRO"

    # Conteo progresivo de ese valor que esta repetido en parameterComparated
    countParamatersComparated:str = "NUMERO_DE_ORDEN"

    nombreArchivoExportacion = "ModificacionDeDatos"



    personalizarColumnasExistentes={'PK_PREDIO':'NUMERO_PREDIAL',
    'MPIO':'MUNICIPIO',
    'TIPO_DOC':'TIPO_DOCUMENTO',
    'DOCUMENTO':'NUMERO_DOCUMENTO',
    'DESTINO':'DESTINO_ECONOMICO',
    'AREACONST':'AREA_CONSTRUIDA',
    'AREATERR':'AREA_TERRENO',
    'FECHAREGISTRO':'VIGENCIA',
    'NPN':'NUMERO_PREDIAL_NACIONAL'}

    personalizarColumnasExistentes2={'PK_PREDIO':'NUMERO_PREDIAL',
    'MPIO':'MUNICIPIO',
    'MATRICULA':'MATRICULA_INMOBILIARIA',
       "AREATERR_TOTAL" :"AREA_TERRENO_1",
    'NPN':'NUMERO_PREDIAL_NACIONAL',
     "AREACONST_TOTAL":"AREA_CONSTRUIDA_1"}

    columnaFecha ="VIGENCIA"



    nuevasColumas = {
           "DEPARTAMENTO" :"05",
           "TIPO_DE_REGISTRO": 1,
           "COMUNA": "N/A",
           "NUMERO_PREDIAL_ANTERIOR":"N/A",
           "ESTADO_CIVIL": "N/A"}
    
    nuevasColumas2 = {
           "DEPARTAMENTO" :"05",
           "TIPO_DE_REGISTRO": 2,
           "ZONA_FISICA_1": "0",
           "ZONA_ECONOMICA_1":"0",
           "ZONA_FISICA_2": "0",
           "ZONA_ECONOMICA_2":"0",
           "AREA_TERRENO_2":"0",
           "HABITACIONES_1":"0",
           "BANOS_1":"0",
              "LOCALES_1":"0",
              "PISOS_1":"0",
              "TIPIFICACION_1":"0",
              "USO_1":"0",
              "PUNTAJE_1":"0",
                     "HABITACIONES_2":"0",
       "BANOS_2":"0",
       "LOCALES_2":"0",
       "PISOS_2":"0",
       "TIPIFICACION_2":"0",
         "USO_2":"0",
       "PUNTAJE_2":"0",
       "AREA_CONSTRUIDA_2":"0",
       "HABITACIONES_3":"0",
       "BANOS_3":"0",
       "LOCALES_3":"0",
       "PISOS_3":"0",
       "TIPIFICACION_3":"0",
       "USO_3":"0",
       "PUNTAJE_3":"0",
       "AREA_CONSTRUIDA_3":"0",
       "NUMERO_PREDIAL_ANTERIOR":"N/A",
       "VIGENCIA":"1999-01-01"


           }
    
    seleccionarColumnasParaExportar =['DEPARTAMENTO',
                'MUNICIPIO',
                'NUMERO_PREDIAL',
                'TIPO_DE_REGISTRO',
                "NUMERO_DE_ORDEN",
                'TOTAL_REGISTRO',
                'NOMBRE',
                'ESTADO_CIVIL',
                'TIPO_DOCUMENTO',
                'NUMERO_DOCUMENTO',
                'DIRECCION',
                'COMUNA',
                'DESTINO_ECONOMICO',
                'AREA_TERRENO',
                'AREA_CONSTRUIDA',
                'AVALUO',
                'VIGENCIA',
                'NUMERO_PREDIAL_ANTERIOR',
                'NUMERO_PREDIAL_NACIONAL',]
    
    seleccionarColumnasParaExportar2 =['DEPARTAMENTO',
                'MUNICIPIO',
                'NUMERO_PREDIAL',
                'TIPO_DE_REGISTRO',
                "NUMERO_DE_ORDEN",
                'TOTAL_REGISTRO',
                "MATRICULA_INMOBILIARIA",
                "ZONA_FISICA_1",
                "ZONA_ECONOMICA_1",
                "AREA_TERRENO_1",
                "ZONA_FISICA_2",
                "ZONA_ECONOMICA_2",
                "AREA_TERRENO_2",
                'HABITACIONES_1',
              "BANOS_1",
              "LOCALES_1",
              "PISOS_1",
              "TIPIFICACION_1",
              "USO_1",
              "PUNTAJE_1",
              "AREA_CONSTRUIDA_1",
              "HABITACIONES_2",
              "BANOS_2",
              "LOCALES_2",
              "PISOS_2",
              "TIPIFICACION_2",
              "USO_2",
              "PUNTAJE_2",
              "AREA_CONSTRUIDA_2",
              "HABITACIONES_3",
              "BANOS_3",
              "LOCALES_3",
              "PISOS_3",
              "TIPIFICACION_3",
              "USO_3",
              "PUNTAJE_3",
              "AREA_CONSTRUIDA_3",
              "VIGENCIA",
              "NUMERO_PREDIAL_ANTERIOR",
              "NUMERO_PREDIAL_NACIONAL",]
    
    module = AppModule(archivo)
    aplicacion = BlocNotasApplication(module.services)
    
    while True:
       os.system("cls")
       info:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Desea hacer los cambios con la configuracion predeterminada del sistema? Responde Si o No: ")
       if info.lower().strip() == "si":
              escoger:str = input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Desea hacer los cambios tipo 1 o 2?: ")
              if escoger == "1":

                     if not aplicacion.tipo_dato(None,None,True):
                            continue

                     if not aplicacion.tipo_dato('AREACONST',"float",default = False):
                            continue

                     if not aplicacion.tipo_dato(column="PK_PREDIO",tipo="str",default=False):
                            continue

                     if not aplicacion.tipo_dato(column="AREATERR",tipo="float",default=False):
                            continue

    

                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Inicializando componentes..."+Style.RESET_ALL)
                     aplicacion.concatenar("NOMBRE","APELLIDOS1")
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Fin concatenado nombres con apellidos"+Style.RESET_ALL)
                     
                     aplicacion.agregarLogicaConteo(parameterCompareted,columnsTotal,countParamatersComparated)
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo conteo del componente"+Style.RESET_ALL)

                     aplicacion.agregarColumnasPersonalizables(**personalizarColumnasExistentes)
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo cambio de nombre de columnas"+Style.RESET_ALL)
                     aplicacion.agregarColumnas(**nuevasColumas)
                     aplicacion.seleccionarColumnas(seleccionarColumnasParaExportar)
                     aplicacion.logicaFecha(columnaFecha)
                     aplicacion.ponerTodasEnMayuscula()
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Fin columnas en mayuscula...  formateando de fechas"+Style.RESET_ALL)
                     
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Fin de la operacion"+Style.RESET_ALL)
                     nombreArchivo :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" Ingresa el nombre del archivo que estara la exportacion :")
                     os.system("cls")
                     print(Fore.YELLOW+Style.BRIGHT+"[ADVERTENCIA] "+Style.RESET_ALL+" Por favor espera a que se finalice la exportacion puede tarda varios segundos, en caso de ver el archivo en el directorio y no hayas recibido la informacion de finalizacion NO ABRIRLO ")
                     aplicacion.exportar(nombreArchivo)
                     input(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo del programa. Presiona ENTER para cerrar el programa"+Style.RESET_ALL)
                     del module
                     exit()
              elif escoger=="2":
                     if not aplicacion.tipo_dato(column="NPN",tipo="str",default=False):
                            input(Fore.RED+"[Error]"+Style.RESET_ALL+"No existe la columna base "+"NPN presiona enter para continuar")
                            continue

                     if not aplicacion.tipo_dato(column="AREATERR_TOTAL",tipo="float",default=False):
                            input(Fore.RED+"[Error]"+Style.RESET_ALL+"No existe la columna base "+"AREATERR_TOTAL presiona enter para continuar")
                            continue

                     if not aplicacion.tipo_dato("AREACONST_TOTAL","float",default = False):
                            input(Fore.RED+"[Error]"+Style.RESET_ALL+"No existe la columna base "+"AREACONST_TOTAL presiona enter para continuar")
                            continue

                     if not aplicacion.tipo_dato(column="PK_PREDIO",tipo="str",default=False):
                            input(Fore.RED+"[Error]"+Style.RESET_ALL+"No existe la columna base "+"PK_PREDIO presiona enter para continuar")
                            continue

                    

                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Inicializando componentes..."+Style.RESET_ALL)
                     
                     
                     aplicacion.agregarLogicaConteo(parameterCompareted,columnsTotal,countParamatersComparated)
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo conteo del componente"+Style.RESET_ALL)

                     aplicacion.agregarColumnasPersonalizables(**personalizarColumnasExistentes2)
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo cambio de nombre de columnas"+Style.RESET_ALL)
                     aplicacion.agregarColumnas(**nuevasColumas2)
                     aplicacion.seleccionarColumnas(seleccionarColumnasParaExportar2)
                     #aplicacion.logicaFecha(columnaFecha)
                     aplicacion.ponerTodasEnMayuscula()
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Fin columnas en mayuscula...  formateando de fechas"+Style.RESET_ALL)
                     
                     print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Fin de la operacion"+Style.RESET_ALL)
                     nombreArchivo :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" Ingresa el nombre del archivo que estara la exportacion :")
                     os.system("cls")
                     print(Fore.YELLOW+Style.BRIGHT+"[ADVERTENCIA] "+Style.RESET_ALL+" Por favor espera a que se finalice la exportacion puede tarda varios segundos, en caso de ver el archivo en el directorio y no hayas recibido la informacion de finalizacion NO ABRIRLO ")
                     aplicacion.exportar(nombreArchivo)
                     input(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo del programa. Presiona ENTER para cerrar el programa"+Style.RESET_ALL)
                     del module
                     exit()
              else:
                      continue
       if "no" == info.lower().strip():
             break
       input("Responde Si o No, tu respuesta no coincide con esas dos monosilabas.. Presiona enter para continuar")



    os.system("cls")
    print(Fore.RED+"[ADVERTECIA] "+Fore.WHITE + "Diligencia el nombre de la columna tal cual como se te muestra en las columnas con Mayusculas o Minusculas de acuerdo al nombre que tenga")
    print(Fore.WHITE+"[INFO] Realizaras las configuracion manual ten presente leer bien la informacion que se le presentara y seguir los pasos adecuados")
    input("Presiona ENTER para continuar")
    os.system("cls")
    print(Fore.RED+"[ADVERTECIA] "+Fore.WHITE + "Diligencia el nombre de la columna tal cual como se te muestra en las columnas con Mayusculas o Minusculas de acuerdo al nombre que tenga")
    result :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"[INFO] Se colocara todos los valores de las columnas de tipo de dato TEXTO si hay algunas columnas que deben ser numericas por favor copiar Si para realizar la modificacion:")
    if result.lower().strip() == "si":
          while True:
                print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                columnDatos: str = input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa la columna que debe ser de tipo numerico :")
                if columnDatos == "" or not columnDatos in aplicacion.obtenerNombreColumnas():
                      input("No existe la columna: "+columnDatos +" presiona ENTER para volver a diligenciar el nombre de la columna ")
                      continue
                
                seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas cambiar otra columna de tipo numerico? copiar? Copia Si o No:")
                while True:
                            if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                  break
                            seguir :str =input(Fore.WHITE+"[INFO] ¿Deseas cambiar otra columna de tipo numerico? copiar? Copia Si o No:")
                aplicacion.tipo_dato(columnDatos,"float",False)
                if seguir.lower().strip() == "si":
                      continue     
                break

    os.system("cls")
    print(Fore.RED+"[ADVERTECIA] "+Fore.WHITE + "Diligencia el nombre de la columna tal cual como se te muestra en las columnas con Mayusculas o Minusculas de acuerdo al nombre que tenga")
    print(Fore.WHITE+"[INFO] Estas son las columnas que tiene el archivo por favor responde las preguntas con la siguiente informacion")
    print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
    columns:list = aplicacion.obtenerNombreColumnas()
    while True:

       parameterCompareted:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"De acuerdo a la informacion anterior cual sera la columna que sera tomada para el conteo :")
       if not parameterCompareted in columns:
              continue

       columnsTotal:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Diligencia el nuevo nombre de la columna que tendra el valor total de conteo de la columna "+parameterCompareted+" :")
       if columnsTotal in  columns:
               print(Fore.RED+"[Error]"+Style.RESET_ALL+"Ya existe este nombre dentro de las columnas por favor realizar el procedimiento del conteo ")
               continue
       countParamatersComparated:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Diligencia el nuevo nombre de la columna el conteo secuencial la columna "+parameterCompareted+" :")
       if countParamatersComparated in  columns:
               print(Fore.RED+"[Error]"+Style.RESET_ALL+"Ya existe este nombre dentro de las columnas por favor realizar el procedimiento del conteo ")
               continue
       break
    os.system("cls")
    print(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Realizando conteo de "+ parameterCompareted+Style.RESET_ALL)


    aplicacion.agregarLogicaConteo(parameterCompareted,columnsTotal,countParamatersComparated)

    os.system("cls")
    print(Fore.RED+"[ADVERTECIA] "+Fore.WHITE + "Diligencia el nombre de la columna tal cual como se te muestra en las columnas con Mayusculas o Minusculas de acuerdo al nombre que tenga")
    seguir:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" ¿Deseas cambiar los nombres de las columnas? Responde Si o No: "+Style.RESET_ALL)
    while True:
              if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                  break
              seguir:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" ¿Deseas cambiar los nombres de las columnas? Responde Si o No: "+Style.RESET_ALL)
    if seguir.lower().strip() == "si":
           while True:
                     print(Fore.WHITE+"[INFO] Estas son las columnas que tiene el archivo por favor responde las preguntas con la siguiente informacion" )
                     print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                     colmunname :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el nombre de la columna que sera cambiado el nombre:")
                     while True:       
                            if colmunname == "" or not colmunname in aplicacion.obtenerNombreColumnas():
                                   input("No existe la columna: "+colmunname +" presiona ENTER para volver a diligenciar el nombre de la columna ")
                                   colmunname :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el nombre de la columna que sera cambiado el nombre:")
                                   continue
                            break
                     colmunnamenew :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el nuevo nombre de la columna:")
                     personalizarColumnasExistentes= {
                            colmunname:colmunnamenew
                     }
                     aplicacion.agregarColumnasPersonalizables(**personalizarColumnasExistentes)
                     seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas cambiar el nombre a otra columna? copiar? Copia Si o No:")
                     while True:
                                   if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                          break
                                   seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas cambiar el nombre a otra columna? copiar? Copia Si o No:")

                     if seguir.lower().strip() == "si":
                            continue     
                     break






    os.system("cls")
    print(Fore.RED+"[ADVERTECIA] "+Fore.WHITE + "Diligencia el nombre de la columna tal cual como se te muestra en las columnas con Mayusculas o Minusculas de acuerdo al nombre que tenga")
    seguir:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" ¿Deseas agregar nuevas columnas? Responde Si o No:"+Style.RESET_ALL)
    while True:
              if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                  break
              seguir:str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+" ¿Deseas agregar nuevas columnas? Responde Si o No:"+Style.RESET_ALL)

    if seguir.lower().strip() == "si":
           while True:
                     print(Fore.WHITE+"[INFO] Estas son las columnas que tiene el archivo por favor responde las preguntas con la siguiente informacion")
                     print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                     colmunname :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa la nueva columna que quieres crear :")
                     while True:       
                            if colmunname == "" or  colmunname in aplicacion.obtenerNombreColumnas():
                                   input("Existe la columna: "+colmunname +" cambia el nombre de la columna ya que existe presiona ENTER para volver a diligenciar el nombre de la columna ")
                                   colmunname :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el nombre de la columna que sera cambiado el nombre:")
                                   continue
                            break
                     colmunnamenew :str =  input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el valor que tendra esa columna:")
                     nuevasColumas= {
                            colmunname:colmunnamenew
                     }
                     aplicacion.agregarColumnas(**nuevasColumas)
                     seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columns? copiar? Copia Si o No:")
                     while True:
                                   if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                          break
                                   seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columns? copiar? Copia Si o No:")
                     if seguir.lower().strip() == "si":
                            continue     
                     break
    # Modificar        
    


    
    os.system("cls")
    while True:
                     print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                     columnsname :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa la columna que quieres formatear la fecha al formato requerido : ")     
                     if not columnsname in  aplicacion.obtenerNombreColumnas():
                             print(Fore.RED+"[ERROR]"+Style.RESET_ALL +" la columna "+columnsname+" no existe por favor revisar en caso de colocar el nombre correctamente los espacios y mayusculas")
                             continue
                     aplicacion.logicaFecha(columnsname)
                     seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columnas? copiar? Copia Si o No:  ")
                     while True:
                                   if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                          break
                                   seguir :str =input(Fore.BLACK+"[INFO] ¿Deseas cambiar otra columna para formatear la fecha? copiar? Copia Si o No:  ")
                     if seguir.lower().strip() == "si":
                            continue     
                     break
    os.system("cls")
    while True:
                     print(Fore.WHITE+"[INFO] Nombre de columnas de archivo" + Fore.BLUE+" >>>>"+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                     columnsname :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa el nombre de la columna principal que se usara para concatenar :")     
                     if  not columnsname in  aplicacion.obtenerNombreColumnas():
                             print(Fore.RED+"[ERROR]"+Style.RESET_ALL +" la columna "+columnsname+"no existe por favor revisar las columnas dadas y cambiar le nombre")
                             continue
                     
                     columnsnamenew :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa la columna que quieres que se concatene :  ")     

                     if  not columnsnamenew in  aplicacion.obtenerNombreColumnas():
                             print(Fore.RED+"[ERROR]"+Style.RESET_ALL +" la columna "+columnsnamenew+"no existe por favor revisar las columnas dadas y cambiar le nombre")
                             continue
                     
                     aplicacion.concatenar(columnsname,columnsnamenew,False)
                     seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columnas para concatenar? copiar? Copia Si o No:  ")
                     while True:
                                   if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                          break
                                   seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columnas para concatenar? copiar? Copia Si o No:  ")
                     if seguir.lower().strip() == "si":
                            continue     
                     break
    os.system("cls")
    #
    seleccionarColumnasParaExportar = []
   
    while True:
                     os.system("cls")
                     print(Fore.WHITE+"[INFO] Nombre de columnas" + Fore.BLUE+" >>>> "+Fore.WHITE+aplicacion.obtenerNombreColumnas())
                     print(Fore.WHITE+"[INFO] Columnas que llevas registradas para la exportacion" + Fore.BLUE+" >>>>"+Fore.WHITE,seleccionarColumnasParaExportar)
                     columnsname :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"Ingresa la columna que quieres exportar :")     
                     if not columnsname in  aplicacion.obtenerNombreColumnas():
                            input(Fore.RED+"[ERROR]"+Style.RESET_ALL +" la columna "+columnsname+" no existe por favor revisar en caso de colocar el nombre correctamente los espacios y mayusculas")
                            continue
                     if columnsname in seleccionarColumnasParaExportar:
                            input(Fore.RED+"[ERROR]"+Style.RESET_ALL +" la columna "+columnsname+" ya existe por favor revisar en caso de colocar el nombre correctamente los espacios y mayusculas")
                            continue
                     seleccionarColumnasParaExportar.append(columnsname)
                     seguir :str =input(Fore.GREEN+Style.BRIGHT+"[INGRESAR_INFORMACION] "+Style.RESET_ALL+"¿Deseas agregar mas columnas? copiar? Copia Si o No:")
                     while True:
                                   if seguir.lower().strip() == "si" or seguir.lower().strip() == "no":
                                          break
                                   seguir :str =input(Fore.BLACK+"[INFO] ¿Deseas agregar mas columnas? copiar? Copia Si o No:  ")
                     if seguir.lower().strip() == "si":
                            continue     
                     break
    aplicacion.seleccionarColumnas(seleccionarColumnasParaExportar)
                     
    
    
    aplicacion.ponerTodasEnMayuscula()
    nombreArchivoExportacion:str  = input("Ingresa el nuevo nombre del archivo :")
    os.system("cls")
    print(Fore.YELLOW+Style.BRIGHT+"[ADVERTENCIA] "+Style.RESET_ALL+" Por favor espera a que se finalice la exportacion puede tarda varios segundos, en caso de ver el archivo en el directorio y no hayas recibido la informacion de finalizacion NO ABRIRLO ")
    aplicacion.exportar(nombreArchivoExportacion)
    input(Style.BRIGHT+Fore.GREEN+"[ESTADO]"+Style.RESET_ALL+" Finalizo del programa. Presiona ENTER para cerrar el programa"+Style.RESET_ALL)
    
    
    exit()
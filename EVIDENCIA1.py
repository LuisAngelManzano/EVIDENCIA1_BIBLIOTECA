import re
import os


condicion = '^[0-9]$' 
registro =[]
inventario =[]
identificador = 0



while True:

   
    print('\t\tMENU PRINCIPAL')
    print(f'{"="*50}')
    print('\t1.REGISTRAR NUEVO EJEMPLAR')
    print('\t2.CONSULTAS Y REPORTES')
    print('\t3.SALIR')
    print(f'{"="*50}')
    opcion = (input('INGRESE NUMERO DE CONSULTA: '))
    os.system('cls')
  
    if opcion=='1':
        while(opcion=='1'):
            identificador = identificador+1
            print(f'{"="*50}')
            print(f'IDENTIFICADOR: {identificador}')
            Titulo = input('TITULO: ').upper()
            Autor =input('AUTOR: ').upper()
            Genero = input('GÉNERO: ').upper()
            Año_publicacion = input('AÑO DE PUBLICACIÓN(dd/mm/aaaa): ')
            Isbn = input('ISBN: ')
            Fecha_adquisicion = input('FECHA DE ADQUISICIÓN(dd/mm/aaaa): ')
        

            registro.append([identificador,Titulo,Autor,Genero,Año_publicacion,Isbn,Fecha_adquisicion])
            
            inventario.append({'Titulo': Titulo,
                'Autor' : Autor,
                'Genero': Genero,
                'Año_publicacion':Año_publicacion,
                'Isbn' : Isbn,
                'Fecha_adquisicion': Fecha_adquisicion})
            break
        os.system('cls')


            
    elif opcion=='2':
        while True:
            print('\t\tCONSULTAS Y REPORTES')
            print(f'{"="*50}')
            print("1.CONSULTA DEL TITULO\n2.REPORTES\n3.VOLVER AL MENU PRINCIPAL.")
            #opcion2= int(input()) anterior por si se opta por numerico
            reportes= (input())
            os.system('cls')
            print(f'{"="*50}') 
            if reportes =='1':#CONSULTA DE TITULO
                while True:
                    print("1.POR TITULO\n2.POR ISBN\n3.VOLVER AL MENÚ DE CONSULTAS Y REPORTES")
                    print(f'{"="*50}')
                    consulta_titulo = input()
                    if consulta_titulo =='1':
                        print('\tCONSULTA POR TITULO')
                        print(f'{"="*50}')
                        print('\t\tTITULO')
                        print(f'{"="*50}') 
                        titulo = [nombre[1]for nombre in registro]
                        print(f'LOS AUTORES EN LA BASE REGISTRADA SON: {titulo}')
                        print(f'{"="*50}')
                        buscar = input('INGRESE LA CONSULTA DEL TITULO: ').upper()
                        print(f'{"="*50}')
                        for p in inventario:
                            if buscar == p['Titulo']:
                                print(f'{"="*50}') 
                                print('\t Titulo:',p['Titulo'])
                                print('\t Autor:',p['Autor'])
                                print('\t Genero:',p['Genero'])
                                print('\t Año Publicado:',p['Año_publicacion'])
                                print('\t Isbn:',p['Isbn'])
                                print('\t Fecha Adquirida:',p['Fecha_adquisicion'])
                                print(f'{"="*50}')
                                                
                        
                    elif consulta_titulo == '2':
                        print('\tCONSULTA POR ISBN')
                        isbn = [dato2[5] for dato2 in registro]
                        print(f'{"="*50}') 
                        print(f'Los ISBN EN LA BASE REGISTRADA SON: {isbn}')
                        buscar = input('INGRESE EL ISBN: ').upper()
                        for p in inventario:
                            if buscar == p['Isbn']:
                                print(f'{"="*50}') 
                                print('\t Titulo:',p['Titulo'])
                                print('\t Autor:',p['Autor'])
                                print('\t Genero:',p['Genero'])
                                print('\t Año Publicado:',p['Año_publicacion'])
                                print('\t Isbn:',p['Isbn'])
                                print('\t Fecha Adquirida:',p['Fecha_adquisicion'])
                                print(f'{"="*50}')
                    elif consulta_titulo=='3':
                        print('REGRESANDO.....')
                        break
            
        
            elif reportes=='2':#REPORTES
                while True:
                    print('1.CATALOGO COMPLETO\n2.REPORTE POR AUTOR\n3.REPORTE POR GENERO\n4.POR AÑO DE PUBLICACION\n5.VOLVER AL MENU DE REPORTES')
                    print(f'{"="*50}')     

                    dato = input()
                    os.system('cls')
                    if dato =='1': #CATALOGO COMPLETO
                        print("ID\tTITULO\t\t\t\tAUTOR\t\t\t\tGENERO\t\t\tAÑO PUBLICADO\tISBN\tFECHA ADQUIRIDA")
                        print(f'{"="*50}') 
                        for identificador,Titulo,Autor,Genero,Año_publicacion,Isbn,Fecha_adquisicion in registro:
                            print(f'{identificador:<3}{Titulo:<39}{Autor:<30}{Genero:<25}{Año_publicacion:<15}{Isbn:<12}{Fecha_adquisicion}')
                        print(f'{"="*50}')     

                    elif dato== '2':#REPORTE POR AUTOR
                        print(f'{"="*50}') 
                        autor = [nombre[2]for nombre in registro]
                        print('\t\tAUTOR')
                        print(f'{"="*50}')
                        print(f'LOS AUTORES EN LA BASE REGISTRADA SON: {autor}')
                        buscar = input('INGRESE EL AUTOR: ').upper()
                        for p in inventario:
                            if buscar == p['Autor']:
                                print(f'{"="*50}') 
                                print('\t Titulo:',p['Titulo'])
                                print('\t Autor:',p['Autor'])
                                print('\t Genero:',p['Genero'])
                                print('\t Año Publicado:',p['Año_publicacion'])
                                print('\t Isbn:',p['Isbn'])
                                print('\t Fecha Adquirida:',p['Fecha_adquisicion'])
                                print(f'{"="*50}')
                           

                    elif dato=='3': #REPORTE POR GENERO
                        print(f'{"="*50}')
                        genero =[g[3] for g in registro]
                        print('\t\tGENERO')
                        print(f'{"="*50}')
                        print(f'LOS GENEROS DISPONIBLES SON: {genero}')
                        buscar = input('INGRESE EL GENERO : ').upper()
                        for p in inventario:
                            if buscar == p['Genero']:
                                print(f'{"="*50}') 
                                print('\t Titulo:',p['Titulo'])
                                print('\t Autor:',p['Autor'])
                                print('\t Genero:',p['Genero'])
                                print('\t Año Publicado:',p['Año_publicacion'])
                                print('\t Isbn:',p['Isbn'])
                                print('\t Fecha Adquirida:',p['Fecha_adquisicion'])
                                print(f'{"="*50}')
                        print(f'{"="*50}')
                    
                    elif dato=='4': #POR AÑO DE PUBLICACION
                        print(f'{"="*50}')
                        año_publicado = [publicacion[4] for publicacion in registro]
                        print('\t\tAÑO PUBLICADO')
                        print(f'{"="*50}')
                        print(f'LOS AÑOS PUBLICADOS EN EL REGISTRO SON: {año_publicado}')
                        buscar = input('INGRESE EL AÑO PUBLICADO A BUSCAR : ').upper()
                        for p in inventario:
                            if buscar == p['Año_publicacion']:
                                print(f'{"="*50}') 
                                print('\t Titulo:',p['Titulo'])
                                print('\t Autor:',p['Autor'])
                                print('\t Genero:',p['Genero'])
                                print('\t Año Publicado:',p['Año_publicacion'])
                                print('\t Isbn:',p['Isbn'])
                                print('\t Fecha Adquirida:',p['Fecha_adquisicion'])
                                print(f'{"="*50}')
                        print(f'{"="*50}')
                    elif dato=='5': #VOLVER AL MENU
                        print('Volviendo')
                        break
                    elif dato == '':
                        print('NO SELECCIONO NINGUNA CONSULTA')
                        print(f'{"="*50}')
                        continue
                    elif  not bool (re.match(condicion,dato)):
                        print('NO CUMPLE CON EL FORMATO DEBE SER NUMERICO ')
                        continue
                    else:
                        print('Numero en lista no detectado')
                        continue

                        
            elif reportes=='3': #VOLVER MENU CONSULTAS Y REPORS
                print('REGRESANDO...')
                break
            elif  not bool (re.match(condicion,reportes)):
                print('NO CUMPLE CON EL FORMATO ')
                continue
            else:
                print('Formato Invalido Numero no encontado en la lista Rango(1-3)')
                


       
    elif opcion =='3':
        print('TERMINACION DEL PROGRAMA')
        break
    elif opcion=='':
        print('NO SE PERMITE ESPACIOS VACIOS.')
        continue
    elif  not bool (re.match(condicion,opcion)):
        print('NO CUMPLE CON EL FORMATO DEBE SER NUMERICO ')
        continue
    else:
        print('Formato Invalido Numero no encontado en la lista Rango(1-3)')

    

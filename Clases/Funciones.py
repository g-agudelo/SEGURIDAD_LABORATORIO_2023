def base_dato():
    #IMPORTAMOS LA LIBRERIA QUE VAMOS A USAR
    import os
    from os import replace
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service 
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.common.by import By
    from pathlib import Path
    #INSTALAMOS LOS DRIVER PARA HACER WEB-SCRAPPING
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install()))
    #ACCEDEMOS AL UNVIRTUAL Y DESCARGAMOS LA BASE DEDATOS
    driver.get('https://unvirtual.medellin.unal.edu.co/mod/simplecertificate/view.php?id=141387&tab=1&page=0&perpage=200&orderby=username')
    usuario=driver.find_element("name","username")
    password=driver.find_element("name","password")
    usuario.send_keys('gagudelo')
    password.send_keys('Pinkfighter343')
    boton=driver.find_elements(By.XPATH,'//*[@id="loginbtn"]')
    boton[0].click()
    boton=driver.find_elements(By.XPATH,'//*[@id="bulkissue"]/div/table/tbody/tr/td[4]/div')
    boton[0].click()
    driver.close()
    #ACTUALIZAMOS LA BASE DE DATOS
    path = str(os.path.join(Path.home(), "Downloads"))
    replace(path+'\\Seguridad en laboratorios-Certificado - Laboratorio de vibro-acústica.xlsx',os.getcwd()+'\\usuarios.xlsx')

    
def buscarbd():
    #IMPORTAMOS LA LIBRERIAS QUE VAMOS A USAR
    import cv2
    import pandas as pd
    import os
    #ACCEDEMOS A LA CAMARA Y DETECTAMOS EL CODIGO QR
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data,bbox, _ = detector.detectAndDecode(img)
        if data:
            a=data
            break
        cv2.imshow("LECTOR DE CODIGO QR", img)    
        if cv2.waitKey(1) == ord("q"):
            break
    #VERIFICAMOS EL CODIGO QR DEL ESTUDIANTE
    ruta_excel = os.getcwd()+'\\usuarios.xlsx'
    excel = pd.read_excel(ruta_excel)
    codigos=excel['Código']
    codigo=str(a[-36:])
    datos_estudiante=(excel.loc[excel['Código']==codigo].values.tolist())
    codigos=codigos.to_list()
    if codigos.count(codigo)>0 and codigos.count(codigo)<2:
        nombre_estudiante=str(datos_estudiante[0][0])
        cedula_estudiante=str(datos_estudiante[0][1])
        fecha=str(datos_estudiante[0][3])
        resultado='El estudiante '+nombre_estudiante+' se encuentra inscrito en la base de datos, su cedula es: '+cedula_estudiante+' y aprobo el curso el '+ fecha
    elif codigos.count(codigo)==0:
        resultado='El estudiante no se encuentra inscrito en la base de datos'
    elif codigos.count(codigo)>0 and codigos.count(codigo)>=2:
        nombre_estudiante=str(datos_estudiante[0][0])
        resultado='El estudiante '+nombre_estudiante+' se encuentra inscrito en la base de datos, pero esta duplicado sus datos'
    return resultado

    
        
    
#MANEJO DE ARCHIVOS

#PARA ELLO SE NECESITA UN ARCHIVO DE ENTRADA
archivos = open('archivos/entrada.txt','r+')

#VAMOS A LEER EL ARCHIVO
linea = archivos.readline()                 #Lee una sola linea
print(linea)    

while linea != '':                          #Iteracion para leer todas las lineas
    linea = archivos.readline()
    print(linea)
#CERRAMOS EL ARCHIVO
archivos.close()
#!encoding: UTF-8
import Modulo
PI=3.1415926535897931159979634685441852
def error(nro_intervalos,nro_test,umbral):
  contador=0
  for i in range(nro_test):
    apri=Modulo.aproxpi(nro_intervalos)
    error=abs(apri-PI)
    if error>umbral:
      contador=contador+1
  fallo=(contador/nro_test)*100
  return fallo

import sys
if(len(sys.argv)==4):
  nro_intervalos=int(sys.argv[1])
  nro_test=int(sys.argv[2])
  umbral=float(sys.argv[3])
else:
  print"Debía introducir dos valores. Ahora se realizarán las operaciones con los valores que han sido establecidos por defecto."
  nro_intervalos=4
  nro_test=4
  umbral=0.0001
Error=error(nro_intervalos,nro_test,umbral)
print"El porcentate de error cometido es de: %4.2f" %Error 
  
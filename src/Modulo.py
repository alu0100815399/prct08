#! encoding: UTF-8
def aproxpi (fin):

  if fin>0:
    
    suma=0.0
    pi=3.1415926535897931159979634685441852
    for i in range(fin+1):
  
      a= float (i-1.0)/fin
      b= float (i)/fin
      x_i= (i-0.5)/fin
      fx_i= ((4.0)/(1.0+x_i**2))
      
      suma+= fx_i

    aprox= suma/fin					
    
  return aprox

if __name__=='__main__':
  import sys
  if(len(sys.argv)==3):
    n=int(sys.argv[1])
    veces=int(sys.argv[2])
  else:
    print "Debe introducir dos valores: n(número de intervalos) y veces(número de veces que se ejecuta). Por defecto, se harán 4 intervalos,ejecutándose 4 veces. "
    n=4
    veces=4
  l=[]
  for i in range (veces+1):
    n*=i
    s=aproxpi (n)
    print "La aproximación del número pi es: %11.10f" %s
    l=l+[s]
  print l

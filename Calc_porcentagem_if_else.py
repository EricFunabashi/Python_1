n1 = float(input( "Qual valor a ser calculado?" ))
n2 = float(input( "Quantos por %?" )) / 100
s = n1 * n2
if s < 50 :   
      print ('Resultado:', s)
      print('Valor menor que a metade')
else:
      print('Valor maior que a metade')

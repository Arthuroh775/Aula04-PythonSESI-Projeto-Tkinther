note = float(input('Qual foi sua nota nesse bimestre? '))

if note >= 8 and note <= 10: 
    print("Você tirou um Notão parabéns! ")
elif note < 8 and note >= 6 : 
    print ('Na média ')
elif note < 6:
    print('Que bosta, tá de recuperação...☠️')
else:
    print("Nota inserida de forma inválida")
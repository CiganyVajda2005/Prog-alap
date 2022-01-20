szo1 = input('Adj meg egy szót: ')
szo2 = input('Adj meg agy második szót:  ')
szo1_hossza = len (szo1)
szo2_hossza = len(szo2)
if (szo1_hossza > szo2_hossza):
    print ('az 1 a hoszab szó' + szo1)
elif szo2_hossza==szo1_hossza:
    print('egyenlő a két szám ')
else:
    print ('a második a nagyobb ')


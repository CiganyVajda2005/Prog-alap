n = int(input("hány kocsi?"))
for i in range (n):
    marka =input ("milyen márka?")
    szin =input ("milyen szin?")
    ev =input ("milyen év?")
    lista += f"{marka}, {szin}, {ev}; \n"
print (lista)
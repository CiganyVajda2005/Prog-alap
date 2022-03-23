n = input ("hányan ember van?")
n = int(n)
nevek = "név gyűjt: "
for x in range (n):
    nevek += f" Az {x+1}.nev: "
    nevek +=  input(f"{x+1}.név:")
print (nevek)
with open ("file.txt","w" ,encoding="utf-8") as file:
    file.write (nevek)
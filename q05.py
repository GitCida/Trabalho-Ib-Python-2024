hora = int(input("Digite o a hora que você deseja saber se é dia, tarde ou noite(de 0 a 23): "))
if (hora >= 0 and hora < 12):
    print("é manhã.")
elif (hora >= 12 and hora < 18):
    print ("é tarde.")
else:
    print("é noite.")
#0 a 11: manhã / 12 as 17: tarde / 18 as 23: noite
nome = input("Diga seu nome: ")
idade = int(input("Agora informe sua idade: "))
if(idade<=15):
    print(f'{nome}, você ainda não pode receber o título de eleitor.')
else: 
    print(f'{nome}, você já pode receber o título de eleitor')
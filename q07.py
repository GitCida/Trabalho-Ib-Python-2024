nome = input("Digite seu nome: ")
disc = input("Digite o nome da matéria que deseja saber a média: ")
n1 = int(input("Diga sua primeira nota: "))
n2 = int(input("Diga sua segunda nota: "))
m = (n1+n2)/2
#de 0 a 5: reprovado / de 6 a 10: aprovado 
if (m > 0 and m < 6 ):
    print(f'{nome} está reprovado(a) na disciplina de {disc}.')
else:
    print(f'{nome} está aprovado(a) na disciplina de {disc}.')
#Não precisaria dizer a nota?
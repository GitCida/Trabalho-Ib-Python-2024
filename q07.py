nome = input("Digite seu nome: ")
disciplina = input("Digite o nome da matéria que deseja saber a média: ")
n1 = float(input("Diga sua primeira nota: "))
n2 = float(input("Diga sua segunda nota: "))
m = (n1+n2)/2
if m <6:
    situação = 'reprovado(a)'
else:
    situação = 'aprovado(a)'
print(f'{nome} está {situação} na disciplina {disciplina}.')
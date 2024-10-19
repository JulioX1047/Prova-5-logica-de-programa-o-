qtalunos=int(input("Informe a qauntidade alunos"))
somag=0

for  n in range(qtalunos):
    nome=input("Digite o nome do aluno ")
    nota1=float(input("Digite a primeira nota "))
    nota2=float(input("Digite a segunda nota"))
    nota3=float(input("Digite a terceira nota "))
    media=(nota1+nota2+nota3)/3
    somag+=media
    if media>=7:
        status="Aprovado"
    else :
       status="Reprovado" 
    print(f"\nNome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f} - Status: {status}")   

mediageral = somag / qtalunos
print(f"\nA média geral da turma é: {mediageral:.2f}")

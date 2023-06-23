notas = {}

while True:
    a = str(input('Digite uma avaliação: '))
    notas[a] = float(input('Digite a nota: '))
    res = str(input('Deseja continuar S/N: ')).upper()
    if res == 'N':
        break
print(notas)

nota = notas.values()
nota = list(notas)

med = sum(nota)
med = med / len(nota)
print(med)
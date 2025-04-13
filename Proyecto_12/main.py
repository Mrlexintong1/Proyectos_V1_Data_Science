votos = {'Diseño 1': 1334, 'Diseño 2': 982, 'Diseño 3': 1751, 
         'Diseño 4': 210, 'Diseño 5': 1811}

total_votos = sum(votos.values())
ganador = max(votos, key=votos.get)

print(f"Diseño ganador: {ganador}")
print(f"Porcentaje de votos del ganador: {100 * votos[ganador] / total_votos:.2f}%")
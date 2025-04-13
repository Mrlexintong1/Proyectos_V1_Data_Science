respuestas_correctas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
puntaje = 0

for i, correcta in enumerate(respuestas_correctas):
    respuesta = input(f"Respuesta del estudiante para la pregunta {i+1}: ").upper()
    if respuesta == correcta:
        puntaje += 1

print(f"Puntuación final del estudiante: {puntaje}/10")
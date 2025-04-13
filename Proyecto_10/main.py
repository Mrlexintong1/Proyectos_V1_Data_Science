meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
temperaturas = [float(input(f"Temperatura media de {mes}: ")) for mes in meses]

promedio_anual = sum(temperaturas) / len(temperaturas)
print(f"Promedio anual: {promedio_anual:.2f}°C")

for i, temp in enumerate(temperaturas):
    if temp > promedio_anual:
        print(f"{meses[i]}: {temp}°C")
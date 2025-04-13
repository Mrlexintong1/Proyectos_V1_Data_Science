bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
porcentajes = []

for i in range(1, len(bacterias)):
    crecimiento = 100 * (bacterias[i] - bacterias[i-1]) / bacterias[i-1]
    porcentajes.append(round(crecimiento, 2))

print("Porcentajes de crecimiento por día:", porcentajes)
datos = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

promedios = {area: sum(valores)/2 for area, valores in datos.items()}
area_mas_diversa = max(promedios, key=promedios.get)

for area, promedio in promedios.items():
    print(f"{area}: Promedio de especies = {promedio:.2f}")

print(f"Área con mayor diversidad: {area_mas_diversa}")
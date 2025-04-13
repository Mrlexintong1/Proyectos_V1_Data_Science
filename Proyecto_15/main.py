sectores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

media_por_sector = {s: sum(edades)/len(edades) for s, edades in sectores.items()}
todas_las_edades = [edad for lista in sectores.values() for edad in lista]
media_general = sum(todas_las_edades) / len(todas_las_edades)
mayores_a_media = sum(1 for edad in todas_las_edades if edad > media_general)

for sector, media in media_por_sector.items():
    print(f"{sector}: media de edad = {media:.2f}")

print(f"Media general: {media_general:.2f}")
print(f"Personas por encima de la media: {mayores_a_media}")
ids = [int(input(f"Ingrese el ID del producto {i+1}: ")) for i in range(10)]
dulces = [id for id in ids if id % 2 == 0]
amargos = [id for id in ids if id % 2 != 0]

print(f"Cantidad de productos dulces: {len(dulces)}")
print(f"Cantidad de productos amargos: {len(amargos)}")
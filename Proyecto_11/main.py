ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 
          'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

total_ventas = sum(ventas.values())
producto_mas_vendido = max(ventas, key=ventas.get)

print(f"Total de ventas: {total_ventas}")
print(f"Producto más vendido: {producto_mas_vendido} ({ventas[producto_mas_vendido]} unidades)")
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonificaciones = {}
total_gasto = 0
bonificacion_minima = 0
bonificacion_maxima = 0

for salario in salarios:
    bonificacion = max(0.10 * salario, 200)
    bonificaciones[salario] = bonificacion
    total_gasto += bonificacion
    if bonificacion == 200:
        bonificacion_minima += 1
    if bonificacion > bonificacion_maxima:
        bonificacion_maxima = bonificacion

print(f"Gasto total en bonificaciones: ${total_gasto:.2f}")
print(f"Empleados con bonificación mínima: {bonificacion_minima}")
print(f"Bonificación más alta: ${bonificacion_maxima:.2f}")
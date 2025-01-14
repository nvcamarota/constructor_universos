"""
CONSTRUCTOR DE UNIVERSOS
Contexto: Son creadoras de universos y deben diseñas galaxias, estrellas y planetas. Cada universo tiene características únicas que deben ser configuradas usando *args y **kwargs. Además, una función anidada calcula el total de cuerpos celestes creados.
Actividad:
Diseña una función crear_universo(*galaxias, **configuracion) que:
• Use *args para recibir nombres de galaxias.
• Use **kwargs para configurar detalles como el número de estrellas y planetas por galaxia.
• Incluya una función anidada calcular_cuerpos() que calcule el total de cuerpos celestes creados en el universo.
"""

def crear_universo(*galaxias, **configuracion):
    def calcular_cuerpos():
        total_estrellas = configuracion.get('estrellas', 0)
        total_planetas = configuracion.get('planetas', 0)
        return total_estrellas + total_planetas
    
    print('Galaxias creadas:')
    for galaxia in galaxias:
        print(f'- {galaxia}')
        
    total_cuerpos = calcular_cuerpos()
    print(f'Total de cuerpos celestes (estrellas + planetas): {total_cuerpos}')
    
crear_universo(
    "Vía Láctea", "Andrómeda",
    estrellas = 100000,
    planetas = 500000
)
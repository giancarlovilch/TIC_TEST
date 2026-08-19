def calcular_descuento(precio, porcentaje):
    if precio < 0 or porcentaje < 0:
        raise ValueError("Los valores no pueden ser negativos")
    descuento = precio * (porcentaje / 100)
    return round(precio - descuento, 2)

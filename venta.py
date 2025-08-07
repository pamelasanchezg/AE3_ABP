def calcular_descuento(cantidad_productos, compras_previas, monto_total, es_dia_promocion):
    descuento = 0

    print("\n🔎 Evaluando condiciones de descuento:\n")
    # Condiciones descuentos
    if cantidad_productos > 10:
        descuento += 10
        print("Productos comprados: Aplica 10% de descuento.")
    else:
        print("Productos comprados: No aplica descuento).")

    if compras_previas > 3:
        descuento += 5
        print("Cliente frecuente: Aplica 5% de descuento.")
    else:
        print("Cliente frecuente: No aplica descuento.")
        
    if monto_total > 500:
        descuento += 7
        print("Descuento por monto: Aplica 7% de descuento.")
    else:
        print("Descuento por monto: No aplica descuento por monto.")

    if es_dia_promocion:
        descuento += 15
        print("Dia promoción: Aplica 15% de descuento.")
    else:
        print("Dia promoción: No aplica descuento.")

    # Limitar descuento máximo
    if descuento > 30:
        descuento = 30

    return descuento
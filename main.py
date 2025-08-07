from venta import calcular_descuento
def main():
    print("=== Cálculo de Descuento ===")

    # Entradas del usuario
    cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
    compras_previas = int(input("Ingrese la cantidad de compras previas del cliente: "))
    monto_total = float(input("Ingrese el monto total de la compra ($): "))
    
    respuesta_promocion = input("¿Es un día de promoción especial? (s/n): ").lower()
    es_dia_promocion = respuesta_promocion == "s"

    # Cálculo del descuento
    descuento = calcular_descuento(cantidad_productos, compras_previas, monto_total, es_dia_promocion)

    # Mostrar resultado
    print(f"\nDescuento aplicado: {descuento}%")
    monto_descuento = monto_total * (descuento / 100)
    total_final = monto_total - monto_descuento

    print(f"Monto de descuento: ${monto_descuento:.2f}")
    print(f"Total a pagar con descuento: ${total_final:.2f}")

    print("\nGracias por tu compra, vuelva pronto.")    

if __name__ == "__main__":
    main()
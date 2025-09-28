saldo_inicial = float(input("Introduce el saldo inicial de la cuenta: "))
ahorro_mensual = float(input("Introduce la cantidad que ahorras cada mes: "))
numero_meses = int(input("Introduce el número de meses que deseas calcular: "))

saldo_final = saldo_inicial + (ahorro_mensual * numero_meses)

if saldo_final > 5000:
    print(f"¡Felicidades! Has superado tu objetivo ahorrando: {saldo_final} euros.")

else:
    print(f"Tu saldo final es de: {saldo_final} euros.")
pesos_cop = int(input("Pesos colombianos: "))

tasa_usd = 4000
tasa_eur = 4600

dolares = pesos_cop / tasa_usd
euros = pesos_cop / tasa_eur

print("\nSalida esperada")
print(f"Pesos colombianos: ${pesos_cop}")
print(f"Dólares: ${dolares:.2f} USD")
print(f"Euros: €{euros:.2f} EUR")

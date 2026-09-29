segundos_totales = int(input("Segundos: "))

horas = segundos_totales // 3600               
segundos_restantes = segundos_totales % 3600    

minutos = segundos_restantes // 60             
segundos_finales = segundos_restantes % 60     

print(f"\n{segundos_totales} segundos equivalen a:")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos_finales} segundo(s)")
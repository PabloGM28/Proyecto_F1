import math
# Vueltas y tiempos de neumaticos:
# vueltas al circuito
# vida esperada del neumatico
# degradacion (usar la funcion de degradacion)
# Velocidad inicial (que diferencia de velocidad hay respecto al duro?? Tiene que ser adimensionalizado respecto a este)


def laptime(laps,life,degradation,speed_0):
    total_time = 0.0
    time_per_lap = []

    # Calcular el tiempo por vuelta y la degradación
    for lap in range(1, laps + 1):
        # Calcular la degradación actual
        deg_now = degradation*lap   
        # Calcular la velocidad actual del neumático
        if lap >= life:
            # La velocidad cae exponencialmente después de la vuelta crítica
            exp_decrease = math.exp(-(abs(1-degradation))*(lap - life))
            #print(exp_decrease)
            speed_now = speed_0*exp_decrease
        else:
            speed_now = speed_0 
        # Calcular el tiempo por vuelta basado en la degradación
        laptime = 10/speed_now + deg_now/100
        # Agregar el tiempo por vuelta al tiempo total
        total_time += laptime

        time_per_lap.append(laptime)
        
    return time_per_lap



# Para probar la funcion:


# #total_time, time_per_lap = laptime(57,15,1.3,2)
time_per_lap = laptime(57,7,1.83,1)
# #print(f"Tiempo total del neumático: {total_time:.2f}")
#print("Tiempos por vuelta:", time_per_lap)


        



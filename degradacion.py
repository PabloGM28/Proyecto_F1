
# FACTOR DEGRADACION

# Parámetros que toma:
#   Temperaturas de pista y aire
#   Curvas de alta, media y baja velocidad
#   carga aerodinamica

#parametros = {"track_temp", "air_temp", "high_speed_turns", "medium_speed_turns", "low_speed_turns", "wing_load", "length", "abrassion"}

<<<<<<< Updated upstream
def degradation(tire_type, track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion):
    # Define degradation factor for each tire type based on input parameters
    degradation_factor = 1.0

=======
def degradation(track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion):
    # Define degradation factor for each tire type based on input parameters
    
>>>>>>> Stashed changes
    ######### Degradacion por compuesto #########
    # Duro, medio, blando
    degradation_factor = [1.5, 1.3, 1.15]

    ######### Degradacion por carga aerodinámica #########   
    if wing_load == 'low': 
        deg_aero = 1.1    
    elif wing_load == 'medium': 
        deg_aero = 1.3
    elif wing_load == 'high': 
        deg_aero = 1.5

    ######### Degradacion por curvas #########
    turn_factor = 1.0 + 0.2*high_speed_turns + 0.1*medium_speed_turns + 0.05*low_speed_turns

    ######### Degradacion por abrasion #########
    abrassion_factor = (1+abrassion)

    ########################### Degradacion por temperaturas de pista y de aire + graining ###########################
    #
    ######### Degradacion por temperatura de pista #########  
    if track_temp < 20:
        deg_track = 1.0
    elif 20<= track_temp < 35:
        deg_track = 1.05
    elif 35<= track_temp < 45:
        deg_track = 1.15

    ######### Degradacion por temperatura del aire #########
    if air_temp < 25:
        deg_air = 0.98
    elif 25<= air_temp < 35:
        deg_air = 1.0

    elif 35<= track_temp < 45: 
        deg_air = 1.02
    else:
        deg_air =1.05

    ######### Degradacion por graining #########
    if abs(abs(air_temp)-abs(track_temp)) >=25:
        graining = 1.1
    else:
        graining = 1.0

    ######### Degradacion por longitud de pista #########
    for i in [0,1,2]:
        degradation_factor[i] = degradation_factor[i]*deg_aero*turn_factor*abrassion_factor*deg_track*deg_air*graining*length
    
    ######### Degradacion adimensional #########
    for i in [0,1,2]:
        degradation_factor[i] = degradation_factor[i]/degradation_factor[2]
    return degradation_factor

print(degradation(35,27,4,3,2,'high',5,0.2)) # que no falten los prints de prueba

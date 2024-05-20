
# FACTOR DEGRADACION

# Parámetros que toma:
#   Temperaturas de pista y aire
#   Curvas de alta, media y baja velocidad
#   carga aerodinamica

#parametros = {"track_temp", "air_temp", "high_speed_turns", "medium_speed_turns", "low_speed_turns", "wing_load", "length", "abrassion"}

def degradation(track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion,condition):
    # Define degradation factor for each tire type based on input parameters
    degradation_factor = 1.0

    ######### Degradacion por compuesto #########
    # Duro, medio, blando
    degradation_factor = [1.083, 1.043, 1.02]

    ######### Degradacion por carga aerodinámica #########   
    if wing_load == 'low': 
        deg_aero = 1.001    
    elif wing_load == 'medium': 
        deg_aero = 1.002
    elif wing_load == 'high': 
        deg_aero = 1.003

    ######### Degradacion por curvas #########
    turn_factor = 1.0 + 0.001*high_speed_turns + 0.0005*medium_speed_turns + 0.00025*low_speed_turns

    ######### Degradacion por abrasion #########
    abrassion_factor = (1+abrassion)

    ########################### Degradacion por temperaturas de pista y de aire + graining ###########################
    #
    ######### Degradacion por temperatura de pista #########  
    if track_temp < 20:
        deg_track = 1.0
    elif 20<= track_temp < 35:
        deg_track = 1.005
    elif 35<= track_temp < 45:
        deg_track = 1.015
    elif track_temp >=45:
        deg_track = 1.2

    ######### Degradacion por temperatura del aire #########
    if air_temp < 25:
        deg_air = 0.098
    elif 25<= air_temp < 35:
        deg_air = 1.0

    elif 35<= track_temp < 45: 
        deg_air = 1.02
    else:
        deg_air =1.05

    ######### Degradacion por graining #########
    if abs(abs(air_temp)-abs(track_temp)) >=25:
        graining = 1.01
    else:
        graining = 1.0

    if condition == "CLOUDY":
        lower_deg = 0.9
    else:
        lower_deg = 1
        
    ######### Degradacion por longitud de pista #########
    for i in [0,1,2]:
        degradation_factor[i] = degradation_factor[i]*deg_aero*turn_factor*abrassion_factor*deg_track*deg_air*graining*(length/2)*lower_deg
    


    ######### DEGRADACION ADIMENSIONAL #########
    # for i in [0,1,2]:
    #     degradation_factor[i] = degradation_factor[i]/degradation_factor[2]
    degradation_factor = {"soft":degradation_factor[0],"medium":degradation_factor[1],"hard":degradation_factor[2]}
    return degradation_factor

#print(degradation(35,27,4,3,2,'high',5/2,0.2,"sunny")) # que no falten los prints de prueba


# FACTOR DEGRADACION

# Parámetros que toma:
#   Tipo de neumáticos
#   Temperaturas de pista y aire
#   Curvas de alta, media y baja velocidad
#   carga aerodinamica


def degradation(tire_type, track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion ):
    # Define degradation factor for each tire type based on input parameters
    degradation_factor = 1.0
    
    ######### Degradacion por compuesto #########
    if tire_type == 'soft':
        degradation_factor = degradation_factor + 0.5
    elif tire_type == 'medium':
        degradation_factor = degradation_factor + 0.3
    elif tire_type == 'hard':
        degradation_factor = degradation_factor + 0.15

    ######### Degradacion por carga aerodinámica #########   
    if wing_load == 'low': 
        deg_aero = 1.1    
    elif wing_load == 'medium': 
        deg_aero = 1.3
    elif wing_load == 'high': 
        deg_aero = 1.5
    degradation_factor = degradation_factor*deg_aero

    ######### Degradacion por curvas #########
    degradation_factor = degradation_factor*(1.0 + 0.2*high_speed_turns + 0.1*medium_speed_turns + 0.05*low_speed_turns)

    ######### Degradacion por abrasion #########
    degradation_factor = degradation_factor*(1+abrassion)

    ########################### Degradacion por temperaturas de pista y de aire + graining ###########################
    #
    ######### Degradacion por temperatura de pista #########  
    if track_temp < 20:
        deg_track = 1.0
    elif 20<= track_temp < 35:
        deg_track = 1.05
    elif 35<= track_temp < 45:
        deg_track = 1.15
    degradation_factor = degradation_factor*deg_track

    ######### Degradacion por temperatura del aire #########

    if air_temp < 25:
        deg_air = 0.98
    elif 25<= air_temp < 35:
        deg_air = 1.0

    elif 35<= track_temp < 45: 
        deg_air = 1.02
    else:
        deg_air =1.05
    
    degradation_factor = degradation_factor*deg_air

    ######### Degradacion por graining #########
    if abs(abs(air_temp)-abs(track_temp)) >=25:
        graining = 1.1
    else:
        graining = 1.0
    degradation_factor = degradation_factor*graining
    
    ######### Degradacion por longitud de pista #########
    degradation_factor = degradation_factor*length

    return degradation_factor

print(degradation('soft',35,27,4,3,2,'high',5,0.2))
print(degradation('medium',35,27,4,3,2,'high',5,0.2))
print(degradation('hard',35,27,4,3,2,'high',5,0.2))
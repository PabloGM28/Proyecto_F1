import numpy as np
from scipy.optimize import minimize

# Degradation function based on tire type and other parameters
def degradation(tire_type, laps, track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load):
    # Define degradation factor for each tire type based on input parameters
    degradation_factor = 1.0
    if tire_type == 'soft':
        # Degradation for soft tires
        degradation_factor *= 0.1 * laps
        degradation_factor *= (1.0 + 0.01 * high_speed_turns + 0.005 * medium_speed_turns + 0.002 * low_speed_turns)
        degradation_factor *= (1.0 + 0.002 * air_temp + 0.003 * track_temp)
        if wing_load == 'high':
            degradation_factor *= 1.1  # Higher degradation with high wing load
    elif tire_type == 'medium':
        # Degradation for medium tires
        degradation_factor *= 0.05 * laps
        degradation_factor *= (1.0 + 0.005 * high_speed_turns + 0.003 * medium_speed_turns + 0.001 * low_speed_turns)
        degradation_factor *= (1.0 + 0.001 * air_temp + 0.002 * track_temp)
        if wing_load == 'high':
            degradation_factor *= 1.05
    elif tire_type == 'hard':
        # Degradation for hard tires
        degradation_factor *= 0.03 * laps
        degradation_factor *= (1.0 + 0.003 * high_speed_turns + 0.002 * medium_speed_turns + 0.001 * low_speed_turns)
        degradation_factor *= (1.0 + 0.001 * air_temp + 0.001 * track_temp)
        if wing_load == 'high':
            degradation_factor *= 1.05
    
    return degradation_factor

# Objective function for optimization
def objective(x, params):
    total_degradation = 0
    num_tires = len(x) // 2  # Number of tires used in the strategy
    race_laps = params['race_laps']
    laps_used = 0  # Track the total laps used
    
    # Loop through each tire usage in the strategy
    for i in range(num_tires):
        tire_type_index = int(x[i * 2])  # Tire type (as an index)
        laps = int(x[i * 2 + 1])  # Number of laps for this tire type
        
        # Determine the tire type from the index
        tire_types = ['soft', 'medium', 'hard']
        tire_type = tire_types[tire_type_index]
        
        # Calculate degradation for the tire type and laps
        degradation = degradation(
            tire_type,
            laps,
            params['track_temp'],
            params['air_temp'],
            params['high_speed_turns'],
            params['medium_speed_turns'],
            params['low_speed_turns'],
            params['wing_load']
        )
        total_degradation += degradation
        
        # Track total laps used
        laps_used += laps
        
        # If total laps used exceeds race laps, stop
        if laps_used > race_laps:
            return float('inf')  # Penalty for exceeding the race laps
    
    # Penalty if the total laps used does not match race laps
    if laps_used != race_laps:
        return float('inf')
    
    return total_degradation

# Read parameters from the user
race_laps = int(input("Enter the total number of laps in the race: "))
track_temp = float(input("Enter the temperature of the track (°C): "))
air_temp = float(input("Enter the temperature of the air (°C): "))
high_speed_turns = int(input("Enter the number of high-speed turns: "))
medium_speed_turns = int(input("Enter the number of medium-speed turns: "))
low_speed_turns = int(input("Enter the number of low-speed turns: "))
wing_load = input("Enter the wing load (low, medium, high): ")

# Input parameters dictionary
params = {
    'race_laps': race_laps,
    'track_temp': track_temp,
    'air_temp': air_temp,
    'high_speed_turns': high_speed_turns,
    'medium_speed_turns': medium_speed_turns,
    'low_speed_turns': low_speed_turns,
    'wing_load': wing_load,
}

# Initial guess for optimization: Start with equal distribution of laps for each tire type
initial_guess = [0, race_laps // 3, 1, race_laps // 3, 2, race_laps // 3]

# Bounds for optimization
# Tire type index (0, 1, 2) and laps (1 to race_laps)
bounds = [(0, 2), (1, race_laps)] * 3

# Optimization using 'SLSQP' method
result = minimize(objective, initial_guess, args=(params,), method='SLSQP', bounds=bounds)

# Extracting optimal solution
optimal_solution = result.x

# Displaying the optimal strategy
print("Optimal strategy:")
num_tires = len(optimal_solution) // 2
for i in range(num_tires):
    tire_type_index = int(optimal_solution[i * 2])
    tire_types = ['soft', 'medium', 'hard']
    tire_type = tire_types[tire_type_index]
    laps = int(optimal_solution[i * 2 + 1])
    print(f"Tire {i + 1}: {tire_type}, Laps: {laps}")

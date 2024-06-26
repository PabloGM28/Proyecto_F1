from flask import Flask, redirect, url_for, render_template, request
from calculadora import estrategia_optima

app = Flask(__name__)

albert_park= {"high_speed":9,"medium_speed":4,"low_speed":3,"length":5.303,"laps":58}
bahrain = {"high_speed":9,"medium_speed":4,"low_speed":2,"length":5.412,"laps":57}
jeddah= {"high_speed":16,"medium_speed":9,"low_speed":2,"length":6.175,"laps":50}
interlagos= {"high_speed":6,"medium_speed":9,"low_speed":0,"length":4.309,"laps":71}
spa= {"high_speed":7,"medium_speed":9,"low_speed":3,"length":7.004,"laps":44}
suzuka= {"high_speed":11,"medium_speed":4,"low_speed":3,"length":5.807,"laps":53}

# Lista para almacenar la selección de neumáticos
tyre_selection = []
# Variables para almacenar la selección de tiempo y temperaturas
weather_selection = ""
asphalt_temp = ""
ambient_temp = ""
# Variables para almacenar la selección de longitud y vueltas
length_km = ""
laps = ""
# Variable para almacenar la selección de downforce
downforce_selection = ""
# Variables para almacenar la selección de curvas
corner_slow = ""
corner_medium = ""
corner_fast = ""
#Variables para el factor de degradación
factor_deterioration = ""

selected_circuit = ""

result = []
laps_per_compound = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tyres')
def tyres():
    return render_template('tyres.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/length')
def length():
    return render_template('length.html')

@app.route('/final_strategy')
def final_strategy():
    return render_template('final_strategy.html', result = result)

@app.route('/downforce')
def downforce():
    return render_template('downforce.html')

@app.route('/corners')
def corners():
    return render_template('corners.html')

@app.route('/deterioration')
def deterioration():
    return render_template('deterioration.html')


@app.route('/process_circuit_and_redirect', methods=['POST'])
def process_circuit_and_redirect():
    global selected_circuit
    if request.method == 'POST':
        # Obtener la selección del circuito del formulario
        selected_circuit = request.form.get('selected_circuit')
        # Imprimir la selección del circuito
        print("Selección del circuito:", selected_circuit)
        # Aquí puedes almacenar la selección en una base de datos si lo deseas
        # Redirigir al usuario a 'tyres.html'
        return redirect(url_for('tyres'))


# Ruta para procesar la selección de neumáticos y redirigir al usuario a "weather.html"
@app.route('/process_tyre_selection_and_redirect', methods=['POST'])
def process_tyre_selection_and_redirect():
    if request.method == 'POST':
        # Obtener la selección de neumáticos del formulario
        selected_tyres = request.form.getlist('tyre_selection[]')
        # Almacenar la selección de neumáticos globalmente
        global tyre_selection
        tyre_selection = selected_tyres
        # Imprimir la selección de neumáticos
        print("Selección de neumáticos:", tyre_selection)
        # Redirigir al usuario a la página "weather.html"
        return redirect(url_for('weather'))

# Ruta para procesar la selección de tiempo y temperaturas y redirigir al usuario a "length.html"
@app.route('/process_weather_selection_and_redirect', methods=['POST'])
def process_weather_selection_and_redirect():
    if request.method == 'POST':
        # Obtener la selección de tiempo y temperaturas del formulario
        global weather_selection, asphalt_temp, ambient_temp
        weather_selection = request.form['weather_selection']
        asphalt_temp = request.form['asphalt_temp']
        ambient_temp = request.form['ambient_temp']
        # Imprimir la selección del usuario
        print("Selección de tiempo:", weather_selection)
        print("Temperatura del asfalto:", asphalt_temp)
        print("Temperatura ambiente:", ambient_temp)
        # Redirigir al usuario a la página "length.html"
        return redirect(url_for('downforce'))

# Ruta para procesar la selección de longitud y vueltas y redirigir al usuario a "downforce.html"
@app.route('/process_length_and_redirect', methods=['POST'])
def process_length_and_redirect():
    if request.method == 'POST':
        # Obtener la selección de longitud y vueltas del formulario
        global length_km, laps,result
        length_km = request.form['length_km']
        laps = request.form['laps']
        # Imprimir la selección del usuario
        print("Longitud del circuito:", length_km, "Km")
        print("Número de vueltas:", laps)
        # Redirigir al usuario a la página "downforce.html"
        result = estrategia_optima(int(laps),int(asphalt_temp),int(ambient_temp),int(corner_fast),int(corner_medium),int(corner_slow),downforce_selection,float(length_km),float(factor_deterioration),weather_selection)
        print("Tu resultado", result)
        return redirect(url_for('final_strategy'))

# Ruta para procesar la selección de downforce y redirigir al usuario a "corners"
@app.route('/process_downforce_and_redirect', methods=['POST'])
def process_downforce_and_redirect():
    global downforce_selection
    if request.method == 'POST':
        # Obtener la selección de downforce del formulario
        downforce_selection = request.form.get('downforce_selection')
        # Imprimir la selección de downforce (para verificar en la consola)
        print("Selección de downforce:",downforce_selection)
        # Redirigir al usuario a la página "corners"
        return redirect(url_for('deterioration'))

@app.route('/process_deterioration_and_redirect', methods=['POST'])
def process_deterioration_and_redirect():
    if request.method == 'POST':
        # Obtener la selección del factor de degradación
        global factor_deterioration,result
        factor_deterioration = request.form['factor_deterioration']
        # Imprimir factor de degradación
        print ("El factor de degradación es:", factor_deterioration)
        
        # Verificar el valor de selected_circuit
        if selected_circuit == 'YOUR OWN CIRCUIT':
            # Redirigir al usuario a la página 'corners'
            return redirect(url_for('corners'))
        else:
            if selected_circuit == 'ALBERT PARK':
                result = estrategia_optima (albert_park['laps'],int(asphalt_temp),int(ambient_temp),albert_park['high_speed'],albert_park['medium_speed'],albert_park['low_speed'],downforce_selection,albert_park['length'],float(factor_deterioration),weather_selection)
                print("Tu estrategia es",result)
            elif selected_circuit == 'BAHRAIN':
                result = estrategia_optima(bahrain["laps"],int(asphalt_temp),int(ambient_temp),bahrain['high_speed'],bahrain['medium_speed'],bahrain['low_speed'],downforce_selection,bahrain["length"],float(factor_deterioration),weather_selection)
            elif selected_circuit == 'JEDDAH':
                result = estrategia_optima (jeddah['laps'],int(asphalt_temp),int(ambient_temp),jeddah['high_speed'],jeddah['medium_speed'],jeddah['low_speed'],downforce_selection,jeddah['length'],float(factor_deterioration),weather_selection)
                print("Tu etrategia es", result)
            elif selected_circuit == 'SPA':
                result = estrategia_optima(spa["laps"],int(asphalt_temp),int(ambient_temp),spa['high_speed'],spa['medium_speed'],spa['low_speed'],downforce_selection,spa["length"],float(factor_deterioration),weather_selection)
                print("Tu estrategia es",result)
            elif selected_circuit == 'INTERLAGOS':
                result = estrategia_optima(interlagos["laps"],int(asphalt_temp),int(ambient_temp),interlagos['high_speed'],interlagos['medium_speed'],interlagos['low_speed'],downforce_selection,interlagos["length"],float(factor_deterioration),weather_selection)
                print("Tu estrategia es",result)            
            elif selected_circuit == 'SUZUKA':
                result = estrategia_optima(suzuka["laps"],int(asphalt_temp),int(ambient_temp),suzuka['high_speed'],suzuka['medium_speed'],suzuka['low_speed'],downforce_selection,suzuka["length"],float(factor_deterioration),weather_selection)
                print("Tu estrategia es",result)
            return render_template('final_strategy.html', result=result)


# Ruta para procesar la selección de esquinas y redirigir al usuario a la página siguiente
@app.route('/process_corners_and_redirect', methods=['POST'])
def process_corners_and_redirect():
    if request.method == 'POST':
        # Obtener la selección de esquinas del formulario
        global corner_slow,corner_medium,corner_fast
        corner_slow = request.form['corner_slow']
        corner_medium = request.form['corner_medium']
        corner_fast = request.form['corner_fast']
        # Imprimir la selección de esquinas (para verificar en la consola)
        print("Curvas lentas:",corner_slow )
        print("Curvas medias:",corner_medium )
        print("Curvas rápidas:",corner_fast )
        # Redirigir al usuario a la siguiente página
        return redirect(url_for('length'))
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)

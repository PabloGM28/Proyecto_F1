from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Lista para almacenar la selección de neumáticos
tyre_selection = []
# Variables para almacenar la selección de tiempo y temperaturas
weather_selection = ""
asphalt_temp = ""
ambient_temp = ""

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
    return render_template('final_strategy.html')

@app.route('/downforce')
def downforce():
    return render_template('downforce.html')

@app.route('/corners')
def corners():
    return render_template('corners.html')

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
        return redirect(url_for('length'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
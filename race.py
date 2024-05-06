from degradacion import degradation 

## Es buena idea adimensionalizar la degradacion:


tyre = ['soft','medium','hard'] # mis neumáticos
hards = degradation('hard', 33,28,5,6,3,'medium',4.8,0.1) # parametro adimensionalizador
deg_adim = [1, 1, 1] # declaro el vector que voy a rellenar

# Adimensionalizo la degradacion en funcion de la del duro, que es el mas lento pero mas duradero
for i in tyre:
    deg_adim[tyre.index(i)] = degradation(i, 33,28,5,6,3,'medium',4.8,0.1)/hards

print(deg_adim) # un print de prueba, que nunca viene mal


# Entrega N° 4 - Dataset Flights

- Javier Ceferino Rodriguez
- Maria Eva Ortega
- Julio Gonzalez
- Gonzalo Estevez

## Introducción

En el siguiente trabajo analizamos los dataset de vuelos (`flights`) y aviones (`planes`) con el objetivo de reforzar las trayectorias con mayor demanda para lograr aumentar las ganancias y mejorar la experiencia de los pasajeros.

Tenemos las siguientes aerolíneas para elegir, el la cual se representan la cantidad de vuelos que tuvieron en el año:

![plot 1](./assets/plot1.png)

## Aerolínea UA (United Airlines)

A partir de lo observado en el gráfico anterior, vamos a enfocar nuestro análisis en la aerolínea (`carrier`) **United Airlines** (`UA`) ya que es la que contiene la mayor cantidad de vuelos. Sin embargo, este análisis sencillamente se podría aplicar al resto de las aerolíneas de este dataset con más de 1000 vuelos.

Como primera aproximación a nuestro objetivo, vemos la cantidad de vuelos según el orígen de cada vuelo en UA (se muestran solamente los que tengan 2000 vuelos o más para apreciar mejor los que tengan más cantidad):

![plot 2](./assets/plot2.png)

Vemos que tenemos los aeropuertos EWR (_Aeropuerto Internacional Libertad de Newark_), LGA (_Aeropuerto Internacional de la Guardia_) y JFK (_Aeropuerto Internacional de John F. Kennedy_). A simple vista EWR destaca en cantidad de vuelos, pero no es parámetro suficiente para tomar una decisión.

Ahora, sumamos los destinos como 3° variable en el gráfico:

![plot 3](./assets/plot3.png)

Si bien se sigue manteniendo EWR como el aeropuerto con mayor cantidad de vuelos (con los destinos SFO, IAH y ORD), podemos sumar otra variable más si incluímos el dataset de aviones (`planes`) a nuestro análisis. Elegimos como nueva variable la cantidad de asientos en cada avión (se muestran solamente los que tengan 1200 vuelos o más para apreciar mejor los que tengan más cantidad):

![plot 4](./assets/plot4.png)


## Conclusión

En este último gráfico tenemos un mejor panoráma para tomar una decisión: JFK (con vuelos a SFO y LAX) y EWR (con vuelo a SFO) son las trayectorias con mayor demanda que elige el público.

Podemos agregar un avión a cada trayectoria para mejorar tanto económicamente, como también la experiencia de usuario al momento de elegir el vuelo.

---

_Código, imágenes y datasets en [este repositorio](https://github.com/JaviCeRodriguez/Intro_Ciencia_Datos/tree/main/Entregas/Entrega4)._
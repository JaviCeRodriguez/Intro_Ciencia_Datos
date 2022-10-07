# Entrega N° 6 - Modelo lineal

Integrantes:
- Ulrich Marcelo
- Anelis Prediger
- Rodriguez Javier

## Tarea 1: Tests estadísticos

Usamos la librería modelr para utilizar datos simulados (`sim1`). Realizamos el ajuste lineal con `lm`, calculamos predicciones y las graficamos:

![Tarea 1 - 2](assets/tarea1-2.png)

Calculamos los residuos y graficamos

![Tarea 1 - 3 - Con x](assets/tarea1-3-x.png)

![Tarea 1 - 3 - Con y](assets/tarea1-3-y.png)

Exploramos los gráficos de `plot(model)` para ver:

- Los datos fiteados vs los residuos

![Tarea 1 - 4 - a](assets/tarea1-4.png)

- Normal Q-Q

![Tarea 1 - 4 - b](assets/tarea1-4b.png)

- Scale Location

![Tarea 1 - 4 - c](assets/tarea1-4c.png)

- Residuos vs Leverage

![Tarea 1 - 4 - d](assets/tarea1-4d.png)

Aplicamos `summary` y obtenemos los coeficientes:

![Tarea 1 - 5](assets/tarea1-5.png)

Agregamos ruido a los valores de y con `rnorm`, agregando la media de y. Graficamos:

![Tarea 1 - 6](assets/tarea1-6.png)



## Tarea 2: Términos de interacción

En esta tarea usamos `sim3` para entender los términos de interacción con el modelo lineal.

Tenemos dos variables categóricas `x2` y `rep` y el resto (`x1`, `y` y `sd`) son continua.

Realizamos un scatter plot para visualizar todos los datos y variables del dataset:

![Tarea 2 - 2](assets/tarea2-2.png)

Vemos la diferencia entre fórmula de suma y producto. En las tablas vemos el resultado de utilizar las variables categóricas. Corresponden a los valores de cada término de la fórmula.

Ahora, ajustamos ambos modelos y lo primero que observamos en las tablas es que las predicciones tienen distintos comportamientos. Si lo graficamos:

- Para suma:
![Tarea 2 - 4 - Modelo 1](assets/tarea2-4a.png)

- Para producto:
![Tarea 2 - 4 - Modelo 2](assets/tarea2-4b.png)

Claramente, el segundo modelo que es por producto se ajusta mejor a nuestro dataset

Ejemplos de casos de uso para estos modelos:

- Diámetro de árboles según especies o comuna
- Seguros para géneros, fumadores o no

## Tarea 3: Transformación de variables

Importamos el dataset de diamantes y usamos las variables `carat` y `price`.

![Tarea 3 - 1 - cut](assets/tarea3-1-cut.png)

El corte del diamante claramente varía el precio y kilates. Nos animamos a ver con otra variable `clarity`:

![Tarea 3 - 1 - clarity](assets/tarea3-1.png)

Realizamos las predicciones para `cut` y vemos los resultados en el siguiente gráfico:

![Tarea 3 - 2](assets/tarea3-2.png)

Calculamos los residuos y graficamos vs predicciones:

![Tarea 3 - 3](assets/tarea3-3.png)

Vemos que los residuos de los datos decaen a medida que aumenta la relación entre `price` y `carat`.

En un nuevo modelo, proponemos utilizar `clarity`, `cut` y `color`. Filtramos los datos para el mejor diamante (según dataset).

![Tarea 3 - 4](assets/tarea3-4.png)

Para finalizar la tarea 3, aplicamos un modelo logarítmico, observamos sus residuos y la media:

- Modelo logarítmico:
![Tarea 3 - 5](assets/tarea3-5a.png)

- Media de residuos:
![Tarea 3 - 5](assets/tarea3-5b.png)


## Tarea 4: Confounders y modelo causal

Hacemos un gráfico de cajas para evaluar la dependencia del corte en el precio de los diamantes:

![Tarea 4 - 2](assets/tarea4-2.png)

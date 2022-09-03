"""
Introducción a la Ciencia de Datos - 2C 2022
Guía para la entrega N° 1

Author: Javier Ceferino Rodriguez
"""

import matplotlib.pyplot as plt
import pandas as pd


def read_dataset(file_name: str) -> pd.DataFrame:
    """
    Lee un archivo xlsx y lo devuelve como un DataFrame
    """
    return pd.read_excel(file_name)


def info_dataset(df: pd.DataFrame) -> None:
    """
    Info de interés del dataframe
    """
    # Observamos las primeras 5 filas
    print(df.head(20))

    # Imprimimos el número de filas y columnas
    print(f'Número de datos (filas): {df.shape[0]}')
    print(f'Número de variables (columnas): {df.shape[1]}')

    # Máximo y mínimo de "bmi (body-mass-index)"
    print(f'Máximo bmi: {df["bmi (body-mass-index)"].max()}')
    print(f'Mínimo bi: {df["bmi (body-mass-index)"].min()}')

    # Máximo y mínimo de "charges"
    print(f'Máximo charges: {df["charges"].max()}')
    print(f'Mínimo charges: {df["charges"].min()}')



def main() -> None:
    """
    Función principal
    """
    plt.style.use('ggplot')

    # Leemos el dataset y observamos las primeras 5 filas
    df = read_dataset('./Guias/Guia1/Guia1_insurance.xlsx')

    # Imprimimos la info del dataset
    info_dataset(df)

    # Plot de "bmi (body-mass-index)" vs "age"
    df.plot(x='age', y='bmi (body-mass-index)', kind='scatter', title="bmi vs age")
    # Trazamos una recta horizontal en 18,5 y otra en 24,9
    plt.axhline(y=18.5, color='r', linestyle='--')
    plt.axhline(y=24.9, color='r', linestyle='--')
    plt.show()

    # Plot de "charges" vs "age"
    df.plot(x='age', y='charges', kind='scatter', title="charges vs age")
    plt.show()

    # Plot de "age" vs "bmi", with s = "charges" * 0.01
    plt.scatter(x='age', y='charges', s=df['bmi (body-mass-index)'] * 10, color='#06DD1F', data=df, alpha=0.5)
    plt.title('age vs charges, with bmi * 10 scale')
    plt.xlabel('age')
    plt.ylabel('charges')
    plt.show()

    # Plot de "age" vs "charges", with s = "bmi" * 10
    df_female = df[df.sex == 'female']
    df_male = df[df.sex == 'male']
    plt.scatter(x='age', y='charges', s=df_female['bmi (body-mass-index)'] * 10, color='#DA70D6', data=df_female, alpha=0.3)
    plt.scatter(x='age', y='charges', s=df_male['bmi (body-mass-index)'] * 10, color='#069AF3', data=df_male, alpha=0.3)
    plt.title('age vs charges, with bim * 10 scale')
    plt.xlabel('age')
    plt.ylabel('charges')
    plt.legend(['charges female', 'charges male'])
    plt.show()

    # Plot de "age" vs "charges", with s = "bmi" * 10
    df_female_filtered = df[(df.sex == 'female') & (df.charges < 17500)]
    df_male_filtered = df[(df.sex == 'male') & (df.charges < 17500)]
    plt.scatter(x='age', y='charges', s=df_female_filtered['bmi (body-mass-index)'] * 10, color='#DA70D6', data=df_female_filtered, alpha=0.3)
    plt.scatter(x='age', y='charges', s=df_male_filtered['bmi (body-mass-index)'] * 10, color='#069AF3', data=df_male_filtered, alpha=0.3)
    plt.title('age vs charges (until 17500), with bim * 10 scale')
    plt.xlabel('age')
    plt.ylabel('charges')
    plt.legend(['charges female', 'charges male'], loc="lower right")
    plt.show()

if __name__ == '__main__':
    main()
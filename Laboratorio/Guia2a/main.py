"""
Introducción a la Ciencia de Datos - 2C 2022
Guía N° 2 - Parte a

Author: Javier Ceferino Rodriguez
"""
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
    # Observamos las primeras 20 filas
    # print(df.head(20))

    # Edades, categorías de trabajo, categorías de educación e intervalo de horas trabajadas por semana
    print(f'Edad mínima: {df["age"].min()} - Edad máxima: {df["age"].max()}')
    print(f'Categorías de trabajo: {", ".join(df["workclass"].unique())}')
    print(f'Categorías de educación: {", ".join(df["education"].unique())}')
    print(f'Intervalo de horas trabajadas p/ semana: {df["hours.per.week"].min()} - {df["hours.per.week"].max()}')


def main():
    df = read_dataset('Laboratorio\Guia2a\dataset_guía_2_adult_census.xlsx')
    info_dataset(df=df)

if __name__ == '__main__':
    main()
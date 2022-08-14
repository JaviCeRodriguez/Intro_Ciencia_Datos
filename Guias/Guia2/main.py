"""
Introducción a la Ciencia de Datos - 2C 2022
Guía para la entrega N° 2

Author: Javier Ceferino Rodriguez
"""

from turtle import title
import matplotlib.pyplot as plt
import pandas as pd


def read_dataset(file_name: str) -> pd.DataFrame:
    """
    Lee un archivo csv y lo devuelve como un DataFrame
    """
    return pd.read_csv(file_name)


def filter_by_height(df: pd.DataFrame, height: int) -> pd.DataFrame:
    """
    Quedarse solo con los árboles mayores a 20 mts
    """
    return df[df['altura_arbol'] > height]


def group_by_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encontrar qué especies son las que tienen más especímenes más altos que 20 mts (agrupar y
    ordenar). Quedarse con las cuatro especies más numerosas.
    """
    df_group = df.groupby(['nombre_cientifico'])
    df_group_sorted = df_group.size().sort_values(ascending=False)
    df_group_sorted_top4 = df_group_sorted.head(4)
    df_top4_by_height = df[df['nombre_cientifico'].isin(df_group_sorted_top4.index)]
    return df_top4_by_height


def group_by_street(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encontrar las tres calles (calle_nombre) con más árboles más altos que 20 mts que sean de estas especies.
    """
    df_group_street = df.groupby(['calle_nombre'])
    df_group_street_sorted = df_group_street.size().sort_values(ascending=False)
    df_group_street_sorted_top3 = df_group_street_sorted.head(3)
    df_top3_by_height = df[df['calle_nombre'].isin(df_group_street_sorted_top3.index)]
    return df_top3_by_height


def plot_dataframe(df: pd.DataFrame, list_plot_str: list) -> None:
    """
    Presentar los resultados encontrados en una gráfico de barras.
    Cantidad de arboles por cada especie, agrupados por calle.
    """
    [title, xlabel, ylabel, legend_title] = list_plot_str
    df_top3_result = df.groupby(['calle_nombre', 'nombre_cientifico']).size()
    print(df_top3_result)
    ax = df_top3_result.unstack().plot(kind='bar', rot=0)
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy() 
        ax.annotate(f'{height:.0f}', (x + width/2, y + height*1.02), ha='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(title=legend_title)
    plt.show()


def main():
    plt.rcParams.update({'font.size': 14})
    df = read_dataset('Guias/Guia2/arbolado_comuna14.csv')
    
    df = filter_by_height(df, 20) # Puede ser 2do paso
    df = group_by_name(df) # Puede ser 1er paso

    df = group_by_street(df)
    plot_dataframe(
        df, 
        [
            'Cantidad de árboles > a 20 mts por calle, diferenciado por especies', 
            'Calles de la Comuna 14 de CABA', 
            'Cantidad de árboles > a 20 mts', 
            'Especies'
        ]
    )

if __name__ == '__main__':
    main()


# Fuentes
# How to display percentage above grouped bar chart: https://stackoverflow.com/questions/52080991/how-to-display-percentage-above-grouped-bar-chart

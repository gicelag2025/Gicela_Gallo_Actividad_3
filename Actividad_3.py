import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import io


class Actividad3:
    def __init__(self, ruta_resultados="resultado_actividad_3/"):
        self.ruta_resultados = ruta_resultados
        self._crear_directorio()

    def _crear_directorio(self):
        """Crea el directorio si no existe"""
        if not os.path.exists(self.ruta_resultados):
            os.makedirs(self.ruta_resultados)

    def guardar_csv(self, df, nombre_archivo):
        """Guarda un DataFrame como CSV"""
        ruta_completa = os.path.join(self.ruta_resultados, nombre_archivo)
        df.to_csv(ruta_completa, index=False, encoding="utf-8")
        print(f"Archivo guardado en: {ruta_completa}")


# Crear instancia de la clase
actividad = Actividad3()

# Punto 1
df = pd.DataFrame({'Granadillas': [20], 'Tomates': [50]})
actividad.guardar_csv(df, "punto_1_frutas.csv")

# Punto 2
ventas_frutas = pd.DataFrame({'Granadillas': [20, 49], 'Tomates': [50, 100]},  
                             index=['Ventas 2021', 'Ventas 2022'])
actividad.guardar_csv(ventas_frutas, "punto_2_ventas_frutas.csv")

# Punto 3
utensilios = pd.Series({'Cuchara': '3 unidades',  
                        'Tenedor': '2 unidades',  
                        'Cuchillo': '4 unidades',  
                        'Plato': '5 unidades'},  
                        name='cocina')
utensilios_df = utensilios.to_frame()
actividad.guardar_csv(utensilios_df, "punto_3_utensilios.csv")

# Punto 4
archivo_vinos = "resultado_actividad_3/punto_4_winemag-data_first150k.csv" 
if os.path.exists(archivo_vinos):
    review = pd.read_csv(archivo_vinos)
else:
    review = None
    print("Error: Archivo de vinos no encontrado.")

# Punto 5
if review is not None:
    actividad.guardar_csv(review.head(5), "punto_5_wine_reviews.csv")

# Punto 6: Guardar información del dataset
if review is not None:
    buffer = io.StringIO()
    review.info(buf=buffer)
    info_text = buffer.getvalue()
    info_df = pd.DataFrame({'Info': [info_text]})
    actividad.guardar_csv(info_df, "punto_6_info_dataset.csv")

# Punto 7
if review is not None and 'price' in review.columns:
    precio_promedio_df = pd.DataFrame({'Precio promedio': [review['price'].mean()]})
    actividad.guardar_csv(precio_promedio_df, "punto_7_precio_promedio.csv")

# Punto 8
if review is not None and 'price' in review.columns:
    precio_maximo = review['price'].dropna().max()
    precio_maximo_df = pd.DataFrame({'Precio más alto': [precio_maximo]})
    actividad.guardar_csv(precio_maximo_df, "punto_8_precio_maximo.csv")

# Punto 9
if review is not None and 'province' in review.columns:
    vinos_california = review[review['province'] == 'California']
    actividad.guardar_csv(vinos_california.head(20), "punto_9_vinos_california.csv")


# Punto 10
if review is not None and 'price' in review.columns:
    idx_max_price = review['price'].idxmax()
    vino_mas_caro_df = review.loc[[idx_max_price]]
    actividad.guardar_csv(vino_mas_caro_df, "punto_10_vino_mas_caro.csv")

# Punto 11
if review is not None and 'variety' in review.columns:
    variedades_comunes_df = vinos_california['variety'].value_counts().head(15).reset_index()
    variedades_comunes_df.columns = ['Variedad', 'Cantidad']
    actividad.guardar_csv(variedades_comunes_df, "punto_11_variedades_comunes.csv")

# Punto 12
if review is not None and 'variety' in review.columns:
    top_10_variedades_df = vinos_california['variety'].value_counts().head(10).reset_index()
    top_10_variedades_df.columns = ['Variedad', 'Cantidad']
    actividad.guardar_csv(top_10_variedades_df, "punto_12_top_10_variedades.csv")

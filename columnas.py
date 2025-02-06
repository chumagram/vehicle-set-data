import pandas as pd
from datetime import datetime

def get_columns():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    # Obtener y mostrar los nombres de las columnas
    print("Nombres de las columnas en el archivo CSV:")
    print(df.columns.tolist())

def get_unique_values(csv_file, column_name):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Obtener valores únicos de la columna especificada en orden alfabético
    unique_values = sorted(df[column_name].dropna().astype(str).unique())

    # Mostrar los valores únicos
    print(f"Valores únicos en la columna '{column_name}':")
    print(unique_values)

def replace_values_in_column(csv_file, column_name, search_value, replace_value):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Reemplazar los valores en la columna, incluyendo NaN si search_value es NaN
    if pd.isna(search_value):
        df[column_name] = df[column_name].fillna(replace_value)
    else:
        df[column_name] = df[column_name].replace(search_value, replace_value)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_upd.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo actualizado guardado como: {output_file}")

def capitalize_column_values(csv_file, column_name):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Convertir valores de la columna al formato "Primera letra en mayúscula"
    df[column_name] = df[column_name].apply(lambda x: x.capitalize() if isinstance(x, str) and not x.isupper() else x)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_capitalized.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con valores capitalizados guardado como: {output_file}")

def lowercase_column_values(csv_file, column_name):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Convertir valores de la columna a minúsculas
    df[column_name] = df[column_name].apply(lambda x: x.lower() if isinstance(x, str) else x)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_lowercase.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con valores en minúsculas guardado como: {output_file}")

def collect_values_from_column(csv_file, column_a, column_b, search_value):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si las columnas existen en el DataFrame
    if column_a not in df.columns or column_b not in df.columns:
        print(f"Error: Una o ambas columnas '{column_a}' y '{column_b}' no existen en el archivo CSV.")
        return

    # Buscar coincidencias en la columna A y agregar valores de la columna B a una lista
    result_list = df[df[column_a] == search_value][column_b].dropna().tolist()

    # Imprimir la lista de valores
    print(f"Valores encontrados en la columna '{column_b}' donde '{column_a}' es '{search_value}':")
    print(result_list)

def copy_long_strings(csv_file, source_column, target_column):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si las columnas existen en el DataFrame
    if source_column not in df.columns or target_column not in df.columns:
        print(f"Error: Una o ambas columnas '{source_column}' y '{target_column}' no existen en el archivo CSV.")
        return

    # Copiar valores con más de dos caracteres de source_column a target_column
    df[target_column] = df[source_column].apply(lambda x: x if isinstance(x, str) and len(x) > 2 else None)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_long_strings_copied.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con valores largos copiados guardado como: {output_file}")

def replace_long_strings(csv_file, column_name, replace_value):
    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Reemplazar valores con más de dos caracteres por replace_value
    df[column_name] = df[column_name].apply(lambda x: replace_value if isinstance(x, str) and len(x) > 2 else x)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_long_strings_replaced.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con valores largos reemplazados guardado como: {output_file}")

def replace_with_dictionary(csv_file, column_name):
    # Diccionario de abreviaturas de estados a nombres completos
    mapping = {
        'beige': 'Beige',
        'black': 'Negro',
        'blue': 'Azul',
        'brown': 'Marrón',
        'burgundy': 'Burdeos',
        'desconocido': 'Desconocido',
        'gold': 'Dorado',
        'gray': 'Gris',
        'green': 'Verde',
        'off-white': 'Blanco hueso',
        'orange': 'Naranja',
        'purple': 'Púrpura',
        'red': 'Rojo',
        'silver': 'Plateado',
        'tan': 'Bronceado',
        'white': 'Blanco',
        'yellow': 'Amarillo',
        '—': 'Desconocido'
    }

    # Cargar el archivo CSV en un DataFrame con delimitador ';'
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Reemplazar las abreviaturas por los nombres completos
    df[column_name] = df[column_name].apply(lambda x: mapping.get(x.lower(), x) if isinstance(x, str) else x)

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_replaced.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con estados reemplazados guardado como: {output_file}")

def transform_saledate_to_powerbi(csv_file, column_name):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        print(f"Error: La columna '{column_name}' no existe en el archivo CSV.")
        return

    # Función para transformar las fechas
    def parse_date(date_str):
        try:
            # Limpiar el formato eliminando todo lo que está entre paréntesis
            clean_date_str = date_str.split(' (')[0].strip()
            # Parsear la fecha al formato deseado
            dt = datetime.strptime(clean_date_str, "%a %b %d %Y %H:%M:%S %Z%z")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            return None  # Si ocurre un error, retorna None

    # Transformar la columna de fechas
    df[column_name] = df[column_name].apply(parse_date)

    # Reportar valores no convertidos
    invalid_dates = df[df[column_name].isna()]
    if not invalid_dates.empty:
        print(f"Se encontraron fechas no válidas. Total: {len(invalid_dates)}")

    # Guardar el archivo actualizado
    output_file = csv_file.replace(".csv", "_saledate_transformed.csv")
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo con fechas transformadas guardado como: {output_file}")

# Parámetros
csv_file = r".\dataset-car_prices_cleaned.csv"  # Ruta al archivo CSV con prefijo raw
column_name = "make"  # Nombre de la columna a analizar
search_value = float('nan')  # Valor a buscar en la columna. Usar float('nan') si es un NaN
replace_value = "desconocido"  # Valor por el que se reemplazará

# Llamadas
#get_columns()
get_unique_values(csv_file, column_name)
#replace_values_in_column(csv_file, column_name, search_value, replace_value)
#capitalize_column_values(csv_file, column_name)
#lowercase_column_values(csv_file, column_name)
#collect_values_from_column(csv_file, column_a="state", column_b="condition", search_value="3vwd17ajxfm315938")
#copy_long_strings(csv_file, source_column="state", target_column="vin")
#replace_long_strings(csv_file, column_name, replace_value)
#replace_with_dictionary(csv_file, column_name)
#transform_saledate_to_powerbi(csv_file, column_name)